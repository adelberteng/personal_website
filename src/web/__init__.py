from flask import Flask
from flask import g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

from web.route import index 
from web.route import about
from web.route import this_website
from web.route import not_implement
from web.route import blog
from web.route import linebot_addfd
from web.route import page_not_found
from web import auth
from web import shop
from web import linebot

from .config import AppConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    csrf.init_app(app)
    csrf.exempt("web.linebot.callback") # csrf will block Line callback

    app.add_url_rule("/", endpoint="index", view_func=index)
    app.add_url_rule("/about", "about", about)
    app.add_url_rule("/this_website", "this_website", this_website)
    app.add_url_rule("/not_implement", "not_implement", not_implement)
    # app.add_url_rule("/blog", "blog", blog)
    app.add_url_rule("/linebot_addfd", "linebot_addfd", linebot_addfd)
    app.register_error_handler(404, page_not_found)

    app.register_blueprint(auth.bp)
    app.register_blueprint(shop.bp)
    app.register_blueprint(linebot.bp)


    return app