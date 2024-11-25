from flask import Blueprint, jsonify

# CONTROLADORES.
from controllers.actividadesController import ActividadesController
from controllers.alumnosController import AlumnosController
from controllers.asistenciasController import AsistenciasController
from controllers.clasesController import ClasesController
from controllers.equipamientosController import EquipamientosController
from controllers.instructoresController import InstructoresController
from controllers.reportesController import ReportesController
from controllers.turnosController import TurnosController

# MODEL PARA CHECKEAR CONEXIÓN A LA BASE DE DATOS.
from model.MySQLScriptRunner import MySQLScriptRunner

# Crea un Blueprint para organizar las rutas
api = Blueprint("api", __name__)

# PRINCIPAL.x
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

# ACTIVIDADES.x
@api.route("/actividades", methods=["GET"])
def get_all_actividades():
    return ActividadesController.get_all_actividades()

@api.route("/actividades/<int:id>", methods=["GET"])
def get_actividad_by_id(id):
    return ActividadesController.get_actividad_by_id(id=id)

@api.route("/actividades/<int:id>", methods=["PATCH"])
def patch_actividad(id):
    return ActividadesController.update_actividad(id=id)

# TURNOS.x
@api.route("/turnos", methods=["GET"])
def get_all_turnos():
    return TurnosController.get_all_turnos()

@api.route("/turnos/<int:id>", methods=["GET"])
def get_turno_by_id(id):
    return TurnosController.get_turno_by_id(id=id)

@api.route("/turnos", methods=["POST"])
def post_turno():
    return TurnosController.create_turno()

@api.route("/turnos/<int:id>", methods=["PATCH"])
def patch_turno(id):
    return TurnosController.update_turno(id=id)

@api.route("/turnos/<int:id>", methods=["DELETE"])
def delete_turno(id):
    return TurnosController.delete_turno(id=id)

# INSTRUCTORES.x
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
def patch_instructor(ci):
    return InstructoresController.update_instructor(ci=ci)

@api.route("/instructores/<int:ci>", methods=["DELETE"])
def delete_instructor(ci):
    return InstructoresController.delete_instructor(ci=ci)

# ALUMNOS.x
@api.route("/alumnos", methods=["GET"])
def get_all_alumnos():
    return AlumnosController.get_all_alumnos()

@api.route("/alumnos/<int:ci>", methods=["GET"])
def get_alumno_by_ci(ci):
    return AlumnosController.get_alumno_by_ci(ci=ci)

@api.route("/alumnos", methods=["POST"])
def post_alumno():
    return AlumnosController.create_alumno()

@api.route("/alumnos/<int:ci>", methods=["PATCH"])
def patch_alumno(ci):
    return AlumnosController.update_alumno(ci=ci)

@api.route("/alumnos/<int:ci>", methods=["DELETE"])
def delete_alumno(ci):
    return AlumnosController.delete_alumno(ci=ci)

# CLASES.
@api.route("/clases", methods=["GET"])
def get_all_clases():
    return ClasesController.get_all_clases()

@api.route("/clases/<int:id>", methods=["GET"])
def get_clase_by_id(id):
    return ClasesController.get_clase_by_id(id=id)

@api.route("/clases", methods=["POST"])
def post_clase():
    return ClasesController.create_clase()

@api.route("/clases/<int:id>", methods=["PATCH"])
def patch_clase(id):
    return ClasesController.update_clase(id=id)

@api.route("/clases/<int:id>", methods=["DELETE"])
def delete_clase(id):
    return ClasesController.delete_clase(id=id)

# EQUIPAMIENTOS.
@api.route("/equipamientos", methods=["GET"])
def get_all_equipamientos():
    return EquipamientosController.get_all_equipamientos()

@api.route("/equipamientos/<int:id>", methods=["GET"])
def get_equipamiento_by_id(id):
    return EquipamientosController.get_equipamiento_by_id(id=id)

# ASISTENCIAS.
@api.route("/asistencias", methods=["GET"])
def get_all_asistencias():
    return AsistenciasController.get_all_asistencias()

@api.route("/asistencias/clases/<int:id>/alumnos/<int:ci>", methods=["GET"])
def get_asistencia_by_id_clase_and_ci_alumno(id, ci):
    return AsistenciasController.get_asistencia_by_id_clase_and_ci_alumno(ci_alumno=ci, id_clase=id)

@api.route("/asistencias", methods=["POST"])
def post_asistencia():
    return AsistenciasController.create_asistencia()

@api.route("/asistencias/clases/<int:id>/alumnos/<int:ci>", methods=["PATCH"])
def patch_asistencia(id, ci):
    return AsistenciasController.update_asistencia(ci_alumno=ci, id_clase=id)

@api.route("/asistencias/clases/<int:id>/alumnos/<int:ci>", methods=["DELETE"])
def delete_asistencia(id, ci):
    return AsistenciasController.delete_asistencia(ci_alumno=ci, id_clase=id)

# REPORTES.

@api.route("/reportes/actividades_mas_ingresos", methods=["GET"])
def get_most_profitable_activities():
    return ReportesController.get_most_profitable_activities()

@api.route("/reportes/turnos_mas_frecuentes", methods=["GET"])
def get_most_populate_schedules():
    return ReportesController.get_most_populate_schedules()

@api.route("/reportes/actividades_mas_alumnos", methods=["GET"])
def get_most_populate_activities():
    return ReportesController.get_most_populate_activities()