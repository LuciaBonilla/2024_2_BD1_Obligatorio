from flask import request, jsonify
from model.entities.Instructor import Instructor
from model.Validator import Validator


class InstructoresController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_instructores():
        """
            Estado: método terminado.
        """
        try:

            is_admin = Validator.is_admin(headers=request.headers)
            if not is_admin:
                return jsonify({"message": "Unauthorized"}), 401

            instructores = Instructor.get_all_instructores()
            if instructores is None:
                return jsonify({"message": "Instructors not found"}), 404

            return jsonify(instructores), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_instructor_by_ci(ci: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            instructor = Instructor.get_instructor_by_ci(ci=ci)
            if (instructor == None):
                return jsonify({"message": "Instructor not found"}), 404

            if (instructor == "duplicated"):
                return jsonify({"message": "Instructor duplicated, server can't handle it"}), 500

            return jsonify(instructor), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_instructor():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            for field in Instructor.values_needed:
                if field not in body_request:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            instructor = Instructor.get_instructor_by_ci(
                ci=body_request["ci"])

            if (instructor != None):
                return jsonify({"message": "Instructor already created", "instructor": instructor}), 400

            instructor = Instructor(
                ci=body_request["ci"],
                nombre=body_request["nombre"],
                apellido=body_request["apellido"],
                telefono_contacto=body_request["telefono_contacto"],
                correo_contacto=body_request.get("correo_contacto", None)
            )

            operation_result = instructor.insert()
            if (operation_result):
                return jsonify({"message": "Instructor created successfully", "ci": instructor.ci}), 201
            else:
                return jsonify({"message": "Error creating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def update_instructor(ci: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()

            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            instructor = Instructor.get_instructor_by_ci(ci=ci)
            if (instructor == None):
                return jsonify({"message": "Instructor not found"}), 404

            if (instructor == "duplicated"):
                return jsonify({"message": "Instructor duplicated, server can't handle it"}), 500

            instructor = Instructor(
                ci=ci,
                nombre=body_request["nombre"] if "nombre" in body_request else instructor["nombre"],
                apellido=body_request["apellido"] if "apellido" in body_request else instructor["apellido"],
                telefono_contacto=body_request["telefono_contacto"] if "telefono_contacto" in body_request else instructor["telefono_contacto"],
                correo_contacto=body_request["correo_contacto"] if "correo_contacto" in body_request else instructor["correo_contacto"]
            )
            operation_result = instructor.update()
            if (operation_result):
                return jsonify({"message": "Instructor updated successfully", "ci": ci}), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_instructor(ci: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401

            instructor = Instructor.get_instructor_by_ci(ci=ci)
            if (instructor == None):
                return jsonify({"message": "Instructor not found"}), 404

            if (instructor == "duplicated"):
                return jsonify({"message": "Instructor duplicated, server can't handle it"}), 500

            instructor = Instructor(
                ci=ci,
                nombre=instructor["nombre"],
                apellido=instructor["apellido"],
                telefono_contacto=instructor["telefono_contacto"],
                correo_contacto=instructor["correo_contacto"]
            )
            operation_result = instructor.delete()
            if (operation_result):
                return jsonify({"message": "Instructor deleted successfully"}), 200
            else:
                return jsonify({"message": "Error deleting"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
