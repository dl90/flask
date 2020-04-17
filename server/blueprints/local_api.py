from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..util.forms import SearchForm, AddArtistForm
from ..db.schema import Artist
from ..create_server import db
from dotenv import load_dotenv
import requests
import os

# /api/local..
local = Blueprint("local_api", __name__)


def api_search(query):
    load_dotenv(verbose=True)
    KEY      = os.getenv("X-RAPIDAPI-KEY")
    URL      = os.getenv("RAPIDAPI-URL")
    headers  = { 'x-rapidapi-key': KEY }
    params   = { "q": query }
    response = requests.request("GET", URL, headers=headers, params=params)
    return response.json()


@local.route("/search", methods=["POST"])
@login_required
def search():
    search_form = SearchForm()

    if request.method == "POST" and search_form.validate_on_submit():
        results = False
        try:
            results = api_search(search_form.query.data)
        except:
            flash("Something went wrong with the search API, contact your admin", "error")
            artists = Artist.query.all()
            return redirect(url_for("home"))
        if results:
            flash("Search successful", "success")
            return render_template("console/search.html", name=current_user.username, title="🕵️‍♂️",
            search_result=results, search_form=search_form, route=url_for("local_api.search"))
    else:
        flash(search_form.errors, "error")
        return redirect(url_for("home"))


@local.route("/artist", methods=["POST", "PUT", "DELETE"])
@login_required
def artist():
    form = AddArtistForm()

    if request.method == "POST" and form.validate_on_submit():
        artist = False
        try:
            artist = Artist.query.filter_by(first_name=form.first_name.data, last_name=form.last_name.data).first()
        except:
            flash("Something is wrong with the database, contact your admin", "error")
            return redirect(url_for('secure.library'))
        if not artist:
            new_artist = Artist(first_name=form.first_name.data, last_name=form.last_name.data, display_pic=form.display_pic.data, rating=form.rating.data)
            db.session.add(new_artist)
            try:
                db.session.commit()
                flash(f"{new_artist} added", "success")
                return redirect(url_for("secure.library"))
            except:
                flash("Something is wrong with the database, contact your admin", "error")
                return redirect(url_for("secure.library"))
        else:
            flash("Artist already exists", "error")
            return redirect(url_for('secure.library'))


    elif request.method == "DELETE":
        body = request.get_json(force=True)
        try:
            selected = Artist.query.filter_by(id=body["id"]).one()
        except:
            flash("Thats odd...", "error")
            return redirect(url_for("secure.library"))
        if selected:
            db.session.delete(selected)
            try:
                db.session.commit()
                flash(f"{selected.id} deleted", "success")
                return redirect(url_for("secure.library")) # cant redirect to same page?
            except:
                flash("Something is wrong with the database, contact your admin", "error")
                return redirect(url_for("secure.library"))
        else:
            flash("Thats odd...", "error")
            return redirect(url_for("secure.library"))

    else:
        flash(form.errors, "error")
        return redirect(url_for("secure.library"))