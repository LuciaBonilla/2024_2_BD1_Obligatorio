from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Obtiene las variables de entorno para la base de datos, definidas en docker-compose.yml.
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# Ruta principal.
@app.route("/")
def index():
    return jsonify(message="Deportes de nieve UCU")

# Objetivo de ruta: Checkear la conexión con la base de datos.
@app.route("/db-check", methods=["GET"])
def db_check():
    try:
        # Intenta conectarse a la base de datos usando las variables de entorno.
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        if connection.is_connected():
            return jsonify({"message": f"Conexión exitosa a la base de datos: {DB_NAME}"}), 200
        else:
            return jsonify({"message": "Error al conectar con la base de datos"}), 500
    except mysql.connector.Error as err:
        return jsonify({"message": f"Error al conectar a la base de datos: {err}"}), 500
    finally:
        # Cierra la conexión si fue exitosa.
        if "connection" in locals() and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
