from flask import Blueprint, request, jsonify
from app.services.product_service import (
    create_product,
    get_product,
    get_all_products,
    update_product,
    delete_product,
)

product_bp = Blueprint("product_bp", __name__)


@product_bp.route("/", methods=["GET"])
def list_products():
    return jsonify(get_all_products())


@product_bp.route("/<int:product_id>/", methods=["GET"])
def get_product_by_id(product_id):
    result = get_product(product_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@product_bp.route("/", methods=["POST"])
def create_product_view():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    result = create_product(name)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@product_bp.route("/<int:product_id>/", methods=["PUT"])
def update_product_view(product_id):
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    result = update_product(product_id, name)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@product_bp.route("/<int:product_id>/", methods=["DELETE"])
def delete_product_view(product_id):
    result = delete_product(product_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)
