from flask import Flask, Blueprint, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_server(config_filename):

    app = Flask(__name__)
    app.config.from_object(config_filename)


    from server.db.schema import User, Profile, Playlist, Artist, Album, Song
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    @app.route("/")
    def initialize():
        return render_template("auth/index.html", title="🚀")

    @app.route("/reset")
    def reset():
        try:
            db.drop_all()
            flash("Database clearned...", "info")
        finally:
            db.create_all()
            flash("Database recreated...", "info")
            return render_template("auth/index.html", title="💥")

    from .blueprints.auth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from .blueprints.secure import secure
    app.register_blueprint(secure, url_prefix="/secure")

    from .blueprints.local_api import local
    app.register_blueprint(local, url_prefix="/local")

    return app
