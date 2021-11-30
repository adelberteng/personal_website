from datetime import datetime
import json

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
from .models import Order
from .models import OrderDetail

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
    amount = 0
    for item in cart_items:
        item_total_price = item.product.price * item.quantity
        amount += item_total_price
    
    return render_template(
        "shop/cart.html", 
        cart_items=cart_items, 
        amount=amount
    )

@bp.route("/order_check", methods=("GET", "POST"))
@login_required
def order_check():
    """last check before user submit their order,
    the order check page will display the items are picked by user
    from previous page.

    Direct to this page is not allow, only method POST can reach out.
    It will redirect to shop page if the method is GET.
    """
    if request.method == "POST":
        product_confirm_list = request.form.getlist("buy_check")
        cart_items = Cart.query.filter_by(uid=g.uid).\
            filter(Cart.product_id.in_(product_confirm_list)).all()

        amount = 0
        for item in cart_items:
            item_total_price = item.product.price * item.quantity
            amount += item_total_price

        return render_template(
            "shop/order_check.html", 
            cart_items=cart_items, 
            amount=amount
        )

    return redirect(url_for("shop.shop"))


@bp.route("/order", methods=("GET", "POST"))
@login_required
def order():
    if request.method == "POST":
        now = datetime.now()
        new_order = Order(uid=g.uid, created_time=now)
        db.session.add(new_order)
        db.session.commit()

        product_confirm_list = request.form.getlist("buy_check")
        if not product_confirm_list:
            return redirect(url_for("shop.order"))

        cart_items = Cart.query.filter_by(uid=g.uid).\
            filter(Cart.product_id.in_(product_confirm_list)).all()

        for item in cart_items:
            new_order_item = OrderDetail(
                product_id=item.product.product_id, 
                quantity=item.quantity, 
                order_id=new_order.order_id
            )
            db.session.add(new_order_item)

        Cart.query.filter_by(uid=g.uid).\
            filter(Cart.product_id.in_(product_confirm_list)).delete()

        db.session.commit()

        return redirect(url_for("shop.order"))
    
    # view order list
    orders = Order.query.filter_by(uid=g.uid).all()
    order_id_list = [i.order_id for i in orders]
    order_items_list = OrderDetail.query.filter(
        OrderDetail.order_id.in_(order_id_list)).all()

    item_content_dict = dict()
    order_amount_dict = dict()
    for id in order_id_list:
        item_content_dict[id] = list(
            filter(lambda x: x.order_id == id, order_items_list))
        order_amount_dict[id] = sum(
            [i.product.price*i.quantity for i in item_content_dict[id]])

    return render_template(
        "shop/order.html", 
        orders=orders, 
        item_content_dict=item_content_dict,
        order_amount_dict=order_amount_dict
    )
