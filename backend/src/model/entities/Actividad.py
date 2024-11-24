from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter

class Actividad:
    """
        Representa la entidad Actividad.
        
        Estado: clase terminada.
    """
    table_name = "ACTIVIDADES"
    values_needed = ["nombre", "costo", "edad_minima"]
    
    def __init__(self, nombre: str, costo: int, edad_minima: int, descripcion: str =None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.edad_minima = edad_minima

    def update(self, id: int) -> bool:
        """
            Intenta actualizar su registro asociado en la tabla.
            
            Entrada:
                - `id`: id de la actividad.
                
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
    
    @classmethod
    def get_actividad_by_id(cls, id: int) -> dict:
        """
            Retorna los datos de una actividad en un diccionario.
            
            Entrada:
                - `id`: id de la actividad.
                
            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa id.
                - un diccionario con la info de la actividad.
                
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
    def get_all_actividades(cls) -> list[dict]:
        """
            Retorna todos las actividades como una lista de diccionarios, donde cada diccionario contiene la info de una actividad.
            
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