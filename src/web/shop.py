from flask import Blueprint

from web.auth import login_required

bp = Blueprint("shop", __name__, url_prefix="/shop")


@bp.route("/shop", methods=("GET", "POST"))
def shop():
	return render_template("shop/shop.html")


@bp.route("/merchandise", methods=("GET", "POST"))
def merchandise():
	pass

@bp.route("/cart", methods=("GET", "POST"))
def cart():
	pass

@bp.route("/order", methods=("GET", "POST"))
def order():
	pass