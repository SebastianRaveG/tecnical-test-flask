from app.extensions import db, migrate
# Importar todos los modelos para que se registren
from app.models.store import Store
from app.models.product import Product
from app.models.store_product import StoreProduct

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
