from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, Length, EqualTo, URL, NumberRange


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=-1, message="Password must be 8 characters long.")])

class NewUserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password_1 = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=-1, message="Password must be 8 characters long.")])
    password_2 = PasswordField("Password", validators=[InputRequired(), EqualTo("password_1", message="Passwords do not match")])

class SearchForm(FlaskForm):
    query = StringField("Search", validators=[InputRequired(), Length(min=2, max=30, message="Must be greater than 2 character long.")])

class AddArtistForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(), Length(min=1, max=-1, message="Must be greater than 1 character long.")])
    last_name = StringField("Last Name", validators=[InputRequired(), Length(min=1, max=-1, message="Must be greater than 1 character long.")])
    rating = SelectField(u"Rating", choices=[(1, "⭐️"), (2, "⭐️⭐️"), (3, "⭐️⭐️⭐️"), (4, "⭐️⭐️⭐️⭐️"), (5, "⭐️⭐️⭐️⭐️⭐️")], coerce=int, default=3)
    display_pic = StringField("Display Picture (URL)", validators=[URL(require_tld=False, message="Valid URL required.")])