from model.MySQLScriptsExecutor import MySQLScriptsExecutor
from model.DataFormatter import DataFormatter


class InstructorManager:
    table = "INSTRUCTORES"

    def getInstructorByCi(ci):
        script = """
            SELECT *
            FROM INSTRUCTORES
            WHERE ci = %s
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(
            script=script, params=(ci,))
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None

    def getAllInstructores():
        script = """
            SELECT *
            FROM INSTRUCTORES
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(script=script)
        
        if (data != None):
            return DataFormatter.formatData(data=data)
        else:
            return None
