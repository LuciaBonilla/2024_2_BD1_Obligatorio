from flask import request, jsonify
from model.ReportMaker import ReportMaker
from model.Validator import Validator

class ReportesController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_most_profitable_activities():
        """
            Estado: método terminado.
        """
        try:
            # body_request = request.get_json() # Da un diccionario.

            # is_admin = Validator.is_admin(body_request=body_request)
            # if (not is_admin):
            #     return jsonify({"message": "Unauthorized"}), 401
            
            actividades = ReportMaker.get_most_profitable_activities()
            if (actividades is None):
                return jsonify({"message": "Activities not found"}), 404
                
            return jsonify(actividades), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_most_populate_schedules():
        """
            Estado: método terminado.
        """
        try:
            # body_request = request.get_json() # Da un diccionario.

            # is_admin = Validator.is_admin(body_request=body_request)
            # if (not is_admin):
            #     return jsonify({"message": "Unauthorized"}), 401
                
            turnos = ReportMaker.get_most_populate_schedules()
            if (turnos == None):
                return jsonify({"message": "Schedules not found"}), 404
            
            return jsonify(turnos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_most_populate_activities():
        """
            Estado: método terminado.
        """
        try:
            # body_request = request.get_json() # Da un diccionario.

            # is_admin = Validator.is_admin(body_request=body_request)
            # if (not is_admin):
            #     return jsonify({"message": "Unauthorized"}), 401
                
            actividades = ReportMaker.get_most_populate_activities()
            if (actividades == None):
                return jsonify({"message": "Activities not found"}), 404
            
            return jsonify(actividades), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500