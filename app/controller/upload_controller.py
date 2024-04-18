# app/controller/upload_controller.py
from flask import Blueprint, request, jsonify
from app.service.upload_service import save_file

upload_bp = Blueprint('upload', __name__)


@upload_bp.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    response = save_file(file)
    return jsonify(response)
