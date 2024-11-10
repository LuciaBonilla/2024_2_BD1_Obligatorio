from flask import Blueprint, request, jsonify

# CONTROLADORES.
from controllers.actividadesController import ActividadesController
from controllers.turnosController import TurnosController

# MODEL PARA CHECKEAR CONEXIÓN A LA BASE DE DATOS.
from model.MySQLScriptsExecutor import MySQLScriptsExecutor

# Crea un Blueprint para organizar las rutas
api = Blueprint("api", __name__)

# PRINCIPAL.
@api.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Escuela de deportes de nieve de la UCU"}), 200

# PARA CHECKEAR CONEXIÓN A LA BASE DE DATOS.
@api.route("/ping", methods=["GET"])
def checkDatabaseConnection():
    status = MySQLScriptsExecutor.getDatabaseConnectionStatus()
    
    if status:
        return jsonify({"message": "Conexión exitosa a la base de datos"}), 200
    else:
        return jsonify({"message": "Conexión NO exitosa a la base de datos"}), 500

# ACTIVIDADES.
@api.route("/actividades", methods=["GET"])
def getAllActividades():
    return ActividadesController.getAllActividades()

@api.route("/actividades", methods=["POST"])
def postActividad():
    return ActividadesController.createActividad(request)

# TURNOS.
@api.route("/turnos", methods=["GET"])
def getAllTurnos():
    return TurnosController.getAllTurnos()