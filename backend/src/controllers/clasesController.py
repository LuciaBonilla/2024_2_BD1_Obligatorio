from flask import request, jsonify
from model.entities.Clase import Clase
from model.Validator import Validator

class ClasesController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_clases():
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            clases = Clase.get_all_clases()
            if (clases is None):
                return jsonify({"message": "Classes not found"}), 404

            return jsonify(clases), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_clase_by_id(id: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            clase = Clase.get_clase_by_id(id=id)
            if (clase == None):
                return jsonify({"message": "Class not found"}), 404

            if (clase == "duplicated"):
                return jsonify({"message": "Class duplicated, server can't handle it"}), 500

            return jsonify(clase), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_clase():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            for field in Clase.values_needed:
                if field not in body_request:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            clase = Clase(
                ci_instructor=body_request["ci_instructor"],
                id_turno=body_request["id_turno"],
                id_actividad=body_request["id_actividad"],
                dictada=False  # Nueva clase no dictada.
            )
            operation_result = clase.insert()
            if (operation_result):
                return jsonify({"message": "Class created successfully"}), 201
            else:
                return jsonify({"message": "Error creating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_clase(id: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            clase = Clase.get_clase_by_id(id=id)
            if (clase == None):
                return jsonify({"message": "Class not found"}), 404

            if (clase == "duplicated"):
                return jsonify({"message": "Class duplicated, server can't handle"}), 500

            clase = Clase(
                ci_instructor=body_request["ci_instructor"] if "ci_instructor" in body_request else clase["ci_instructor"],
                id_turno=body_request["id_turno"] if "id_turno" in body_request else clase["id_turno"],
                id_actividad=body_request["id_actividad"] if "id_actividad" in body_request else clase["id_actividad"],
                dictada=body_request["dictada"] if "dictada" in body_request else clase["dictada"]
            )
            operation_result = clase.update(id=id)
            if (operation_result):
                return jsonify({"message": "Class updated successfully", "id": id}), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_clase(id: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            clase = Clase.get_clase_by_id(id=id)
            if (clase == None):
                return jsonify({"message": "Class not found"}), 404

            if (clase == "duplicated"):
                return jsonify({"message": "Class duplicated, server can't handle it"}), 500

            clase = Clase(
                ci_instructor=clase["ci_instructor"],
                id_turno=clase["id_turno"],
                id_actividad=clase["id_actividad"],
                dictada=clase["dictada"]
            )
            operation_result = clase.delete(id=id)
            if (operation_result):
                return jsonify({"message": "Class deleted successfully"}), 200
            else:
                return jsonify({"message": "Error deleting"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
