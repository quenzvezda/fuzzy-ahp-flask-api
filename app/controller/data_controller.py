# app/controller/data_controller.py
from flask import jsonify, current_app, Blueprint
from app.service.data_service import get_file_list, delete_file

data_bp = Blueprint('data', __name__)


@data_bp.route('/api/data', methods=['GET'])
def data():
    files = get_file_list(current_app.config['UPLOAD_FOLDER'])
    return jsonify(files)


@data_bp.route('/api/data/<filename>', methods=['DELETE'])
def delete(filename):
    return jsonify(delete_file(filename, current_app.config['UPLOAD_FOLDER']))
