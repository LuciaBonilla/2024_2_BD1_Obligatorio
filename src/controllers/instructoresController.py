from flask import request, jsonify
from model.Instructor import Instructor
from model.InstructorManager import InstructorManager
from model.DataFormatter import DataFormatter

class instructoresController:
    @staticmethod
    def getInstructorByCi(ci):
        try:
            instructor = InstructorManager.getInstructorByCi(ci)
            if (instructor != None):
                return jsonify(instructor), 200
            else:
                return jsonify({"message": "Instructor not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def getAllInstructores(): 
        try:
            data = InstructorManager.getAllInstructores()
            if (data != None):
                return jsonify(data), 200
            else:
                return jsonify({"message": "No instructors found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @staticmethod
    def updateInstructor(ci, request):
        try:
            data = request.get_json()
            instructor = InstructorManager.getInstructorByCi(ci)
            if (instructor != None):
                instructor = Instructor(
                    ci=ci,
                    nombre=data["nombre"] if "nombre" in data else instructor["nombre"],
                    apellido=data["apellido"] if "apellido" in data else instructor["apellido"],
                    telefono_contacto=data["telefono_contacto"] if "telefono_contacto" in data else instructor["telefono_contacto"],
                    correo_contacto=data["correo_contacto"] if "correo_contacto" in data else instructor["correo_contacto"]
                )
                result = instructor.save()
                
                if result:
                    return jsonify({"message": "Instructor updated successfully"}), 200
                else:
                    return jsonify({"message": "Error making the querie"}), 400
            else:
                return jsonify({"message": "Instructor not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def createInstructor(request):
        try:
            data = request.get_json()
            for field in Instructor.values_needed:
                if field not in data:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            instructor = Instructor(
                ci=data["ci"],
                nombre=data["nombre"],
                apellido=data["apellido"],
                telefono_contacto=data["telefono_contacto"],
                correo_contacto=data.get("correo_contacto", None)
            )
            result = instructor.save()
            if result:
                return jsonify({"message": "Instructor created successfully"}), 201
            else:
                return jsonify({"message": "Error making the querie"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
