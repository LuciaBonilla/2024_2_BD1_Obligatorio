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
    
    def __init__(self, ci: int, nombre: str, apellido: str, telefono_contacto: str, correo_contacto: str =None):
        self.ci = ci
        self.nombre = nombre
        self.apellido = apellido
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto

    def insert(self) -> bool:
        script, params = MySQLScriptGenerator.create_insert_script(
            entity=self,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)

    def update(self) -> bool:
        script, params = MySQLScriptGenerator.create_update_script(
            entity=self,
            filter_key="ci",
            filter_value=self.ci,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
    
    def delete(self) -> bool:
        script, params = MySQLScriptGenerator.create_delete_script(
            filter_key="ci",
            filter_value=self.ci,
            table_name=Instructor.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
    
    @staticmethod
    def get_instructor_by_ci(ci: int) -> dict:
        """
            Retorna los datos de un instructor en un diccionario.
            
            Entrada:
                - `ci`: cédula de identidad.
                
            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa cédula.
                - un diccionario con la info del instructor
                
            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_select_all_columns_script(
            filter_key="ci",
            filter_value=ci,
            table_name=Instructor.table_name
        )
        data = MySQLScriptRunner.run_script_to_query_database(script=script, params=params)
        if (data is None):
            return None
        elif (len(data) == 1):
            formmatedData = DataFormatter.format_data(data=data)
            return formmatedData[0]
        else: # Si encuentra más de un registro, entonces retorna un string de indicación.
            return "duplicated"
    
    @staticmethod
    def get_all_instructores() -> list[dict]:
        """
            Retorna todos los instructores como una lista de diccionarios, donde cada diccionario contiene la info de un instructor.
            
            Salida:
                - `None` si no encuentra nada, en caso contrario, la lista de diccionarios.
                
            Estado: método terminado.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script=f"SELECT * FROM {Instructor.table_name}"
        )
        if (data is None):
            return None
        else:
            return DataFormatter.format_data(data=data)