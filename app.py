from flask import Flask, render_template, request, escape
app = Flask(__name__,
            static_url_path='',
            static_folder='public',
            template_folder='templates')

# do not format
from db.schema import (User, Profile, Playlist, Artist, Album, Song)


# @app.route('/')
# def home():
#     return "<h1>Hello world</h1>"


# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == 'POST':
#         return "do_the_login"
#     else:
#         return "show_the_login_form"


# passing args to rendering templates
@app.route('/<page>')
def pageRoute(page):
    return render_template(f'{page}.html', page='home')


@app.route('/library')
def library():
    return render_template(f'home.html', page='library')


@app.route("/artists")
def artists():
    artistName = 'snoop'  # hardcoded, passed param from
    artists = Artist.query.all()
    artist = Artist.query.filter_by(first_name=artistName).first()

    return render_template("artists.html",
                           appName=" Music",
                           alt="artist image",
                           profileImage="/css/images/profile_image.jpg",


                           artistName="ArtistName",
                           # albumsList = {{'art': "/css/images/albumImage.jpg", 'title': 'title1'}, {'art': "/css/images/albumImage.jpg", 'title': 'title2'}})
                           albumArt="/css/images/albumImage.jpg",
                           title="albumTitle",
                           album_page="albums",
                           playlist_page="playlists",
                           playlistArt="/css/images/playlistArt.jpeg",
                           playlistTitle="Playlist Title",
                           artists=artists
                           )


@app.route("/albums")
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
