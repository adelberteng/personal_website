from flask import Flask

from web.route import index 
from web.route import login
from web.route import register
from web.route import blog
from web.route import linebot_addfd

methods = ["GET", "POST"]


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/", endpoint="index", view_func=index)
    app.add_url_rule("/login", "login", login, methods=methods)
    app.add_url_rule("/register", "register", register, methods=methods)
    app.add_url_rule("/blog", "blog", blog)
    app.add_url_rule("/linebot_addfd", "linebot_addfd", linebot_addfd)

    return app