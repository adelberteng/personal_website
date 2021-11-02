# route.py deals with regular page.
from flask import render_template


def index():
	return render_template("index.html")

def about():
	return render_template("about.html")

def this_website():
	return render_template("this_website.html")

def blog():
	return render_template("blog.html")

def linebot_addfd():
	return render_template("linebot_addfd.html")

def not_implement():
	return render_template("not_implement.html")