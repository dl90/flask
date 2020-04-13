from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from util.forms import LoginForm, NewUserForm, SearchForm, AddArtistForm
from markupsafe import escape
from datetime import timedelta
from jinja2 import FileSystemLoader

import requests
import os

# FileSystemLoader([os.getcwd()])

app = Flask(__name__,
            static_url_path="",
            static_folder='public',
            template_folder='templates')
app.config["SECRET_KEY"] = "maQ97z2uMNyWthgvrpKd36DfW4pbCkzFsdEJ6P54tq5wkzdNE2SA2JzJU7AjD3aotiU4go8p9usLFssa852GEd3n3UbpwVVUT4csDjEdSrFZnGXk68pEChHgVA5cmmuB"
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# DO NOT FORMAT
# try:
from db import schema
# except ImportError:
#     print(ImportError.msg)
#     print("Import error")
# from db import db


# flask_login
login_manager = LoginManager()
login_manager.init_app(app)

def api_search(query):
    api = "https://deezerdevs-deezer.p.rapidapi.com/search"
    headers = {'x-rapidapi-key': "c037579dddmsh470ab55c12a8ddap18dc96jsn4c0f53fa75cf"}
    params = {"q": query}
    response = requests.request("GET", api, headers=headers, params=params)
    return response.json()

@login_manager.user_loader
def load_user(user_id):
    user = None
    try:
        user = User.query.get(user_id)
    except:
        print(f"Error loading {user_id} from database")
    finally:
        return user


@app.route('/')
def landing_page():
    return render_template("auth/index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("auth/login.html", form=form)
    if request.method == "POST" and form.validate_on_submit():
        user = False
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('landing_page'))
        if user:
            result = bcrypt.check_password_hash(user.password, form.password.data)
            if result:
                login_user(user, duration=timedelta(minutes=20))
                return redirect(url_for('home'))
            else:
                flash("Incorrect username or password", "error")
                return redirect(url_for('login'))
        else:
            flash("Incorrect username or password", "error")
            return redirect(url_for('login'))
    else:
        flash(form.errors, "error")
        return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    flash(f"{current_user.username} has logged out", "info")
    logout_user()
    return redirect(url_for('landing_page'))


@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = NewUserForm()
    if request.method == "GET":
        return render_template("auth/sign-up.html", form=form)
    if request.method == 'POST' and form.validate_on_submit():
        user = False
        try:
            user = User.query.filter_by(username=form.username.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('landing_page'))
        if not user:
            pw_hash = bcrypt.generate_password_hash(form.password_1.data, 10)
            new_user = User(username=form.username.data, password=pw_hash)
            db.session.add(new_user)
            try:
                db.session.commit()
                flash(f"{new_user.username} successfully created", "success")
                return redirect(url_for("landing_page"))
            except:
                flash("Something is wrong with the database, contact your admin", "error")
                return redirect(url_for("landing_page"))
        else:
            flash("Please chose another username", "info")
            return redirect(url_for("sign_up"))
    else:
        flash(form.errors, "error")
        return redirect(url_for("sign_up"))


@app.route("/home")
@login_required
def home():
    if current_user.is_authenticated:
        return render_template('home.html', page='home', name=current_user.username)
    else:
        return redirect(url_for("landing_page"))


@app.route('/library', methods=["GET"])
@login_required
def library():
    return render_template('home.html', page='library', name=current_user.username)


@app.route('/search', methods=["POST"])
@login_required
def search():
    search_form = SearchForm()
    form = AddArtistForm()

    if request.method == 'POST' and search_form.validate_on_submit():
        results = False
        try:
            results = api_search(search_form.query.data)
        except:
            flash("Something went wrong with the search API, contact your admin", "error")
            artists = Artist.query.all()
            return redirect(url_for('artists'))
        if results:
            flash("Search successful", "success")
            return render_template('artists.html', search_results=results, form=form, search_form=search_form)
    else:
        flash(search_form.errors, "error")
        return redirect(url_for("artists"))


@app.route("/artists", methods=["GET", "POST"])
@login_required
def artists():
    form = AddArtistForm()
    search_form = SearchForm()
    if request.method == "GET":
        artists = Artist.query.all()
        return render_template("artists.html",
                                search_form=search_form,
                                form=form,

                                appName=" Music",
                                alt="artist image",
                                profileImage="/css/images/profile_image.jpg",
                                artistName="ArtistName",
                                albumArt="/css/images/albumImage.jpg",
                                title="albumTitle",
                                album_page="albums",
                                playlist_page="playlists",
                                playlistArt="/css/images/playlistArt.jpeg",
                                playlistTitle="Playlist Title",
                                artists=artists
                                )

    if request.method == 'POST' and form.validate_on_submit():
        artist = False
        try:
            artist = Artist.query.filter_by(first_name=form.first_name.data, last_name=form.last_name.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('artists'))
        if not artist:
            # new_artist = form.populate_obj(Artist())
            new_artist = Artist(first_name=form.first_name.data, last_name=form.last_name.data, display_pic=form.display_pic.data)
            db.session.add(new_artist)
            try:
                db.session.commit()
                flash(f"{new_artist} added", "success")
                return redirect(url_for("artists"))
            except:
                flash("Something is wrong with the database, contact your admin", "error")
                return redirect(url_for("artists"))
    else:
        flash(form.errors, "error")
        return redirect(url_for("artists"))

@app.route("/albums")
@login_required
def albums():
    return render_template("albums.html",
                           appName=" Music",
                           artistName="ArtistName",
                           albumArt="/css/images/albumImage.jpg",
                           title="albumTitle",
                           albumName="Album Name",
                           artist_page="artists",
                           songName="Amazing Song"
                           )


@app.route("/playlists")
@login_required
def playlists():
    return render_template("playlists.html",
                           appName=" Music",
                           profileImage="/css/images/profile_image.jpg",
                           artistName="ArtistName",
                           albumArt="/css/images/albumImage.jpg",
                           title="albumTitle",
                           album_page="albums",
                           playlist_page="playlists",
                           playlistArt="/css/images/playlistArt.jpeg",
                           playlistTitle="Playlist Title",
                           songName="Amazing Song",
                           playlistName="playlistName"
                           )


# Listener
if __name__ == "__main__":
    app.run(port=9999, debug=True)
