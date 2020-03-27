from flask import Flask, render_template, request
app = Flask(__name__,
            static_url_path='', 
            static_folder='public',
            template_folder='templates')

# @app.route('/chris')
# def index():
#     return app.send_static_file('index.html')

# passing args to rendering templates
@app.route('/<page>')
def pageRoute(page):
    return render_template( f'{page}.html', user='bob' )

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"


@app.route("/artists")
def artists():
    return render_template("artists.html", 
    appName = " Music", 
    alt = "name", 
    profileImage = "/css/images/profile_image.jpg",
    artistName = "ArtistName",
    # albumsList = {{'art': "/css/images/albumImage.jpg", 'title': 'title1'}, {'art': "/css/images/albumImage.jpg", 'title': 'title2'}})
    albumArt = "/css/images/albumImage.jpg",
    title = "albumTitle",
    album_page = "albums",
    playlist_page = "playlists",
    playlistArt = "/css/images/playlistArt.jpeg",
    playlistTitle = "Playlist Title"

    )

@app.route("/albums")
def albums():
    return render_template("albums.html",
    appName = " Music",
    artistName = "ArtistName",
    albumArt = "/css/images/albumImage.jpg",
    title = "albumTitle",
    albumName = "Album Name",
    artist_page = "artists",
    songName = "Amazing Song"
    )

@app.route("/playlists")
def playlists():
    return render_template("playlists.html",
    appName = " Music", 
    profileImage = "/css/images/profile_image.jpg",
    artistName = "ArtistName",
    albumArt = "/css/images/albumImage.jpg",
    title = "albumTitle",
    album_page = "albums",
    playlist_page = "playlists",
    playlistArt = "/css/images/playlistArt.jpeg",
    playlistTitle = "Playlist Title",
    songName = "Amazing Song",
    playlistName = "playlistName"
    )


# Listener
if __name__ == "__main__":
    app.run(port=9999, debug=True)
