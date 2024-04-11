# app/service/upload_service.py

from werkzeug.utils import secure_filename
import os


def save_file(file, upload_folder):
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))
        return {'message': 'File uploaded successfully'}, 200
    return {'error': 'No file provided'}, 400
