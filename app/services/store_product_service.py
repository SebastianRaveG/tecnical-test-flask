from app import db
from app.models.store_product import StoreProduct
from app.models.store import Store
from app.models.product import Product
from sqlalchemy.exc import IntegrityError


def create_store_product(store_id, product_id, price, inventory):
    if not Store.query.get(store_id):
        return {"error": "Store not found"}, 404
    if not Product.query.get(product_id):
        return {"error": "Product not found"}, 404
    sp = StoreProduct(
        store_id=store_id, product_id=product_id, price=price, inventory=inventory
    )
    db.session.add(sp)
    try:
        db.session.commit()
        return {
            "message": "StoreProduct created",
            "store_product": {
                "id": sp.id,
                "store_id": sp.store_id,
                "product_id": sp.product_id,
                "price": sp.price,
                "inventory": sp.inventory,
            },
        }, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "This store-product relation already exists."}, 400


def get_store_product(sp_id):
    sp = StoreProduct.query.get(sp_id)
    if sp:
        return {
            "id": sp.id,
            "store_id": sp.store_id,
            "product_id": sp.product_id,
            "price": sp.price,
            "inventory": sp.inventory,
        }
    return {"error": "StoreProduct not found"}, 404


def get_all_store_products():
    return [
        {
            "id": sp.id,
            "store_id": sp.store_id,
            "product_id": sp.product_id,
            "price": sp.price,
            "inventory": sp.inventory,
        }
        for sp in StoreProduct.query.all()
    ]


def get_store_products_by_store(store_id):
    return [
        {
            "id": sp.id,
            "store_id": sp.store_id,
            "product_id": sp.product_id,
            "price": sp.price,
            "inventory": sp.inventory,
        }
        for sp in StoreProduct.query.filter_by(store_id=store_id).all()
    ]


def update_store_product(sp_id, price=None, inventory=None):
    sp = StoreProduct.query.get(sp_id)
    if not sp:
        return {"error": "StoreProduct not found"}, 404
    if price is not None:
        sp.price = price
    if inventory is not None:
        sp.inventory = inventory
    db.session.commit()
    return {
        "message": "StoreProduct updated",
        "store_product": {
            "id": sp.id,
            "store_id": sp.store_id,
            "product_id": sp.product_id,
            "price": sp.price,
            "inventory": sp.inventory,
        },
    }


def delete_store_product(sp_id):
    sp = StoreProduct.query.get(sp_id)
    if not sp:
        return {"error": "StoreProduct not found"}, 404
    db.session.delete(sp)
    db.session.commit()
    return {"message": "StoreProduct deleted"}


def get_products_in_store(store_id):
    from app.models.product import Product

    results = (
        db.session.query(StoreProduct, Product)
        .join(Product, StoreProduct.product_id == Product.id)
        .filter(StoreProduct.store_id == store_id)
        .all()
    )
    return [
        {
            "store_product_id": sp.id,
            "product_id": p.id,
            "product_name": p.name,
            "price": sp.price,
            "inventory": sp.inventory,
        }
        for sp, p in results
    ]


def get_product_info_in_store(store_id, product_id):
    from app.models.product import Product

    result = (
        db.session.query(StoreProduct, Product)
        .join(Product, StoreProduct.product_id == Product.id)
        .filter(
            StoreProduct.store_id == store_id, StoreProduct.product_id == product_id
        )
        .first()
    )
    if not result:
        return {"error": "No such product in this store"}, 404
    sp, p = result
    return {
        "store_product_id": sp.id,
        "product_id": p.id,
        "product_name": p.name,
        "price": sp.price,
        "inventory": sp.inventory,
    }
