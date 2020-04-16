from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..util.forms import SearchForm
from ..create_server import db
import billboard

# /secure...
secure = Blueprint('secure', __name__)
chart = billboard.charts()

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
    return render_template('console/home.html', name=current_user.username, title="🖥", api=url_for(".rankings"), chart=chart, selectionTitle=selection_title ,selection=selection, route=url_for("local_api.search"), search_form=search_form)



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
    return render_template('console/home.html', name=current_user.username, title="🖥", api=url_for(".rankings"), chart=chart, selectionTitle=query, selection=selection, route=url_for("local_api.search"), search_form=search_form)



@secure.route('/library', methods=["GET"])
@login_required
def library():
    search_form = SearchForm()
    return render_template('console/library.html', name=current_user.username, title="📚", route=url_for("local_api.search"), search_form=search_form)