from flask import current_app
from flask import g
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy import text

def get_db():
    if "db" not in g:
        g.db = create_engine(
            current_app.config.get("SQLALCHEMY_DATABASE_URI")
        )

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        sql_text = f.read().decode('utf-8').replace("\n","")
        db.execute(sql_text)
