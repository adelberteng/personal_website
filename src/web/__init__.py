import os

from flask import Flask
from flask import send_from_directory
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from web.route import index 
from web.route import about
from web.route import this_website
from web.route import not_implement
from web.route import blog
from web.route import linebot_addfd
from web import auth
from web import linebot

from .config import Config
conf = Config.load(env="dev")

database = conf.get("MYSQL_DATABASE")
mysql_user = conf.get("MYSQL_USER")
mysql_password = conf.get("MYSQL_PASSWORD")
mysql_endpoint = "localhost"
mysql_port = 3306
secret_key = conf.get("secret_key")

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{mysql_user}:{mysql_password}@"
        f"{mysql_endpoint}:{mysql_port}/{database}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/robots.txt')
    def static_from_root():
        return send_from_directory("/robots.txt")

    app.add_url_rule("/", endpoint="index", view_func=index)
    app.add_url_rule("/about", "about", about)
    app.add_url_rule("/this_website", "this_website", this_website)
    app.add_url_rule("/not_implement", "not_implement", not_implement)
    app.add_url_rule("/blog", "blog", blog)
    app.add_url_rule("/linebot_addfd", "linebot_addfd", linebot_addfd)

    app.register_blueprint(auth.bp)
    app.register_blueprint(linebot.bp)

    return app

    