from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..util.forms import SearchForm
from ..create_server import db

import billboard
secure = Blueprint('secure', __name__)
chart = billboard.charts()

@secure.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "GET":
        if current_user.is_authenticated:
            search_form = SearchForm()
            hot_100 = billboard.ChartData('hot-100', date=None, fetch=True, timeout=25)
            return render_template('console/home.html', name=current_user.username, chart=chart, selection=hot_100, route=url_for("local_api.search"), search_form=search_form)
        else:
            return redirect(url_for("initialize"))


@secure.route('/library', methods=["GET"])
@login_required
def library():
    return render_template('console/home.html', name=current_user.username)