from app import db
from app.models.product import Product
from sqlalchemy.exc import IntegrityError

def create_product(name):
    product = Product(name=name)
    db.session.add(product)
    try:
        db.session.commit()
        return {"message": "Product created", "product": {"id": product.id, "name": product.name}}
    except IntegrityError:
        db.session.rollback()
        return {"error": "Product with this name already exists."}, 400

def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return {"id": product.id, "name": product.name}
    return {"error": "Product not found"}, 404

def get_all_products():
    return [{"id": p.id, "name": p.name} for p in Product.query.all()]

def update_product(product_id, name):
    product = Product.query.get(product_id)
    if not product:
        return {"error": "Product not found"}, 404
    product.name = name
    try:
        db.session.commit()
        return {"message": "Product updated", "product": {"id": product.id, "name": product.name}}
    except IntegrityError:
        db.session.rollback()
        return {"error": "Product with this name already exists."}, 400

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return {"error": "Product not found"}, 404
    db.session.delete(product)
    db.session.commit()
    return {"message": "Product deleted"}
