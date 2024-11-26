from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter
from model.entities.Turno import Turno
from model.entities.Alumno import Alumno
from datetime import datetime

class Clase:
    """
        Representa la entidad Clase.
        
        Nota: Con respecto a las clases, en el día de la fecha, es importante tener en cuenta que un instructor no 
        puede dar 2 clases en el mismo turno y que un alumno no puede estar inscripto en 2 clases 
        distintas en el mismo turno. Además, las clases no pueden ser modificadas ni eliminadas durante 
        el horario de esta, únicamente se pueden alterar antes o después de la misma.
        
        Estado: clase terminada.
    """
    table_name = "CLASES"
    values_needed = ["ci_instructor", "id_turno", "id_actividad"]
    
    def __init__(self, ci_instructor: int, id_turno: int, id_actividad: int, dictada: bool=False):
        self.ci_instructor = ci_instructor
        self.id_turno = id_turno
        self.id_actividad = id_actividad
        self.dictada = dictada

    def insert(self) -> bool:
        """
            Intenta insertar un registro asociado en la tabla.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        if (Clase.can_instructor_assist(self.ci_instructor, self.id_turno)):
            script, params = MySQLScriptGenerator.create_insert_script(
                entity=self,
                table_name=self.table_name
            )
            return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
        else:
            return False

    def update(self, id: int) -> bool:
        """
            Intenta actualizar su registro asociado en la tabla.
            
            Entrada:
                - `id`: id de la clase.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        clase_actual = Clase.get_clase_by_id(id=id)
        if (clase_actual is None):
            return False
        
        if (Clase.can_update_or_delete_clase(clase_actual["id_turno"]) and Clase.can_instructor_assist(self.ci_instructor, self.id_turno)):
            script, params = MySQLScriptGenerator.create_update_script(
                entity=self,
                filter_key="id",
                filter_value=id,
                table_name=self.table_name
            )
            return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
        else:
            return False
    
    def delete(self, id: int) -> bool:
        """
            Intenta eliminar su registro asociado en la tabla.
            
            Entrada:
                - `id`: id de la clase.
            
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        clase_actual = Clase.get_clase_by_id(id=id)
        if (clase_actual is None):
            return False
        
        if (Clase.can_update_or_delete_clase(clase_actual["id_turno"])):
            script, params = MySQLScriptGenerator.create_delete_script(
                filter_key="id",
                filter_value=id,
                table_name=self.table_name
            )
            return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
        else:
            return False
    
    @classmethod
    def get_clase_by_id(cls, id: int) -> dict:
        """
            Retorna los datos de una clase en un diccionario.
            
            Entrada:
                - `id`: id de la clase.
                
            Salida:
                - `None`, si no encontró nada.
                - `duplicated` si encontró más de un registro correspondiente a esa id.
                - un diccionario con la info de la clase
                
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
    def get_all_clases(cls) -> list[dict]:
        """
            Retorna todos los alumnos como una lista de diccionarios, donde cada diccionario contiene la info de una clase.
            
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
        
    @staticmethod
    def can_instructor_assist(ci_instructor: int, id_turno: int) -> bool:
        """
            Dice si un instructor puede dar la clase.
            
            Entradas:
                - `ci_instructor`: cédula de identidad del instructor.
                - `id_turno`: id del turno de la clase a asistir.
                
            Salida:
                - `True` si el instructor puede dar la clase, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script="""
                SELECT *
                FROM CLASES
                WHERE ci_instructor=%s AND id_turno=%s AND dictada=false
            """,
            params=(ci_instructor, id_turno)
        )
        
        if (data is None):
            return True
        else:
            return False
        
    @staticmethod
    def can_update_or_delete_clase(id_turno: int) -> bool:
        """
            Dice si la clase se puede actualizar o eliminar, según la hora actual y la hora de la clase.
            
            Entradas:
                - `id_turno`: id del turno de la clase.
                
            Salida:
                - `True` si la clase se puede actualizar o eliminar, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        # Obtener la hora actual como objeto datetime.time
        hora_actual = datetime.now().time()  

        # Obtener los datos del turno
        turno = Turno.get_turno_by_id(id=id_turno)
        
        if (turno == "duplicated"):
            return False

        # Convertir las horas de inicio y fin del turno en objetos datetime.time
        hora_inicio = datetime.strptime(turno["hora_inicio"], "%H:%M:%S").time()
        hora_fin = datetime.strptime(turno["hora_fin"], "%H:%M:%S").time()

        # Comparar las horas
        if (hora_inicio <= hora_actual <= hora_fin):
            return False
        else:
            return True
