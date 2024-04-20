# app/service/upload_service.py
import json

import pandas as pd
from flask import current_app
from werkzeug.utils import secure_filename
import os
import random

from app.util.directory_util import ensure_directory_exists


def convert_to_json(file_path, new_filename, upload_folder):
    if new_filename.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif new_filename.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        return {'error': 'Unsupported file format'}, 415

    columns_order = list(df.columns)
    json_folder = os.path.join(upload_folder, "json")
    ensure_directory_exists(json_folder)
    json_path = os.path.join(json_folder, os.path.splitext(new_filename)[0] + '.json')
    df.to_json(json_path, orient='records', lines=True)

    columns_path = os.path.join(json_folder, os.path.splitext(new_filename)[0] + '_columns.json')
    with open(columns_path, 'w') as f:
        json.dump(columns_order, f)

    return json_path



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

        # Konversi file yang diupload ke JSON dan simpan di subfolder "json"
        json_path = convert_to_json(file_path, new_filename, upload_folder)
        if isinstance(json_path, dict):  # Cek jika terjadi error pada konversi
            return json_path

        return {'message': 'File uploaded and converted to JSON successfully', 'filename': new_filename,
                'json_path': json_path}, 200

    return {'error': 'No file provided'}, 400
