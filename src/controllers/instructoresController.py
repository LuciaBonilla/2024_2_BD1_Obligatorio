from flask import request, jsonify
from model.Instructor import Instructor
from model.InstructorManager import InstructorManager
from model.DataFormatter import DataFormatter

class instructoresController:

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
    def createInstructor(request):
        try:
            data = request.get_json()
            required_fields = ["ci", "nombre", "apellido",
                               "telefono_contacto", "correo_contacto"]

            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing field: {field}"}), 400

            instructor = Instructor(
                ci=data["ci"],
                nombre=data["nombre"],
                apellido=data["apellido"],
                telefono_contacto=data["telefono_contacto"],
                correo_contacto=data["correo_contacto"]
            )
            result = instructor.save()
            if result:
                return jsonify({"message": "Instructor created successfully"}), 201
            else:
                return jsonify({"message": "Error making the querie"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
