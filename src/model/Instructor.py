# - **Endpoints:**
#     - `GET /api/Instructores`: Retrieve all instructors.
#     - `GET /api/Instructores/<int:id>`: Retrieve a single instructor by CI.
#     - `POST /api/Instructores: Create a new instructor.
#     - `PUT /api/Instructores/<int:id>`: Update an existing instructor by CI.
#     - `DELETE /api/Instructores/<int:id>`: Delete an instructor by CI.
from model.MySQLScriptsExecutor import MySQLScriptsExecutor
from utils.utilSql import utilSql
from flask import current_app


class Instructor:
    table = "INSTRUCTORES"
    values_needed = ["ci", "nombre", "apellido",
                     "telefono_contacto"]

    def __init__(self, ci, nombre, apellido, telefono_contacto, correo_contacto=None):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto

    def save(self) -> bool:
        """Search in the db if the instructor already exists, if not, insert it
        or update the existing one.
        """
        script = """
            SELECT *
            FROM INSTRUCTORES
            WHERE ci = %s
        """
        data = MySQLScriptsExecutor.runScriptToQueryDatabase(
            script=script, params=(self.ci,))
        if (data != None):
            return self.update()
        else:
            current_app.logger.info(f"Data from instructor: {data}")
            return self.insert()

    def insert(self) -> bool:
        current_app.logger.info(f"Inserting new instructor: {self.__dict__}")
        atributesName = utilSql.getNewAttributesValues(entity=self)
        current_app.logger.info(f"Inserting new instructor: {atributesName}")
        
        script = utilSql.createInsertQuery(
            entity=self,
            tableName=self.table
        )
        return MySQLScriptsExecutor.runScriptToModifyDatabase(script=script, params=atributesName)

    def update(self, filterKey="ci") -> bool:
        script, params = utilSql.createUpdateQuery(
            value_to_insert=self,
            filterKey=filterKey,
            tableName=self.table,
        )
        return MySQLScriptsExecutor.runScriptToModifyDatabase(script=script, params=params)
