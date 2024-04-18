import os


def ensure_directory_exists(folder):
    os.makedirs(folder, exist_ok=True)
