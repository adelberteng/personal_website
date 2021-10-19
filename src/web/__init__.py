from flask import Flask

from web.route import index


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/", endpoint="index", view_func=index)

    return app