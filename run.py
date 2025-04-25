from flask import Flask
from dotenv import load_dotenv
import os

from app import init_app
from app.views.store_views import store_bp
from app.views.product_views import product_bp
from app.views.store_product_views import store_product_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:e4ZXY8YyHBhPhj9f@192.168.20.34:5433/tecnical_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_app(app)

    app.register_blueprint(store_bp, url_prefix='/stores')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(store_product_bp, url_prefix='/store-products')

    return app

app = create_app() 
