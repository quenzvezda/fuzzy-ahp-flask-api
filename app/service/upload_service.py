# app/service/upload_service.py

from werkzeug.utils import secure_filename
import os
import random


def save_file(file, upload_folder):
    if file:
        filename = secure_filename(file.filename)
        name, ext = os.path.splitext(filename)
        random_suffix = random.randint(1000000, 9999999)  # Generate a random number between 1,000,000 and 9,999,999
        new_filename = f"{name}_{random_suffix}{ext}"  # Add the random suffix to the filename
        file.save(os.path.join(upload_folder, new_filename))
        return {'message': 'File uploaded successfully', 'filename': new_filename}, 200
    return {'error': 'No file provided'}, 400
