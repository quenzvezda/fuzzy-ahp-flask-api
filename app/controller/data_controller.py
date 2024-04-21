# app/controller/data_controller.py
import time

from flask import Blueprint, jsonify, request
from app.service.data_service import get_file_list, delete_file, paginate_data_json, get_column_names

data_bp = Blueprint('data', __name__)


@data_bp.route('/api/data', methods=['GET'])
def data():
    files = get_file_list()
    return jsonify(files)


@data_bp.route('/api/data/<filename>', methods=['DELETE'])
def delete(filename):
    result = delete_file(filename)
    return jsonify(result)


@data_bp.route('/api/data-show', methods=['GET'])
def show_data():
    filename = request.args.get('filename')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if not filename:
        return jsonify({'error': 'Filename parameter is required'}), 400

    result = paginate_data_json(filename, page, per_page)
    return jsonify(result)


@data_bp.route('/api/get-column', methods=['GET'])
def get_columns():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'Filename parameter is required'}), 400

    result = get_column_names(filename)
    return jsonify(result)