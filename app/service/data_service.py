# app/service/data_service.py
import json
import time
from datetime import datetime
import os
import pandas as pd
from flask import current_app
from app.util.directory_util import ensure_directory_exists


def get_file_list():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    ensure_directory_exists(upload_folder)

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


def delete_file(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder, filename)

    # Tentukan path file JSON
    json_folder = os.path.join(upload_folder, "json")
    json_file_path = os.path.join(json_folder, os.path.splitext(filename)[0] + '.json')

    messages = []
    error = False

    # Hapus file utama jika ada
    if os.path.exists(file_path):
        os.remove(file_path)
        messages.append(f'File {filename} deleted successfully')
    else:
        messages.append(f'File {filename} not found')
        error = True

    # Hapus file JSON jika ada
    if os.path.exists(json_file_path):
        os.remove(json_file_path)
        messages.append(f'JSON file for {filename} deleted successfully')
    else:
        messages.append(f'JSON file for {filename} not found')
        error = True

    if error:
        return {'error': ' '.join(messages)}, 404
    return {'message': ' '.join(messages)}, 200


def paginate_data_json(filename, page, per_page=10):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    json_path = os.path.join(upload_folder, filename.rsplit('.', 1)[0] + '.json')

    if not os.path.exists(json_path):
        return {'error': 'JSON file not found'}, 404

    # Hitung baris awal berdasarkan halaman dan jumlah per halaman
    start_line = (page - 1) * per_page
    data = read_json_partial(json_path, start_line, per_page)

    # Anggap total baris tersedia di tempat lain atau hitung sekali dan simpan
    # Sementara ini, kembalikan data tanpa info total halaman
    return {'data': data, 'page': page, 'per_page': per_page}


def count_total_rows(file_path, filename):
    if filename.endswith('.csv'):
        with open(file_path, 'r') as file:
            return sum(1 for row in file) - 1  # Mengurangi satu untuk header
    elif filename.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
        return len(df)


def read_json_partial(file_path, start_line, num_lines):
    data = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= start_line + num_lines:
                break
            if i >= start_line:
                data.append(json.loads(line))
    return data