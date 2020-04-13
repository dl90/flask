from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from util.forms import LoginForm, NewUserForm, SearchForm, AddArtistForm
from markupsafe import escape
from datetime import timedelta
from jinja2 import FileSystemLoader

import requests
import os


def api_search(query):
    api = "https://deezerdevs-deezer.p.rapidapi.com/search"
    headers = {'x-rapidapi-key': "c037579dddmsh470ab55c12a8ddap18dc96jsn4c0f53fa75cf"}
    params = {"q": query}
    response = requests.request("GET", api, headers=headers, params=params)
    return response.json()



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
