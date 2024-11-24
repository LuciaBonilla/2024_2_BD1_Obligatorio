from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter

class Turno:
    """
        Representa la entidad Turno.
        
        Estado: clase terminada.
    """
    table_name = "TURNOS"
    values_needed = ["hora_inicio", "hora_fin"]
    
    def __init__(self, hora_inicio: str, hora_fin: str):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

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

    def update(self, id: int) -> bool:
        """
            Intenta actualizar un registro asociado en la tabla.
            
            Entrada:
                - `id`: id del turno.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_update_script(
            entity=self,
            filter_key="id",
            filter_value=id,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
    
    def delete(self, id: int) -> bool:
        """
            Intenta eliminar un registro asociado en la tabla.
            
            Entrada:
                - `id`: id del turno.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_delete_script(
            filter_key="id",
            filter_value=id,
            table_name=self.table_name
        )
        return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
    
    @classmethod
    def get_turno_by_id(cls, id: int) -> dict:
        """
            Retorna los datos de un turno en un diccionario.
            
            Entrada:
                - `id`: id del turno.
                
            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa id.
                - un diccionario con la info del turno.
                
            Estado: método terminado.
        """
        script, params = MySQLScriptGenerator.create_select_all_columns_script(
            filter_key="id",
            filter_value=id,
            table_name=cls.table_name
        )
        data = MySQLScriptRunner.run_script_to_query_database(script=script, params=params)
        if (data is None):
            return None
        elif (len(data) == 1):
            data = DataFormatter.format_data(data=data)
            return data[0]
        else: # Si encuentra más de un registro, entonces retorna un string de indicación.
            return "duplicated"
    
    @classmethod
    def get_all_turnos(cls) -> list[dict]:
        """
            Retorna todos los turnos como una lista de diccionarios, donde cada diccionario contiene la info de un turno.
            
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