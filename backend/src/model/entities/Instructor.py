from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter

class Instructor:
    """
        Representa la entidad Instructor.

        Estado: clase terminada.
    """
    table_name = "INSTRUCTORES"
    values_needed = ["ci", "nombre", "apellido", "telefono_contacto"]

    def __init__(self, ci: int, nombre: str, apellido: str, telefono_contacto: str, correo_contacto: str = None):
        self.ci = int(ci)
        self.nombre = nombre
        self.apellido = apellido
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto

    def insert(self) -> bool:
        """
            Intenta insertar un registro asociado en la tabla.

            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.

            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_insert_script(
            entity=self,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)

    def update(self) -> bool:
        """
            Intenta actualizar un registro asociado en la tabla.

            Nota: el atributo de filtrado es `ci`.

            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.

            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_update_script(
            entity=self,
            filter_key="ci",
            filter_value=self.ci,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)

    def delete(self) -> bool:
        """
            Intenta eliminar un registro asociado en la tabla.

            Nota: el atributo de filtrado es `ci`.

            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.

            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_delete_script(
            filter_key="ci",
            filter_value=self.ci,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)

    @classmethod
    def get_instructor_by_ci(cls, ci: int) -> dict:
        """
            Retorna los datos de un instructor en un diccionario.

            Entrada:
                - `ci`: cédula de identidad.

            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa cédula.
                - un diccionario con la info del instructor.

            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_select_all_columns_script(
            filter_key="ci",
            filter_value=ci,
            table_name=cls.table_name
        )

        data = MySQLScriptRunner.run_script_to_query_database(
            script=script, params=params)
        if (data is None):
            return None
        elif (len(data) == 1):
            data = DataFormatter.format_data(data=data)
            return data[0]
        else:  # Si encuentra más de un registro, entonces retorna un string de indicación.
            return "duplicated"

    @classmethod
    def get_all_instructores(cls) -> list[dict]:
        """
            Retorna todos los instructores como una lista de diccionarios, donde cada diccionario contiene la info de un instructor.

            Salida:
                - `None` si no encuentra nada, en caso contrario, la lista de diccionarios.

            Estado: método terminado.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script=f"SELECT * FROM {cls.table_name}"
        )
        if (data is None):
            return None
        else:
            return DataFormatter.format_data(data=data)

    def __str__(self) -> str:
        return f"Instructor(ci={self.ci}, nombre={self.nombre}, apellido={self.apellido}, telefono_contacto={self.telefono_contacto}, correo_contacto={self.correo_contacto})"
