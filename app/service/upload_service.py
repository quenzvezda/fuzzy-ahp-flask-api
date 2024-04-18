# app/service/upload_service.py
from flask import current_app
from werkzeug.utils import secure_filename
import os
import random

from app.util.directory_util import ensure_directory_exists


def save_file(file):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    ensure_directory_exists(upload_folder)

    if file:
        filename = secure_filename(file.filename)
        name, ext = os.path.splitext(filename)
        random_suffix = random.randint(1000000, 9999999)  # Generate a random number
        new_filename = f"{name}_{random_suffix}{ext}"
        file_path = os.path.join(upload_folder, new_filename)
        file.save(file_path)
        return {'message': 'File uploaded successfully', 'filename': new_filename}, 200
    return {'error': 'No file provided'}, 400
