import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext
from sqlalchemy import create_engine



def get_db():
    if "db" not in g:
        g.db = create_engine(
            current_app.config.get("SQLALCHEMY_DATABASE_URI"))

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with open("schema.sql", 'r', encoding='utf-8') as f:
        sql_text = f

    db.execute(sql_text)



@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


# def init_app(app):
#     """Register database functions with the Flask app. This is called by
#     the application factory.
#     """
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)