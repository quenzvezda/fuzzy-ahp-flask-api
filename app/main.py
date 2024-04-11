# app/main.py

from flask import Blueprint
from app.controller.upload_controller import upload_file, get_data, delete_data

main = Blueprint('main', __name__)


@main.route('/api/upload', methods=['POST'])
def upload():
    return upload_file()


@main.route('/api/data', methods=['GET'])
def data():
    return get_data()


@main.route('/api/data/<filename>', methods=['DELETE'])
def delete(filename):
    return delete_data(filename)
