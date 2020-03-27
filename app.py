from flask import Flask, render_template, request
app = Flask(__name__,
            static_url_path='', 
            static_folder='public',
            template_folder='templates')

# @app.route('/chris')
# def index():
#     return app.send_static_file('index.html')

# passing args to rendering templates
# @app.route('/<arg>')
# def indexWithArg(arg):
#     return render_template("home.html", arg = arg)


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
    alt = "man", 
    profileImage = "/css/images/profile_image.jpg",
    artistName = "Chris",
    # albumsList = {{'art': "/css/images/albumImage.jpg", 'title': 'title1'}, {'art': "/css/images/albumImage.jpg", 'title': 'title2'}})
    albumArt = "/css/images/albumImage.jpg",
    title = "albumTitle"
    )

@app.route("/albums")
def albums():
    return render_template("albums.html")

@app.route("/playlists")
def playlists():
    return render_template("playlists.html")


# Listener
if __name__ == "__main__":
    app.run(port=9999, debug=True)