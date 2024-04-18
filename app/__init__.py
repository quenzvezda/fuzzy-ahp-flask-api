# app/__init__.py
from flask import Flask
from flask_cors import CORS
import os


def create_app():
    app = Flask(__name__)

    cors_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000,https://fuzzy-ahp-react.vercel.app').split(',')
    CORS(app, origins=cors_origins)

    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    from app.controller.upload_controller import upload_bp
    from app.controller.data_controller import data_bp
    app.register_blueprint(upload_bp)
    app.register_blueprint(data_bp)

    return app
