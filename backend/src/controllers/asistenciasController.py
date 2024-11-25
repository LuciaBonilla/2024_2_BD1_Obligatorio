from flask import request, jsonify
from model.entities.Asistencia import Asistencia
from model.Validator import Validator


class AsistenciasController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_asistencias():
        """
            Estado: método terminado.
        """
        try:

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            asistencias = Asistencia.get_all_asistencias()
            if (asistencias is None):
                return jsonify({"message": "Assistances not found"}), 404

            return jsonify(asistencias), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_asistencia_by_id_clase_and_ci_alumno(ci_alumno: int, id_clase: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            asistencia = Asistencia.get_asistencia_by_id_clase_and_ci_alumno(
                ci_alumno=ci_alumno, id_clase=id_clase)
            if (asistencia == None):
                return jsonify({"message": "Assistance not found"}), 404

            if (asistencia == "duplicated"):
                return jsonify({"message": "Assistance duplicated, server can't handle it"}), 500

            return jsonify(asistencia), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_asistencia():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            for field in Asistencia.values_needed:
                if field not in body_request:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            asistencia = Asistencia.get_asistencia_by_id_clase_and_ci_alumno(
                ci_alumno=body_request["ci_alumno"], id_clase=body_request["id_clase"])
            if (asistencia != None):
                return jsonify({"message": "Assistance already created"}), 400

            asistencia = Asistencia(
                ci_alumno=body_request["ci_alumno"],
                id_clase=body_request["id_clase"],
                id_equipamiento=body_request.get("id_equipamiento", None)
            )
            operation_result = asistencia.insert()
            if (operation_result):
                return jsonify({"message": "Assistance created successfully",
                                "id_clase": asistencia.id_clase,
                                "ci_alumno": asistencia.ci_alumno,
                                "id_equipamiento": asistencia.id_equipamiento}), 201
            else:
                return jsonify({"message": "Error creating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_asistencia(ci_alumno: int, id_clase: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            asistencia = Asistencia.get_asistencia_by_id_clase_and_ci_alumno(
                ci_alumno=ci_alumno, id_clase=id_clase)
            if (asistencia == None):
                return jsonify({"message": "Assistance not found"}), 404

            if (asistencia == "duplicated"):
                return jsonify({"message": "Assistance duplicated, server can't handle"}), 500

            asistencia = Asistencia(
                ci_alumno=ci_alumno,
                id_clase=id_clase,
                id_equipamiento=body_request["id_equipamiento"] if "id_equipamiento" in body_request else asistencia["id_equipamiento"],
            )
            operation_result = asistencia.update()
            if (operation_result):
                return jsonify({"message": "Assistance updated successfully",
                                "id_clase": asistencia.id_clase,
                                "ci_alumno": asistencia.ci_alumno,
                                "id_equipamiento": asistencia.id_equipamiento
                                }), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_asistencia(ci_alumno: int, id_clase: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            asistencia = Asistencia.get_asistencia_by_id_clase_and_ci_alumno(
                ci_alumno=ci_alumno, id_clase=id_clase)
            if (asistencia == None):
                return jsonify({"message": "Assistance not found"}), 404

            if (asistencia == "duplicated"):
                return jsonify({"message": "Assistance duplicated, server can't handle it"}), 500

            asistencia = Asistencia(
                ci_alumno=ci_alumno,
                id_clase=id_clase,
                id_equipamiento=body_request["id_equipamiento"] if "id_equipamiento" in body_request else asistencia["id_equipamiento"],
            )
            operation_result = asistencia.delete()
            if (operation_result):
                return jsonify({"message": "Assistance deleted successfully"}), 200
            else:
                return jsonify({"message": "Error deleting"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
