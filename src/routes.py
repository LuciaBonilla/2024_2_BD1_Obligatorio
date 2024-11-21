from flask import Blueprint, request, jsonify, current_app

# CONTROLADORES.
from controllers.actividadesController import ActividadesController
from controllers.turnosController import TurnosController
from controllers.instructoresController import instructoresController

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

# INSTRUCTORES
@api.route("/instructores", methods=["GET"])
def getAllInstructores():
    return instructoresController.getAllInstructores()

@api.route("/instructores/<int:ci>", methods=["GET"])
def getInstructorByCi(ci):
    return instructoresController.getInstructorByCi(ci)

@api.route("/instructores", methods=["POST"])
def postInstructor():
    current_app.logger.info(f"Creating new instructor: {request}")

    return instructoresController.createInstructor(request)

@api.route("/instructores/<int:ci>", methods=["PUT"])
def putInstructor(ci):
    current_app.logger.info(f"Updating instructor with CI: {ci}")

    return instructoresController.updateInstructor(ci, request)

# - **Endpoints:**
#   - `DELETE /api/Instructores/<int:id>`: Delete an instructor by CI.