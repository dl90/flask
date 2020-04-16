from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, login_user, current_user, logout_user
from datetime import timedelta, datetime
from jinja2 import TemplateNotFound
from markupsafe import escape
from ..create_server import bcrypt, login_manager, db
from ..util.forms import LoginForm, NewUserForm
from ..db.schema import User

# /auth...
auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    user = None
    try:
        user = User.query.get(user_id)
    except:
        print(f"Error loading {user_id} from database")
    finally:
        return user


@login_manager.unauthorized_handler
def unauthorized():
    flash("👮‍♀️ Unauthorized", "error")
    return redirect(url_for('initialize'))


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "GET":
        try:
            return render_template("auth/login.html", title="👮‍♂️" ,route=url_for(".login"), form=form)
        except TemplateNotFound:
            abort(404)

    if request.method == "POST" and form.validate_on_submit():
        user = False
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('initialize'))
        if user:
            result = bcrypt.check_password_hash(
                user.password, form.password.data)
            if result:
                login_user(user, duration=timedelta(minutes=20))
                return redirect(url_for('secure.home'))
            else:
                flash("Incorrect username or password", "error")
                return redirect(url_for(".login"))
        else:
            flash("Incorrect username or password", "error")
            return redirect(url_for(".login"))
    else:
        flash(form.errors, "error")
        return redirect(url_for(".login"))


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = NewUserForm()

    if request.method == "GET":
        try:
            return render_template("auth/sign-up.html", title="💣" ,route=url_for(".sign_up"), form=form)
        except TemplateNotFound:
            abort(404)

    if request.method == 'POST' and form.validate_on_submit():
        user = False
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('initialize'))
        if not user:
            pw_hash = bcrypt.generate_password_hash(form.password_1.data, 10)
            new_user = User(username=escape(form.username.data),
                            password=pw_hash, creation_date=datetime.now())
            db.session.add(new_user)
            try:
                db.session.commit()
                flash(f"{new_user.username} successfully created", "success")
                return redirect(url_for("initialize"))
            except:
                flash(
                    "Something is wrong with the database, contact your admin", "error")
                return redirect(url_for("initialize"))
        else:
            flash("Please chose another username", "info")
            return redirect(url_for(".sign_up"))
    else:
        flash(form.errors, "error")
        return redirect(url_for(".sign_up"))


@auth.route('/logout')
@login_required
def logout():
    flash(f"{current_user.username} has logged out", "info")
    logout_user()
    return redirect(url_for('initialize'))
