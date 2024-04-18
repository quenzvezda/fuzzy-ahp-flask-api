# app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.config.default import Config
from app.controller.upload_controller import upload_bp
from app.controller.data_controller import data_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=Config.CORS_ORIGINS)

    # Register Blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(data_bp)

    return app
