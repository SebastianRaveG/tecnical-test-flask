from app import db
from app.models.store import Store
from sqlalchemy.exc import IntegrityError


def create_store(name):
    store = Store(name=name)
    db.session.add(store)
    try:
        db.session.commit()
        return {
            "message": "Store created",
            "store": {"id": store.id, "name": store.name},
        }, 201
    except IntegrityError:
        db.session.rollback()
        return {"error": "Store with this name already exists."}, 400


def get_store(store_id):
    store = Store.query.get(store_id)
    if store:
        return {"id": store.id, "name": store.name}
    return {"error": "Store not found"}, 404


def get_all_stores():
    return [{"id": s.id, "name": s.name} for s in Store.query.all()]


def update_store(store_id, name):
    store = Store.query.get(store_id)
    if not store:
        return {"error": "Store not found"}, 404
    store.name = name
    try:
        db.session.commit()
        return {
            "message": "Store updated",
            "store": {"id": store.id, "name": store.name},
        }
    except IntegrityError:
        db.session.rollback()
        return {"error": "Store with this name already exists."}, 400


def delete_store(store_id):
    store = Store.query.get(store_id)
    if not store:
        return {"error": "Store not found"}, 404
    db.session.delete(store)
    db.session.commit()
    return {"message": "Store deleted"}
