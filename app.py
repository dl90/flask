from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/chris')
def index():
    return app.send_static_file('index.html')

# passing args to rendering templates
@app.route('/<arg>')
def indexWithArg(arg):
    return render_template("home.html", arg = arg)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"

if __name__ == "__main__":
    app.run(port=9999, debug=True)