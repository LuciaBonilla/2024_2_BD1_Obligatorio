from flask import request, jsonify, json, current_app
from model.entities.Equipamiento import Equipamiento
from model.Validator import Validator

class EquipamientosController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_equipamientos():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
            
            equipamientos = Equipamiento.get_all_equipamientos()
            if (equipamientos is None):
                return jsonify({"message": "Equipments not found"}), 404
                
            return jsonify(equipamientos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_equipamiento_by_id(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            equipamiento = Equipamiento.get_equipamiento_by_id(id=id)
            if (equipamiento == None):
                return jsonify({"message": "Equipment not found"}), 404
                
            if (equipamiento == "duplicated"):
                return jsonify({"message": "Equipment duplicated, server can't handle it"}), 500
            
            return jsonify(equipamiento), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
