import re
from flask import Blueprint, jsonify, request
from app import db
from app.models import Customer

customers_bp = Blueprint("customers", __name__)

@customers_bp.get("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if customer is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(customer.to_dict()), 200


@customers_bp.post("/customers")
def create_customer():
    if not request.is_json:
        return jsonify({"error": "El Content-Type debe ser application/json"}), 400
    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "El JSON no tiene formato valido"}), 400

    if not isinstance(payload, dict):
        return jsonify({
            "error": "El cuerpo de la petición debe ser un objeto JSON válido"
            }), 400

    campos_requeridos = ["name", "email"]
    campos_faltantes = [campo for campo in campos_requeridos if campo not in payload]

    if campos_faltantes:
        return jsonify({
            "error": f"Faltan campos obligatorios: {', '.join(campos_faltantes)}"}), 400

    if (
        not isinstance(payload["name"], str)
        or not isinstance(payload["email"], str)
        or not payload["name"].strip()
        or not payload["email"].strip()
    ):
        return jsonify({
            "error": "Los campos email y name deben ser textos no vacíos"
        }), 400
    
    patron_correo = r"^[\w.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    if not re.match(patron_correo, payload["email"]):
        return jsonify({"error": "Formato de email no valido"}), 400
    customer = Customer(
        name=payload["name"],
        email=payload["email"],
    )

    db.session.add(customer)
    db.session.commit()

    return jsonify(customer.to_dict()), 201
