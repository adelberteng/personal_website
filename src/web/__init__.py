from flask import Flask
# from flask_wtf.csrf import CSRFProtect
# csrf = CSRFProtect()

from web.route import index 
from web.route import login
from web.route import register
from web.route import not_implement
from web.route import blog
from web.route import linebot_addfd
from web import linebot

methods = ["GET", "POST"]


def create_app():
    app = Flask(__name__)
    # csrf.init_app(app)
    app.add_url_rule("/", endpoint="index", view_func=index)
    app.add_url_rule("/login", "login", login, methods=methods)
    app.add_url_rule("/register", "register", register, methods=methods)
    app.add_url_rule("/not_implement", "not_implement", not_implement)
    app.add_url_rule("/blog", "blog", blog)
    app.add_url_rule("/linebot_addfd", "linebot_addfd", linebot_addfd)

    app.register_blueprint(linebot.bp)

    return app