# app/service/upload_service.py

from werkzeug.utils import secure_filename
from datetime import datetime
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


def get_file_list(upload_folder):
    files = []
    for filename in os.listdir(upload_folder):
        file_path = os.path.join(upload_folder, filename)
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            creation_time = os.path.getctime(file_path)
            date_created = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            name, extension = os.path.splitext(filename)
            files.append({
                'name': name,
                'extension': extension,
                'size': size,
                'date_created': date_created
            })
    return files


def delete_file(filename, upload_folder):
    file_path = os.path.join(upload_folder, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {'message': f'File {filename} deleted successfully'}, 200
    return {'error': f'File {filename} not found'}, 404
