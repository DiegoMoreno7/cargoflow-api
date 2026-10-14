from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.shipments import shipments_bp

    app.register_blueprint(shipments_bp, url_prefix="/api/v1")

    @app.errorhandler(404)
    def handle_404(_error):
        return jsonify(error="Recurso no encontrado"), 404

    @app.errorhandler(500)
    def handle_500(_error):
        return jsonify(error="Error interno del servidor"), 500

    return app
