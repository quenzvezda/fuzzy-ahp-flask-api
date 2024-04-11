# app/__init__.py

from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Konfigurasi folder tempat menyimpan file yang diupload
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Batas maksimum ukuran file (dalam bytes), misalnya 16MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    # Import dan daftarkan blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
