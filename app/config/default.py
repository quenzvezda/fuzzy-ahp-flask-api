# app/config/default.py
import os


class Config:
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000,https://fuzzy-ahp-react.vercel.app').split(',')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 Megabytes
