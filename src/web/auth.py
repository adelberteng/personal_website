import functools

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import g
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .forms import LoginForm
from .forms import RegisterForm

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


def login():
    form = LoginForm(csrf_enabled=False)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        return redirect(url_for("index"))

    else:
        return render_template("login.html", form = form)
    
def register():
    form = RegisterForm(csrf_enabled=False)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        password_repeat = request.form.get("password_repeat")
        if password_repeat != password:
            not_match_warning = "Two of your passwords does not match, Please retry again."
            return render_template("register.html", not_match_warning = not_match_warning)
        # todo: save user info to db

        return redirect(url_for("login"))
    else:
        return render_template("register.html")
        


def change_password():
    pass
