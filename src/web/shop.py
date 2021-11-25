from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for
from flask import g

from web.auth import login_required
from web import db
from .models import Product
from .models import Cart

bp = Blueprint("shop", __name__, url_prefix="/shop")


@bp.route("/shop", methods=("GET", "POST"))
@login_required
def shop():
    return render_template("shop/shop.html")


@bp.route("/product", methods=("GET", "POST"))
@login_required
def product():
    product_id = request.form.get('product_id')
    product = Product.query.filter_by(product_id=product_id).first()

    return render_template("shop/product.html", product=product)

@bp.route("/cart", methods=("GET", "POST"))
@login_required
def cart():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        quantity = request.form.get("quantity")
        
        new_item = Cart(uid=g.uid, product_id=product_id, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()

        # cart_items = Cart.query.filter_by(uid=g.uid).all()
        # cart_items = Cart.query.join(Cart, Cart.product_id == Product.product_id).filter(Cart.uid == g.uid).all()

        return render_template("shop/cart.html", cart_items=quantity)
    
    return render_template("shop/cart.html")

@bp.route("/order", methods=("GET", "POST"))
@login_required
def order():
    pass