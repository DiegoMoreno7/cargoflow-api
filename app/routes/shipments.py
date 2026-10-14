from flask import Blueprint, jsonify, request

from app import db
from app.models import Shipment

shipments_bp = Blueprint("shipments", __name__)


@shipments_bp.get("/shipments")
def list_shipments():
    status = request.args.get("status")

    query = Shipment.query
    if status:
        query = query.filter_by(status=status)

    shipments = query.all()
    return jsonify([shipment.to_dict() for shipment in shipments]), 200


@shipments_bp.get("/shipments/<int:shipment_id>")
def get_shipment(shipment_id):
    shipment = Shipment.query.get(shipment_id)

    if shipment is None:
        return jsonify(error="Envío no encontrado"), 404

    return jsonify(shipment.to_dict()), 200


@shipments_bp.post("/shipments")
def create_shipment():
    payload = request.get_json(silent=True)

    shipment = Shipment(
        origin=payload["origin"],
        destination=payload["destination"],
        weight_kg=payload["weight_kg"],
        customer_id=payload["customer_id"],
    )

    db.session.add(shipment)
    db.session.commit()

    return jsonify(shipment.to_dict()), 201
