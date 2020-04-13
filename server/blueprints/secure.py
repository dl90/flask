from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
secure = Blueprint('secure', __name__)


@secure.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "GET":
        if current_user.is_authenticated:
            return render_template('home.html', page='home', name=current_user.username)
        else:
            return redirect(url_for("initialize"))


@secure.route('/library', methods=["GET"])
@login_required
def library():
    return render_template('home.html', page='library', name=current_user.username)