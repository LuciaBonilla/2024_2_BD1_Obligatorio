from model.UCUSnowSportsSchoolQuerier import UCUSnowSportsSchoolQuerier
from flask import jsonify

class ActividadesController:
    @staticmethod
    def getAllActividades():
        """
        Llama al método del modelo para obtener todas las actividades y devuelve los datos formateados.
        """
        actividades = UCUSnowSportsSchoolQuerier.getAllActividades()
        if (actividades is not None):
            return jsonify(actividades), 200
        else:
            return jsonify({"message": "No se encontraron actividades."}), 200

    @staticmethod
    def createActividad(request):
        """
        Llama al método del modelo para insertar una nueva actividad en la base de datos.
        """
        nombre = request.json.get("nombre")
        descripcion = request.json.get("descripcion")
        costo = request.json.get("costo")
        edad_minima = request.json.get("edad_minima")

        if (not nombre or not costo or not edad_minima):
            return jsonify({"message": "Faltan datos obligatorios."}), 400
        
        result = UCUSnowSportsSchoolQuerier.insertActividad(
            nombre=nombre,
            descripcion=descripcion,
            costo=costo,
            edad_minima=edad_minima
        )
        
        if result:
            return jsonify({"message": "Actividad creada exitosamente."}), 201
        else:
            return jsonify({"message": "Error al crear la actividad."}), 400