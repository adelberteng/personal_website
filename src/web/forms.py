from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Login")


class RegisterForm(FlaskForm):
	username = StringField(
		"Username", validators=[DataRequired(), Length(max=30)])
	password = PasswordField("Password", validators=[DataRequired()])
	password_repeat = PasswordField(
		"Password Repeat", validators=[DataRequired()])
	submit = SubmitField("Sign Up")
	