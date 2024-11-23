from flask import request, jsonify, json, current_app
from model.entities.Instructor import Instructor
from model.Validator import Validator

class InstructoresController:
    @staticmethod
    def get_all_instructores(): 
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            
            if (is_admin):
                instructors = Instructor.get_all_instructores()
                if (instructors != None):
                    return jsonify(instructors), 200
                else:
                    return jsonify({"message": "No instructors found"}), 404
            else:
                return jsonify({"message": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_instructor_by_ci(ci: int):
        try:
            body_request = request.get_json() # Da un diccionario.

            is_admin = Validator.is_admin(body_request=body_request)
            
            if (is_admin):
                instructor = Instructor.get_instructor_by_ci(ci=ci)
                if (instructor != None):
                    if (instructor != "duplicated"):
                        return jsonify(instructor), 200
                    else:
                        return jsonify({"message": "Instructor duplicated, server can't handle it"}), 500
                else:
                    return jsonify({"message": "Instructor not found"}), 404
            else:
                return jsonify({"message": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_instructor():
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            
            if (is_admin):
                for field in Instructor.values_needed:
                    if field not in body_request:
                        return jsonify({"error": f"Missing field: {field}"}), 400

                instructor = Instructor.get_instructor_by_ci(ci=body_request["ci"])
                if (instructor is None):
                    instructor = Instructor(
                        ci=body_request["ci"],
                        nombre=body_request["nombre"],
                        apellido=body_request["apellido"],
                        telefono_contacto=body_request["telefono_contacto"],
                        correo_contacto=body_request.get("correo_contacto", None)
                    )
                    operation_result = instructor.insert()
                    if (operation_result):
                        return jsonify({"message": "Instructor created successfully"}), 201
                    else:
                        return jsonify({"message": "Error creating"}), 400
                else:
                    return jsonify({"message": "Instructor already created"}), 400
            else:
                return jsonify({"message": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def update_instructor(ci: int):
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            
            if (is_admin):
                instructor = Instructor.get_instructor_by_ci(ci=ci)
                if (instructor != None):
                    if (instructor != "duplicated"):
                        instructor = Instructor(
                            ci=ci,
                            nombre=body_request["nombre"] if "nombre" in body_request else instructor["nombre"],
                            apellido=body_request["apellido"] if "apellido" in body_request else instructor["apellido"],
                            telefono_contacto=body_request["telefono_contacto"] if "telefono_contacto" in body_request else instructor["telefono_contacto"],
                            correo_contacto=body_request["correo_contacto"] if "correo_contacto" in body_request else instructor["correo_contacto"]
                        )
                        operation_result = instructor.update()
                        if (operation_result):
                            return jsonify({"message": "Instructor updated successfully"}), 200
                        else:
                            return jsonify({"message": "Error updating"}), 400
                    else:
                        return jsonify({"message": "Instructor duplicated, server can't handle"}), 500
                else:
                    return jsonify({"message": "Instructor not found"}), 404
            else:
                return jsonify({"message": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_instructor(ci: int):
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(body_request=body_request)
            
            if (is_admin):
                instructor = Instructor.get_instructor_by_ci(ci=ci)
                if (instructor != None):
                    if (instructor != "duplicated"):
                        instructor = Instructor(
                            ci=ci,
                            nombre=body_request["nombre"] if "nombre" in body_request else instructor["nombre"],
                            apellido=body_request["apellido"] if "apellido" in body_request else instructor["apellido"],
                            telefono_contacto=body_request["telefono_contacto"] if "telefono_contacto" in body_request else instructor["telefono_contacto"],
                            correo_contacto=body_request["correo_contacto"] if "correo_contacto" in body_request else instructor["correo_contacto"]
                        )
                        operation_result = instructor.delete()
                        if (operation_result):
                            return jsonify({"message": "Instructor deleted successfully"}), 200
                        else:
                            return jsonify({"message": "Error deleting"}), 400
                    else:
                        return jsonify({"message": "Instructor duplicated, server can't handle it"}), 500
                else:
                    return jsonify({"message": "Instructor not found"}), 404
            else:
                return jsonify({"message": "Unauthorized"}), 401
        except Exception as e:
            return jsonify({"error": str(e)}), 500
