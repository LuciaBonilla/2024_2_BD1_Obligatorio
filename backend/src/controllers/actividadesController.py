from flask import request, jsonify
from model.entities.Actividad import Actividad
from model.Validator import Validator

class ActividadesController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_actividades():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
            
            actividades = Actividad.get_all_actividades()
            if (actividades is None):
                return jsonify({"message": "Activities not found"}), 404
                
            return jsonify(actividades), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_actividad_by_id(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            actividad = Actividad.get_actividad_by_id(id=id)
            if (actividad == None):
                return jsonify({"message": "Activity not found"}), 404
                
            if (actividad == "duplicated"):
                return jsonify({"message": "Activity duplicated, server can't handle it"}), 500
            
            return jsonify(actividad), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def update_actividad(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            actividad = Actividad.get_actividad_by_id(id=id)
            if (actividad == None):
                return jsonify({"message": "Activity not found"}), 404
            
            if (actividad == "duplicated"):
                return jsonify({"message": "Activity duplicated, server can't handle"}), 500
                
            actividad = Actividad(
                nombre=body_request["nombre"] if "nombre" in body_request else actividad["nombre"],
                descripcion=body_request["descripcion"] if "descripcion" in body_request else actividad["descripcion"],
                costo=body_request["costo"] if "costo" in body_request else actividad["costo"],
                edad_minima=body_request["edad_minima"] if "edad_minima" in body_request else actividad["edad_minima"],
            )
            operation_result = actividad.update(id=id)
            if (operation_result):
                return jsonify({"message": "Activity updated successfully", "id": id}), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
