from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Text)
from datetime import date

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
# https://pypi.org/project/Flask-SQLAlchemy/
# https://pypi.org/project/Flask-Migrate/
# https://flask-migrate.readthedocs.io/en/latest/

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# from db import db
# db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    profileInfo = db.Column(db.PickleType)
    recommendations = db.Column(db.PickleType)
    likes = db.Column(db.PickleType)
    playHistory = db.Column(db.PickleType)
    isPremium = db.Column(db.Boolean)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    sex = db.Column(db.String(255))
    profilePicture = db.Column(db.String(255))
    tiktok = db.Column(db.String(255))

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    songs = db.Column(db.PickleType)
    date = db.Column(db.DateTime, default=date.today())
    genreOfSongs = db.Column(db.String(255))

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    albumList = db.Column(db.PickleType)
    albumArt = db.Column(db.String(255))

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.PickleType)
    art = db.Column(db.String(255))
    songList = db.Column(db.PickleType)
    releaseDate = db.Column(db.DateTime, default=date.today())

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.PickleType)
    realeaseDate = db.Column(db.DateTime, default=date.today())
    coverArt = db.Column(db.String(255))
    lyrics = db.Column(db.Text)


db.session.add(User(username="Flask", profileInfo="example@example.com"))
db.session.commit()

users = User.query.all()
