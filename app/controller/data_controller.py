# app/controller/data_controller.py
from flask import Blueprint, jsonify
from app.service.data_service import get_file_list, delete_file

data_bp = Blueprint('data', __name__)


@data_bp.route('/api/data', methods=['GET'])
def data():
    files = get_file_list()
    return jsonify(files)


@data_bp.route('/api/data/<filename>', methods=['DELETE'])
def delete(filename):
    result = delete_file(filename)
    return jsonify(result)
