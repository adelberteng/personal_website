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



# class Merchandise(db.Model):
#     __tablename__ = 'merchandise_tbl'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(32), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)

#     def __repr__(self):
#         return f"id: {self.id} username: {self.username} password_hash: {self.password_hash}"







# from flask import current_app
# from flask import g
# from sqlalchemy import create_engine

# def get_db():
#     if "db" not in g:
#         g.db = create_engine(
#             current_app.config.get("SQLALCHEMY_DATABASE_URI")
#         )

#     return g.db



