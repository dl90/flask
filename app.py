from flask import Flask, render_template, request, escape
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello world</h1>"

# passing args to rendering templates
@app.route('/<arg>')
def indexWithArg(arg):
    return render_template("home.html", arg=arg)


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"


if __name__ == "__main__":
    app.run(port=8888, debug=True)
