from flask import request, jsonify, json, current_app
from model.entities.Alumno import Alumno
from model.Validator import Validator

class AlumnosController:
    """
        Estado: controlador terminado.
    """
    @staticmethod
    def get_all_alumnos():
        """
            Estado: método terminado.
        """
        try:
            # body_request = request.get_json() # Da un diccionario.
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
            
            alumnos = Alumno.get_all_alumnos()
            if (alumnos is None):
                return jsonify({"message": "No students found"}), 404
                
            return jsonify(alumnos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_alumno_by_ci(ci: int):
        """
            Estado: método terminado.
        """
        try:
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            alumno = Alumno.get_alumno_by_ci(ci=ci)
            if (alumno == None):
                return jsonify({"message": "Student not found"}), 404
                
            if (alumno == "duplicated"):
                return jsonify({"message": "Student duplicated, server can't handle it"}), 500
            
            return jsonify(alumno), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def create_alumno():
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            for field in Alumno.values_needed:
                if field not in body_request:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            alumno = Alumno.get_alumno_by_ci(ci=body_request["ci"])
            if (alumno != None):
                return jsonify({"message": "Student already created"}), 400
                
            alumno = Alumno(
                ci=body_request["ci"],
                nombre=body_request["nombre"],
                apellido=body_request["apellido"],
                fecha_nacimiento=body_request["fecha_nacimiento"],
                telefono_contacto=body_request["telefono_contacto"],
                correo_contacto=body_request.get("correo_contacto", None)
            )
            operation_result = alumno.insert()
            if (operation_result):
                return jsonify({"message": "Student created successfully", "ci": alumno.ci}), 201
            else:
                return jsonify({"message": "Error creating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def update_alumno(ci: int):
        """
            Estado: método terminado.
        """
        try:
            body_request = request.get_json()
            
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            alumno = Alumno.get_alumno_by_ci(ci=ci)
            if (alumno == None):
                return jsonify({"message": "Student not found"}), 404
            
            if (alumno == "duplicated"):
                return jsonify({"message": "Student duplicated, server can't handle"}), 500
                
            alumno = Alumno(
                ci=ci,
                nombre=body_request["nombre"] if "nombre" in body_request else alumno["nombre"],
                apellido=body_request["apellido"] if "apellido" in body_request else alumno["apellido"],
                fecha_nacimiento=body_request["fecha_nacimiento"] if "fecha_nacimiento" in body_request else alumno["fecha_nacimiento"],
                telefono_contacto=body_request["telefono_contacto"] if "telefono_contacto" in body_request else alumno["telefono_contacto"],
                correo_contacto=body_request["correo_contacto"] if "correo_contacto" in body_request else alumno["correo_contacto"]
            )
            operation_result = alumno.update()
            if (operation_result):
                return jsonify({"message": "Student updated successfully", "ci": alumno.ci}), 200
            else:
                return jsonify({"message": "Error updating"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def delete_alumno(ci: int):
        """
            Estado: método terminado.
        """
        try:
            
            is_admin = Validator.is_admin(headers=request.headers)
            if (not is_admin):
                return jsonify({"message": "Unauthorized"}), 401
                
            alumno = Alumno.get_alumno_by_ci(ci=ci)
            if (alumno == None):
                return jsonify({"message": "Student not found"}), 404
                
            if (alumno == "duplicated"):
                return jsonify({"message": "Student duplicated, server can't handle it"}), 500
                    
            alumno = Alumno(
                ci=ci,
                nombre=alumno["nombre"],
                apellido=alumno["apellido"],
                fecha_nacimiento=alumno["fecha_nacimiento"],
                telefono_contacto=alumno["telefono_contacto"],
                correo_contacto=alumno["correo_contacto"]
            )
            operation_result = alumno.delete()
            if (operation_result):
                return jsonify({"message": "Student deleted successfully"}), 200
            else:
                return jsonify({"message": "Error deleting"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
