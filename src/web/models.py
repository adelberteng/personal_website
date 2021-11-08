from web import db

class User(db.Model):
    __tablename__ = 'user_tbl'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"id: {self.id} username: {self.username} password_hash: {self.password_hash}"


class Merchandise(db.Model):
    __tablename__ = 'merchandise_tbl'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"id: {self.id} username: {self.username} password_hash: {self.password_hash}"