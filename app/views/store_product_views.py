from flask import Blueprint, request, jsonify
from app.services.store_product_service import (
    create_store_product,
    get_store_product,
    get_all_store_products,
    get_store_products_by_store,
    update_store_product,
    delete_store_product,
    get_products_in_store,
    get_product_info_in_store
)

store_product_bp = Blueprint(
    "store_product_bp",
    __name__,
)


@store_product_bp.route("/", methods=["GET"])
def list_store_products():
    return jsonify(get_all_store_products())


@store_product_bp.route("/<int:sp_id>/", methods=["GET"])
def get_store_product_by_id(sp_id):
    result = get_store_product(sp_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_product_bp.route("/store/<int:store_id>/", methods=["GET"])
def get_products_by_store(store_id):
    return jsonify(get_store_products_by_store(store_id))


@store_product_bp.route("/", methods=["POST"])
def create_store_product_view():
    data = request.get_json()
    store_id = data.get("store_id")
    product_id = data.get("product_id")
    price = data.get("price")
    inventory = data.get("inventory")
    if not all([store_id, product_id, price is not None, inventory is not None]):
        return (
            jsonify(
                {"error": "store_id, product_id, price, and inventory are required"}
            ),
            400,
        )
    result = create_store_product(store_id, product_id, price, inventory)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_product_bp.route("/<int:sp_id>/", methods=["PUT"])
def update_store_product_view(sp_id):
    data = request.get_json()
    price = data.get("price")
    inventory = data.get("inventory")
    if price is None and inventory is None:
        return jsonify({"error": "At least one of price or inventory is required"}), 400
    result = update_store_product(sp_id, price, inventory)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_product_bp.route("/<int:sp_id>/", methods=["DELETE"])
def delete_store_product_view(sp_id):
    result = delete_store_product(sp_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_product_bp.route("/products-in-store/<int:store_id>/", methods=["GET"])
def products_in_store(store_id):
    return jsonify(get_products_in_store(store_id))


@store_product_bp.route(
    "/product-info/<int:store_id>/<int:product_id>/", methods=["GET"]
)
def product_info_in_store(store_id, product_id):
    result = get_product_info_in_store(store_id, product_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)
