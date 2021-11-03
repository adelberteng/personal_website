from flask import current_app
from flask import g
from sqlalchemy import create_engine

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

