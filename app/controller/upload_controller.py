# app/controller/upload_controller.py

from flask import request, jsonify, current_app
from app.service.upload_service import save_file
from app.service.upload_service import get_file_list


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'xls', 'xlsx', 'csv'}


def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if allowed_file(file.filename):
        return jsonify(save_file(file, current_app.config['UPLOAD_FOLDER']))

    return jsonify({'error': 'File type not allowed'}), 400


def get_data():
    files = get_file_list(current_app.config['UPLOAD_FOLDER'])
    return jsonify(files)
