from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for

from .forms import LoginForm

def index():
	return render_template("index.html")

def login():
	form = LoginForm(csrf_enabled=False)
	if request.method == 'POST':
		username = form.username.data
		password = form.password.data

		return redirect(url_for("index"))

	elif request.method == 'GET':
		return render_template("login.html", form = form)
	
def register():
	if request.method == 'GET':
		return render_template("register.html")
	else:
		username = form.username.data
		password = form.password.data
		password_repeat = request.form.get("password_repeat")
		if password_repeat != password:
			not_match_warning = "Two of your passwords does not match, Please retry again."
			return render_template("register.html", not_match_warning = not_match_warning)
		# todo: save user info to db

		return redirect(url_for("login"))


def change_password():
	pass

def blog():
	return render_template("blog.html")

def linebot_addfd():
	return render_template("linebot_addfd.html")


def not_implement():
	return render_template("not_implement.html")