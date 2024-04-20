# app/service/data_service.py
import json
import os
from datetime import datetime

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
    # Bangun path ke file JSON dalam subfolder 'json'
    json_path = os.path.join(upload_folder, 'json', os.path.splitext(filename)[0] + '.json')

    if not os.path.exists(json_path):
        return {'error': 'JSON file not found'}, 404

    # Menghitung jumlah total baris di file JSON untuk informasi paginasi
    total = count_total_rows(json_path)

    # Menghitung indeks baris untuk paginasi
    start_line = (page - 1) * per_page
    num_lines = per_page
    data = read_json_partial(json_path, start_line, num_lines)

    # Hitung total halaman
    total_pages = (total + per_page - 1) // per_page

    return {
        'data': data,
        'page': page,
        'per_page': per_page,
        'total_pages': total_pages,
        'total': total
    }


def read_json_partial(json_path, start_line, num_lines):
    data = []
    with open(json_path, 'r') as file:
        for i, line in enumerate(file):
            if i >= start_line + num_lines:
                break
            if i >= start_line:
                data.append(json.loads(line))
    return data


def count_total_rows(json_path):
    with open(json_path, 'r') as file:
        return sum(1 for line in file)
