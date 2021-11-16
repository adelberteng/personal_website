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

from web import db
from .forms import LoginForm
from .forms import RegisterForm
from .models import User


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
        user = User.query.filter_by(username=username).first()
        g.user = (
            user.username
        )

@bp.route("/login", methods=("GET", "POST"))
def login():
    """User login and keep login status by session."""
    form = LoginForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if not user:
            flash("the username is not exist, please check again.")
            return redirect(url_for("auth.login"))
        elif not user.check_password(password):
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
    """User register and redirect to login page after signup."""
    form = RegisterForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        password_repeat = form.password_repeat.data
        email = form.email.data

        if password_repeat != password:
            flash(
                "Two of your passwords does not match, "
                "Please retry again."
            )
            return render_template("auth/register.html", form = form)
        elif User.query.filter_by(username=username).first():
            flash(f"User {username} is already registered.")
            return render_template("auth/register.html", form = form)
        elif User.query.filter_by(email=email).first():
            flash(f"Email address: {email} is already registered.")
            return render_template("auth/register.html", form = form)

        new_user = User(username=username, email=email)
        new_user.set_password(password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Signup success! Please login with your account.")
        return redirect(url_for("auth.login"))
    else:
        return render_template("auth/register.html", form = form)
        

@bp.route("/change_password")
def change_password():
    """User change password by entry their old password."""
    pass

@bp.route("/reset_password")
def reset_password():
    """If user forget their password, user could reset password by 
    entry their email for verification."""
    pass


@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash("logout success!")
    g.user = None
    res = make_response(redirect(url_for("index")))
    return res
