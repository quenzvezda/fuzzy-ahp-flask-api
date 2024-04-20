# app.py
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    host = os.getenv('SERVER_IP', '0.0.0.0')
    port = int(os.getenv('SERVER_PORT', '2722'))
    app.run(debug=True, host=host, port=port)
