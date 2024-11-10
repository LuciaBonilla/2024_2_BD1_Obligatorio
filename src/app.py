from flask import Flask

# RUTAS.
from routes import api

# Inicialización de la aplicación Flask.
app = Flask(__name__)

# Registro del blueprint de rutas. Usar la URI (http://localhost:3006/api)
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)