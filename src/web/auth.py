import functools

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import g
from flask import flash
from sqlalchemy.engine import url
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
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

# @bp.before_app_request
# def load_logged_in_user():
#     """If a user id is stored in the session, load the user object from
#     the database into ``g.user``."""
#     user_id = session.get("user_id")

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = (
#             get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
#         )

@bp.route("/login", methods=("GET", "POST"))
def login():
    # csrf_enabled=False
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        # db = g.db
        # password_hash = db.execute(
        #     f"SELECT password_hash FROM user WHERE username = '{username}'")

        # if not check_password_hash(password_hash, password):
        #     login_warning = "the password is incorrect, please try again."
        #     return redirect(url_for("login"), login_warning = login_warning)

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
            not_match_warning = (
                "Two of your passwords does not match, "
                "Please retry again."
            )
            return render_template(
                "auth/register.html", 
                form = form, 
                not_match_warning = not_match_warning
            )

        # todo: save user into to db

        return redirect(url_for("auth.login"))
    else:
        return render_template("auth/register.html", form = form)
        


def change_password():
    pass

@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("index"))
