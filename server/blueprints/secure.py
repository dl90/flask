from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..util.forms import SearchForm, AddArtistForm
from ..create_server import db
from ..db.schema import Artist
import billboard

# /secure...
secure = Blueprint('secure', __name__)
try:
    chart = billboard.charts()
except Exception:
    print(Exception)


@secure.route("/home", methods=["GET"])
@login_required
def home():
    search_form = SearchForm()
    selection_title = 'hot-100'
    try:
        selection = billboard.ChartData(selection_title, date=None, fetch=True, timeout=25)
    except Exception:
        flash("Problem loading chart data.", "error")
        return redirect(url_for("initialize"))
    return render_template('console/home.html', name=current_user.username, title="🖥", api=url_for(".rankings"), chart=chart,
    selectionTitle=selection_title ,selection=selection, searchRoute=url_for("local_api.search"), search_form=search_form)



@secure.route('/chart', methods=["GET"])
@login_required
def rankings():
    search_form = SearchForm()
    query = request.args.get("chart")
    try:
        selection = billboard.ChartData(query, date=None, fetch=True, timeout=25)
    except Exception:
        flash("Problem loading chart data.", "error")
        return redirect(url_for("initialize"))
    return render_template('console/home.html', name=current_user.username, title="🖥", api=url_for(".rankings"), chart=chart,
    selectionTitle=query, selection=selection, searchRoute=url_for("local_api.search"), search_form=search_form)



@secure.route('/library', methods=["GET", "DELETE"])
@login_required
def library():
    search_form = SearchForm()
    add_artist_form = AddArtistForm()
    artists = Artist.query.all()

    return render_template('console/library.html', name=current_user.username, title="📚", searchRoute=url_for("local_api.search"), search_form=search_form,
    artists=artists, add_artist_form=add_artist_form, addArtistRoute=url_for("local_api.artist"), deleteArtistRoute=url_for('local_api.artist'))
