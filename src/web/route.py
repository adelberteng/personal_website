from flask import render_template, request, jsonify, redirect

def index():
	return render_template("index.html")

def login():
	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")
		print(username)

	elif request.method == 'GET':
		return render_template("login.html")
	
def register():
	pass

def change_password():
	pass

def blog():
	return render_template("blog.html")

def linebot_addfd():
	return render_template("linebot_addfd.html")