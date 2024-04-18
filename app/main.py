# app/main.py

from flask import Flask
from app.controller.upload_controller import upload_bp
from app.controller.data_controller import data_bp


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(data_bp)

    return app
