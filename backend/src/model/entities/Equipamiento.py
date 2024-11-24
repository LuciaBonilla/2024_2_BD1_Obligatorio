from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter

class Equipamiento:
    """
        Representa la entidad Equipamiento.
        
        Estado: clase terminada.
    """
    table_name = "EQUIPAMIENTOS"
    
    @classmethod
    def get_equipamiento_by_id(cls, id: int) -> dict:
        """
            Retorna los datos de un equipamiento en un diccionario.
            
            Entrada:
                - `id`: id del equipamiento.
                
            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa id.
                - un diccionario con la info del equipamiento.
                
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
    def get_all_equipamientos(cls) -> list[dict]:
        """
            Retorna todos los equipamientos como una lista de diccionarios, donde cada diccionario contiene la info de un equipamiento.
            
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