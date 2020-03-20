from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Text)
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profileInfo = db.Column(db.PickleType)
    recommendations = db.Column(db.PickleType)
    likes = db.Column(db.PickleType)
    playHistory = db.Column(db.PickleType)
    isPremium = db.Column(db.Boolean)

    def __init__(self, username, password, profileInfo=None, recommendations=None, likes=None, playHistory=None, isPremium=False) :
        self.username = username
        self.password = password
        self.profileInfo = profileInfo
        self.recommendations = recommendations
        self.likes = likes
        self.playHistory = playHistory
        self.isPremium = isPremium

    def __repr__(self):
        return '<User: %r, Password: %r>' % (self.username, self.password)

    def __hash__(self):
        return hash(self.username)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
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


from db import db
db.create_all()
