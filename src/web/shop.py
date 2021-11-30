from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
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
        
        same_item = Cart.query.filter_by(uid=g.uid, product_id=product_id).first()
        if not same_item:
            new_item = Cart(uid=g.uid, product_id=product_id, quantity=quantity)
            db.session.add(new_item)
            db.session.commit()
        else:
            same_item.quantity = quantity
            db.session.commit()

        return redirect(url_for("shop.cart"))

    cart_items = Cart.query.filter_by(uid=g.uid).all()
    total_amount = 0
    for item in cart_items:
        item_total_price = item.product.price * item.quantity
        total_amount += item_total_price
    
    return render_template(
        "shop/cart.html", 
        cart_items=cart_items, 
        total_amount=total_amount
    )

@bp.route("/order_check", methods=("GET", "POST"))
@login_required
def order_check():
    if request.method == "POST":
        product_confirm_list = request.form.getlist("buy_check")
        cart_items = Cart.query.filter_by(uid=g.uid).\
            filter(Cart.product_id.in_(product_confirm_list)).all()

        total_amount = 0
        for item in cart_items:
            item_total_price = item.product.price * item.quantity
            total_amount += item_total_price

        return render_template(
            "shop/order_check.html", 
            cart_items=cart_items, 
            total_amount=total_amount
        )

    url = request.referrer
    return render_template(
            "shop/order_check.html", 
            data = url
        )


    


@bp.route("/order", methods=("GET", "POST"))
@login_required
def order():
    pass