from flask import Blueprint
from flask import render_template
from flask import request

from web.auth import login_required
from web import db
from .models import Product

bp = Blueprint("shop", __name__, url_prefix="/shop")


@bp.route("/shop", methods=("GET", "POST"))
@login_required
def shop():
	return render_template("shop/shop.html")


@bp.route("/product", methods=("GET", "POST"))
@login_required
def product():
	product_id = request.args.get('product_id')
	product = Product.query.filter_by(product_id=product_id).first()
	product_name = product.product_name
	product_img_path = product.product_img_path
	product_detail = product.product_detail
	price = product.price

	return render_template("shop/product.html", var = product_id)

@bp.route("/cart", methods=("GET", "POST"))
@login_required
def cart():
	pass

@bp.route("/order", methods=("GET", "POST"))
@login_required
def order():
	pass