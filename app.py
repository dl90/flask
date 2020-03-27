from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return "test"

# passing args to rendering templates
@app.route('/<page>')
def pageRoute(page):
    return render_template( f'{page}.html', page='home' )

@app.route('/library')
def library():
    return render_template( f'home.html', page='library' )

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"

if __name__ == "__main__":
    app.run(port=7000, debug=True)
