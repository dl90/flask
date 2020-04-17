from sqlalchemy import Text
from sqlalchemy.orm import relationship
from datetime import date
from flask_login import UserMixin
from ..create_server import db


class User(UserMixin, db.Model):
    __tablename__ = 'User'

    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(255), unique=True, nullable=False)
    password        = db.Column(db.String(255), nullable=False)
    creation_date   = db.Column(db.DateTime, default=date.today())
    recommendations = db.Column(db.PickleType)
    likes           = db.Column(db.PickleType)
    play_history    = db.Column(db.PickleType)
    is_premium      = db.Column(db.Boolean)
    profile         = relationship("Profile", uselist=False, back_populates="user")

    def __init__(self, username, password, creation_date=None, recommendations=None, likes=None, play_history=None, is_premium=False, profile=None) :
        self.username        = username
        self.password        = password
        self.creation_date   = creation_date
        self.recommendations = recommendations
        self.likes           = likes
        self.play_history    = play_history
        self.is_premium      = is_premium
        self.profile         = profile

    def __repr__(self):
        return '<ID: %r  User: %r  isPremium: %r>\n' % (self.id, self.username, self.is_premium)


class Profile(db.Model):
    __tablename__ = 'Profile'

    id              = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    first_name      = db.Column(db.String(255), nullable=False)
    last_name       = db.Column(db.String(255))
    email           = db.Column(db.String(255), unique=True, nullable=False)
    sex             = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255))
    user            = relationship("User", back_populates="profile")

    def __init__(self, user_id, email, user, first_name, last_name=None, sex=None, profile_picture=None):
        self.user_id         = user_id
        self.first_name      = first_name
        self.last_name       = last_name
        self.email           = email
        self.sex             = sex
        self.profile_picture = profile_picture
        self.user            = user

    def __repr__(self):
        return '<First Name: %r  Email: %r  User: %r>\n' % (self.first_name, self.email, self.user)


class Playlist(db.Model):
    __tablename__ = 'Playlist'

    id             = db.Column(db.Integer, primary_key=True)
    user_id        = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    name           = db.Column(db.String(255), unique=True, nullable=False)
    songs          = db.Column(db.PickleType)
    date           = db.Column(db.DateTime, default=date.today())
    genre_of_songs = db.Column(db.String(255))
    user           = db.relationship('User', backref=db.backref('playlists', lazy=True))
    rating         = db.Column(db.Integer)

    def __init__(self, user_id, name, songs=None, genre_of_songs=None, rating=None):
        self.user_id        = user_id
        self.name           = name
        self.songs          = songs
        self.genre_of_songs = genre_of_songs
        self.rating         = rating
        self.date           = date.today()

    def __repr__(self):
        return '<Playlist Name: %r  User: %r  Songs: %r>\n' % (self.name, self.user, self.songs)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id            = db.Column(db.Integer, primary_key=True)
    first_name    = db.Column(db.String(255), nullable=False)
    last_name     = db.Column(db.String(255), nullable=False)
    album_list    = db.Column(db.PickleType)
    display_pic   = db.Column(db.String(255))
    rating        = db.Column(db.Integer, default=3)
    creation_date = db.Column(db.DateTime, default=date.today())

    def __init__(self, first_name, last_name, album_list=None, display_pic=None, rating=None):
        self.first_name    = first_name
        self.last_name     = last_name
        self.album_list    = album_list
        self.display_pic   = display_pic
        self.rating        = rating
        self.creation_date = date.today()

    def __repr__(self):
        return '<ID: %r  First Name: %r  Last Name: %r>\n' % (self.id, self.first_name, self.last_name)


class Album(db.Model):
    __tablename__ = 'Album'

    id             = db.Column(db.Integer, primary_key=True)
    title          = db.Column(db.String(255), nullable=False)
    artists        = db.Column(db.PickleType) # list of artist/primary_artist
    art            = db.Column(db.String(255))
    song_list      = db.Column(db.PickleType, nullable=False)
    release_date   = db.Column(db.DateTime, nullable=False, default=date.today())
    artist_id      = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    primary_artist = db.relationship('Artist', backref=db.backref('albums', lazy=True))
    rating         = db.Column(db.Integer)

    def __init__(self, title, primary_artist, song_list, artists=None, art=None, rating=None, release_date=date.today()):
        self.title          = title
        self.primary_artist = primary_artist
        self.artists        = artists
        self.art            = art
        self.song_list      = song_list
        self.rating         = rating
        self.release_date   = release_date

    def __repr__(self):
        return '<ID: %r  Primary Artist: %r  Song List: %r>\n' %(self.id, self.primary_artist, self.song_list)


class Song(db.Model):
    __tablename__ = "Song"

    id             = db.Column(db.Integer, primary_key=True)
    title          = db.Column(db.String(255), nullable=False)
    artists        = db.Column(db.PickleType)
    realease_date  = db.Column(db.DateTime, default=date.today(), nullable=False)
    cover_art      = db.Column(db.String(255))
    lyrics         = db.Column(db.Text, nullable=False)
    rating         = db.Column(db.Integer)
    artist_id      = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    album_id       = db.Column(db.Integer, db.ForeignKey('Album.id'), nullable=False)
    primary_artist = db.relationship('Artist', backref=db.backref('songs', lazy=True))
    primary_album  = db.relationship('Album', backref=db.backref('songs', lazy=True))

    def __init__(self, title, primary_artist, primary_album, lyrics, artists=None, cover_art=None, rating=None, release_date=date.today()):
        self.title          = title
        self.artists        = artists
        self.realease_date  = release_date
        self.cover_art      = cover_art
        self.lyrics         = lyrics
        self.rating         = rating
        self.primary_artist = primary_artist
        self.primary_album  = primary_album

    def __repr__(self):
        return '<ID: %r  Title: %r  Primary Artist: %r  Primary Album: %r  Rating: %r>\n' % (self.id, self.title, self.primary_artist, self.primary_album, self.rating)
