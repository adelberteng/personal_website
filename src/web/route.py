from flask import render_template, request, jsonify, redirect, url_for

def index():
	return render_template("index.html")

def login():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")


	elif request.method == 'GET':
		return render_template("login.html")
	
def register():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")
		password_repeat = request.form.get("password_repeat")
		if password_repeat != password:
			return render_template("register.html", not_match_warning = "Two of your passwords does not match, Please retry again.")

	elif request.method == 'GET':
		return render_template("register.html")

def change_password():
	pass

def blog():
	return render_template("blog.html")

def linebot_addfd():
	return render_template("linebot_addfd.html")