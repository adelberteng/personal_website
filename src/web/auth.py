import functools

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import g
from flask import flash
from flask import session
from flask import make_response
import sqlalchemy
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .forms import LoginForm
from .forms import RegisterForm
from .db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Not logged in, please log in to continue")
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into g.user."""
    username = session.get("username")

    if username is None:
        g.user = None
    else:
        g.user = (
            get_db().execute(
                f"SELECT username FROM user WHERE username = '{username}'"
            ).fetchone()[0]
        )

@bp.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        db = get_db()

        password_hash = db.execute(
            f"SELECT password_hash FROM user WHERE username = '{username}'"
        ).fetchone()

        if not password_hash:
            flash("the username is not exist, please check again.")
            return redirect(url_for("auth.login"))
        elif not check_password_hash(password_hash[0], password):
            flash("the password is incorrect, please try again.")
            return redirect(url_for("auth.login"))

        session['username'] = username
        session.permanent = True
        g.user = username

        flash("Login success! Knock youself out!")
        return redirect(url_for("index"))
    else:
        return render_template("auth/login.html", form = form)
    
@bp.route("/register", methods=("GET", "POST"))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        password_repeat = form.password_repeat.data
        if password_repeat != password:
            flash(
                "Two of your passwords does not match, "
                "Please retry again."
            )
            return render_template("auth/register.html", form = form)

        db = get_db()
        try:
            password_hash = generate_password_hash(password)
            db.execute(
                "INSERT INTO user (username, password_hash)"
                f"VALUES ('{username}', '{password_hash}')"
            )
        except sqlalchemy.exc.IntegrityError:
            flash(f"User {username} is already registered.")
            return render_template("auth/register.html", form = form)
        except Exception as e:
            print(e)

        flash("Signup success! Please login with your account.")
        return redirect(url_for("auth.login"))
    else:
        return render_template("auth/register.html", form = form)
        


def change_password():
    pass

@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash("logout success!")
    g.user = None
    res = make_response(redirect(url_for("index")))
    return res
