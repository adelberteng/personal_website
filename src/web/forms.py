from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")


class RegisterForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	password_repeat = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Sign Up")
	