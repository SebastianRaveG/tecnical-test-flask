from flask import Blueprint, request, jsonify
from app.services.store_service import (
    create_store,
    get_store,
    get_all_stores,
    update_store,
    delete_store,
)

store_bp = Blueprint("store_bp", __name__)


@store_bp.route("/", methods=["GET"])
def list_stores():
    return jsonify(get_all_stores())


@store_bp.route("/<int:store_id>/", methods=["GET"])
def get_store_by_id(store_id):
    result = get_store(store_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_bp.route("/", methods=["POST"])
def create_store_view():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    result = create_store(name)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_bp.route("/<int:store_id>/", methods=["PUT"])
def update_store_view(store_id):
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    result = update_store(store_id, name)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)


@store_bp.route("/<int:store_id>/", methods=["DELETE"])
def delete_store_view(store_id):
    result = delete_store(store_id)
    if isinstance(result, tuple):
        return jsonify(result[0]), result[1]
    return jsonify(result)
