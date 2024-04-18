# app/service/data_service.py

from datetime import datetime
import os


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
