from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=-1, message="Password must be 8 characters long.")])

class NewUserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password_1 = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=-1, message="Password must be 8 characters long.")])
    password_2 = PasswordField("Password", validators=[InputRequired(), EqualTo("password_1", message="Passwords do not match")])