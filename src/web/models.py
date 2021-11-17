from flask import g
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from web import db

class User(db.Model):
    __tablename__ = 'user_tbl'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        return (
            f"uid: {self.uid} username: {self.username} "
            f"password_hash: {self.password_hash}"
            f"email: {self.email}"
        )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



# class Product(db.Model):
#     __tablename__ = 'product_tbl'
#     product_id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(32), unique=True, nullable=False)
#     product_detail = db.Column(db.String)
#     price =  db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return (
#             f"product_id: {self.product_id} product_name: {self.product_name}"
#             f"product_detail: {self.product_detail} "
#             f"price: {self.price}"
#         )


# class Cart(db.Model):
#     __tablename__ = 'cart_tbl'
#     cart_item_id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer,  nullable=False, index=True)
#     product_id = db.Column(db.Integer, nullable=False)
#     quantity = db.Column(db.Integer,  nullable=False)
#     status = db.Column(db.BOOLEAN) # True is added in order.



# class Order(db.Model):
#     __tablename__ = 'order_tbl'
#     order_id = db.Column(db.Integer, primary_key=True)
#     uid = db.Column(db.Integer,  nullable=False, index=True)
#     created_time = db.Column(db.Integer,  nullable=False) # timestamp

# class OrderDetail(db.Model):
#     __tablename__ = 'order_detail_tbl'
#     order_item_id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer,  nullable=False)

