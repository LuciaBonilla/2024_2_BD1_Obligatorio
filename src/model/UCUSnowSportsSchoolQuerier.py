from .MySQLScriptsExecutor import MySQLScriptsExecutor
from .DataFormatter import DataFormatter

"""
Responsabilidad: Enviar consultas MySQL a MySQLScriptsExecutor para interactuar con la base de datos "ucu_snow_sports".
Puede retornar la información consultada o retornar el resultado de una operación de modificación a la base.
"""
class UCUSnowSportsSchoolQuerier:
    def getAllAlumnos():
        script = """
            SELECT *
            FROM ALUMNOS
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
    
    def getAllActividades():
        script = """
            SELECT *
            FROM ACTIVIDADES
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
    
    def getAllEquipamientos():
        script = """
            SELECT *
            FROM EQUIPAMIENTOS
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
    
    def getAllTurnos():
        script = """
            SELECT *
            FROM TURNOS
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
    
    def getAllClases():
        script = """
            SELECT *
            FROM CLASES
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
    
    def getAllAsistenciasAClases():
        script = """
            SELECT *
            FROM ALUMNOS_CLASES
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
        
    def insertActividad(nombre, descripcion, costo, edad_minima):
        if (descripcion is None):
            script = """
                INSERT INTO ACTIVIDADES (nombre, costo, edad_minima)
                VALUES (%s, %s, %s)
            """
            params = (nombre, costo, edad_minima)
        else:
            script = """
                INSERT INTO ACTIVIDADES (nombre, descripcion, costo, edad_minima)
                VALUES (%s, %s, %s, %s)
            """
            params = (nombre, descripcion, costo, edad_minima)

        return MySQLScriptsExecutor.runScriptToModifyDatabase(script=script, params=params)