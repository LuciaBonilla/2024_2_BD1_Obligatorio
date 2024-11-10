from model.UCUSnowSportsSchoolQuerier import UCUSnowSportsSchoolQuerier
from flask import jsonify

class TurnosController:
    @staticmethod
    def getAllTurnos():
        """
        Llama al método del modelo para obtener todos los turnos y devuelve los datos formateados.
        """
        turnos = UCUSnowSportsSchoolQuerier.getAllTurnos()
        if (turnos is not None):
            return jsonify(turnos), 200
        else:
            return jsonify({"message": "No se encontraron turnos."}), 200