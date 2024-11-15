from model.MySQLScriptsExecutor import MySQLScriptsExecutor
from model.DataFormatter import DataFormatter


class InstructorManager:
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
