from app.extensions import db


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    products = db.relationship("StoreProduct", backref="store", lazy=True)
