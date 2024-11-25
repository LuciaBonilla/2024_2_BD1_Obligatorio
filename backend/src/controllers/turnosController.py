from flask import request, jsonify
from model.entities.Turno import Turno
from model.Validator import Validator

class TurnosController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_turnos():
        """
            Estado: método terminado.
        """
        try:
            # body_request = request.get_json() # Da un diccionario.

            # is_admin = Validator.is_admin(body_request=body_request)
            # if (not is_admin):
            #     return jsonify({"message": "Unauthorized"}), 401
            
            turnos = Turno.get_all_turnos()
            if (turnos is None):
                return jsonify({"message": "Schedules not found"}), 404
                
            return jsonify(turnos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_turno_by_id(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            turno = Turno.get_turno_by_id(id=id)
            if (turno == None):
                return jsonify({"message": "Schedule not found"}), 404
                
            if (turno == "duplicated"):
                return jsonify({"message": "Schedule duplicated, server can't handle it"}), 500
            
            return jsonify(turno), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_turno():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            for field in Turno.values_needed:
                if field not in body_request:
                    return jsonify({"error": f"Missing field: {field}"}), 400
                
            turno = Turno(
                hora_inicio=body_request["hora_inicio"],
                hora_fin=body_request["hora_fin"]
            )
            operation_result = turno.insert()
            if (operation_result):
                return jsonify({"message": "Schedule created successfully"}), 201
            else:
                return jsonify({"message": "Error creating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def update_turno(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            turno = Turno.get_turno_by_id(id=id)
            if (turno == None):
                return jsonify({"message": "Schedule not found"}), 404
            
            if (turno == "duplicated"):
                return jsonify({"message": "Schedule duplicated, server can't handle"}), 500
                
            turno = Turno(
                hora_inicio=body_request["hora_inicio"] if "hora_inicio" in body_request else turno["hora_inicio"],
                hora_fin=body_request["hora_fin"] if "hora_fin" in body_request else turno["hora_fin"]
            )
            operation_result = turno.update(id=id)
            if (operation_result):
                return jsonify({"message": "Schedule updated successfully"}), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_turno(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            turno = Turno.get_turno_by_id(id=id)
            if (turno == None):
                return jsonify({"message": "Schedule not found"}), 404
                
            if (turno == "duplicated"):
                return jsonify({"message": "Schedule duplicated, server can't handle it"}), 500
                    
            turno = Turno(
                hora_inicio=turno["hora_inicio"],
                hora_fin=turno["hora_fin"]
            )
            operation_result = turno.delete(id=id)
            if (operation_result):
                return jsonify({"message": "Schedule deleted successfully"}), 200
            else:
                return jsonify({"message": "Error deleting"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
