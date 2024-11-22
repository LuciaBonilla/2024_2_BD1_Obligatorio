from flask import Blueprint, jsonify

# CONTROLADORES.
from controllers.instructoresController import InstructoresController

# MODEL PARA CHECKEAR CONEXIÓN A LA BASE DE DATOS.
from model.MySQLScriptRunner import MySQLScriptRunner

# Crea un Blueprint para organizar las rutas
api = Blueprint("api", __name__)

# PRINCIPAL.
@api.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Escuela de deportes de nieve de la UCU"}), 200

# PARA CHECKEAR CONEXIÓN A LA BASE DE DATOS.
@api.route("/ping", methods=["GET"])
def checkDatabaseConnection():
    status = MySQLScriptRunner.get_database_connection_status()
    
    if (status):
        return jsonify({"message": "Conexión exitosa a la base de datos"}), 200
    else:
        return jsonify({"message": "Conexión NO exitosa a la base de datos"}), 500

# ACTIVIDADES.

# TURNOS.

# INSTRUCTORES
@api.route("/instructores", methods=["GET"])
def get_all_instructores():
    return InstructoresController.get_all_instructores()

@api.route("/instructores/<int:ci>", methods=["GET"])
def get_instructor_by_ci(ci):
    return InstructoresController.get_instructor_by_ci(ci=ci)

@api.route("/instructores", methods=["POST"])
def post_instructor():
    return InstructoresController.create_instructor()

@api.route("/instructores/<int:ci>", methods=["PATCH"])
def put_instructor(ci):
    return InstructoresController.update_instructor(ci=ci)

@api.route("/instructores/<int:ci>", methods=["DELETE"])
def delete_instructor(ci):
    return InstructoresController.delete_instructor(ci=ci)