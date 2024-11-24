from model.MySQLScriptRunner import MySQLScriptRunner
from utils.MySQLScriptGenerator import MySQLScriptGenerator
from utils.DataFormatter import DataFormatter
from model.entities.Turno import Turno
from model.entities.Alumno import Alumno
from datetime import datetime
from model.entities.Clase import Clase
from model.entities.Actividad import Actividad

class Asistencia:
    """
        Representa la entidad Asistencia.
        
        Nota: La asistencia indica que el alumno se anotó para asistir a tal clase no dictada, o bien, que ya asitió a una clase dictada.
        
        Nota: La asistencia se puede borrar porque un alumno puede cancelar su asistencia.
        
        Nota: La asistencia se puede modificar porque un alumno puede cambiar el equipamiento usado.
        
        Nota: Con respecto a las clases, en el día de la fecha, es importante tener en cuenta que un instructor no 
        puede dar 2 clases en el mismo turno y que un alumno no puede estar inscripto en 2 clases 
        distintas en el mismo turno. Además, las clases no pueden ser modificadas ni eliminadas durante 
        el horario de esta, únicamente se pueden alterar antes o después de la misma.
        
        Nota: Tener en cuenta restricción de edad de las actividades.
        
        Estado: clase terminada.
    """
    table_name = "ALUMNOS_CLASES"
    values_needed = ["id_clase", "ci_alumno"]
    
    def __init__(self, id_clase: int, ci_alumno: int, id_equipamiento: int=None):
        self.id_clase = id_clase
        self.ci_alumno = ci_alumno
        self.id_equipamiento = id_equipamiento

    def insert(self) -> bool:
        """
            Intenta insertar un registro asociado en la tabla.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        if (Asistencia.can_insert_update_or_delete_assistances(id_clase=self.id_clase) and
                Asistencia.can_alumno_assist(ci_alumno=self.ci_alumno, id_clase=self.id_clase)): # Puedo insertar asistencia relacionada a la clase?
            script, params = MySQLScriptGenerator.create_insert_script(
                entity=self,
                table_name=self.table_name
            )
            return MySQLScriptRunner.run_script_to_modify_database(script=script, params=params)
        else:
            return False

    def update(self) -> bool:
        """
            Intenta actualizar un registro asociado en la tabla.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        if (Asistencia.can_insert_update_or_delete_assistances(id_clase=self.id_clase) and
                Asistencia.can_alumno_assist(ci_alumno=self.ci_alumno, id_clase=self.id_clase)): # Puedo actualizar asistencia relacionada a la clase?
            return MySQLScriptRunner.run_script_to_modify_database(
                script=f"""
                    UPDATE {self.table_name}
                    SET ci_alumno = %s AND id_clase = %s AND id_equipamiento = %s
                    WHERE ci_alumno = %s AND id_clase = %s
                """,
                params=(self.ci_alumno, self.id_clase, self.id_equipamiento, self.ci_alumno, self.id_clase)
            )
        else:
            return False
    
    def delete(self) -> bool:
        """
            Intenta eliminar un registro asociado en la tabla.
            
            Entrada:
                - `id`: id de la asistencia.
                
            Salida:
                - `True` si la operación fue exitosa, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        if (Asistencia.can_insert_update_or_delete_assistances(id_clase=self.id_clase)): # Puedo borrar asistencia relacionada a la clase?
            return MySQLScriptRunner.run_script_to_modify_database(
                script=f"""
                    DELETE FROM {self.table_name}
                    WHERE ci_alumno = %s AND id_clase = %s
                """,
                params=(self.ci_alumno, self.id_clase)
            )
        else:
            return False
    
    @classmethod
    def get_asistencia_by_id_clase_and_ci_alumno(cls, ci_alumno: int, id_clase: int) -> dict:
        """
            Retorna los datos de la asistencia a una clase en un diccionario.
            
            Entrada:
                - `id_clase`: id de la clase relacionada a la asistencia.
                - `ci_alumno`: cédula de identidad del alumno.
                
            Salida:
                - `None`, si no encontró nada.
                - una diccionario con la info de la asistencia.
                
            Estado: método terminado.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script=f"""
                SELECT *
                FROM {cls.table_name}
                WHERE ci_alumno = %s AND id_clase = %s
            """,
            params=(ci_alumno, id_clase)
        )
        if (data is None):
            return None
        elif (len(data) == 1):
            data = DataFormatter.format_data(data=data)
            return data[0]
        else: # Si encuentra más de un registro, entonces retorna un string de indicación.
            return "duplicated"
    
    @classmethod
    def get_all_asistencias(cls) -> list[dict]:
        """
            Retorna todas las asistencias como una lista de diccionarios, donde cada diccionario contiene la info de una asistencia.
            
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
    def can_alumno_assist(ci_alumno: int, id_clase: int) -> bool:
        """
            Dice si un alumno puede ir a la clase.
            
            Entradas:
                - `ci_alumno`: cédula de identidad del alumno.
                - `id_clase`: id de la clase a asistir.
                
            Salida:
                - `True` si el alumno puede ir a la clase, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        clase_to_assist = Clase.get_clase_by_id(id=id_clase)
        if (clase_to_assist is None or clase_to_assist == "duplicated"):
            return False
        
        # Verifica si el alumno cumple la restricción de edad.
        actividad = Actividad.get_actividad_by_id(clase_to_assist["id_actividad"])
        if (actividad is None or actividad == "duplicated"):
            return False
        
        alumno = Alumno.get_alumno_by_ci(ci=ci_alumno)
        if (alumno is None or alumno == "duplicated"):
            return False

        restriccion_edad = actividad["edad_minima"]
        fecha_nacimiento=alumno["fecha_nacimiento"]
        edad_alumno = Asistencia.__calcular_edad(fecha_nacimiento)
        if edad_alumno < restriccion_edad:
            return False
        
        # Verifica si el alumno no está en otra clase en el mismo turno.
        asistencias = MySQLScriptRunner.run_script_to_query_database(
            script="""
                SELECT *
                FROM ALUMNOS_CLASES
                WHERE ci_alumno=%s
            """,
            params=(ci_alumno,)
        )
        
        if (asistencias is None):
            return True

        can_assist=True
        # Busca clases no dictadas donde el estudiante esté y que la clase esté en el mismo turno que la clase a asistir. Si encuentra, entonces no puede asistir.
        for asistencia in asistencias:
            clase = Clase.get_clase_by_id(id=asistencia["id_clase"])
            if (clase == "duplicated"):
                return False
            if (clase != None):
                if (clase["id_turno"] == clase_to_assist["id_turno"]) and (clase["dictada"]==False): 
                    return False
        return can_assist
        
    @staticmethod
    def can_insert_update_or_delete_assistances(id_clase: int) -> bool:
        """
            Dada la clase, si está en curso, no se podrá insertar o modificar asistencias para esa clase.
            
            Entrada:
                `id_clase`: id de la clase asociada a la asistencia.
                
            Salida:
                `True` si se puede modificar asistencias, en caso contrario, `False`
                
            Estado: método terminado.
        """
        # Obtener la hora actual como objeto datetime.time.
        hora_actual = datetime.now().time()  

        # La clase de la asistencia asociada.
        clase = Clase.get_clase_by_id(id=id_clase)
        
        if (clase is None or clase == "duplicated"):
            return False
        
        # Turno de la clase de la asistencia asociada.
        clase_turno = Turno.get_turno_by_id(id=clase["id_turno"])
        
        if (clase_turno is None or clase_turno == "duplicated"):
            return False
        
        # Convertir las horas de inicio y fin del turno en objetos datetime.time
        clase_hora_inicio = datetime.strptime(clase_turno["hora_inicio"], "%H:%M:%S").time()
        clase_hora_fin = datetime.strptime(clase_turno["hora_fin"], "%H:%M:%S").time()

        # Comparar las horas.
        if (clase_hora_inicio <= hora_actual <= clase_hora_fin):
            return False
        else:
            return True
        
    @staticmethod
    def __calcular_edad(fecha_nacimiento: str) -> int:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        fecha_actual = datetime.now()
        # Calcular la edad
        edad = fecha_actual.year - fecha_nacimiento.year
        # Ajustar si el cumpleaños aún no ha ocurrido este año
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        return edad