# app/main.py

from flask import Blueprint
from app.controller.upload_controller import upload_file

main = Blueprint('main', __name__)

@main.route('/api/upload', methods=['POST'])
def upload():
    return upload_file()

# Daftarkan blueprint

