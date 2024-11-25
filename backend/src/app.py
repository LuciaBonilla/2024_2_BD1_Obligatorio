from flask import Flask
from flask_cors import CORS
import logging

# RUTAS.
from routes import api

# Inicialización de la aplicación Flask.
app = Flask(__name__)
app.config['DEBUG'] = True 
CORS(app)

logging.basicConfig(level=logging.INFO)

# Registro del blueprint de rutas. Usar la URI (http://localhost:3006/api)
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
