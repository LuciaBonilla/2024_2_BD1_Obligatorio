from model.MySQLScriptRunner import MySQLScriptRunner
from utils.DataFormatter import DataFormatter

class ReportMaker:
    """
        Clase que entrega los datos referidos a estas consultas:
            - Actividades que más ingresos generan – se debe sumar el costo de equipamiento.
            - Actividades con más alumnos.
            - Los turnos más con más clases dictadas.
            
        Estado: clase terminada.
    """
    
    @staticmethod
    def get_most_profitable_activities() -> list[dict]:
        """
            Se consulta: Actividades que más ingresos generan – se debe sumar el costo de equipamiento.
            
            Nota: Sólo se toman ingresos según las asistencias (confirmadas o en curso) a las clases.
            
            Nota: No se muestran actividades que no han generado ningún ingreso.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            # No hay problema en poner a.nombre en en SELECT y agrupar por id porque a.nombre es único al igual que la id.
            script="""
                SELECT
                    a.nombre AS actividad,
                    SUM(a.costo) AS ganancias_sin_equipamiento,
                    SUM(IFNULL(e.costo, 0)) AS ganancias_por_equipamiento,
                    SUM(a.costo + IFNULL(e.costo, 0)) AS ganancias_totales
                FROM 
                    ALUMNOS_CLASES AS ac
                LEFT JOIN
                    CLASES AS c ON ac.id_clase = c.id
                LEFT JOIN
                    EQUIPAMIENTOS AS e ON ac.id_equipamiento = e.id
                LEFT JOIN
                    ACTIVIDADES AS a ON c.id_actividad = a.id
                GROUP BY
                    a.id
                ORDER BY
                    ganancias_totales DESC
            """
        )
        if (data is None):
            return None
        
        return DataFormatter.format_data(data)
    
    @staticmethod
    def get_most_populate_schedules() -> list[dict]:
        """
            Se consulta: Los turnos con más clases dictadas.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script="""
                SELECT
                    t.id AS id_turno,
                    t.hora_inicio AS hora_inicio,
                    t.hora_fin AS hora_fin,
                    COUNT(c.id) AS num_clases_dictadas
                FROM 
                    CLASES AS c
                LEFT JOIN
                    TURNOS AS t ON c.id_turno = t.id
                WHERE
                    c.dictada = true
                GROUP BY
                    t.id
                ORDER BY
                    num_clases_dictadas DESC
            """
        )
        if (data is None):
            return None
        return DataFormatter.format_data(data)
    
    @staticmethod
    def get_most_populate_activities() -> list[dict]:
        """
            Se consulta: Actividades con más alumnos.

            Nota: Se intuye a que se refiere a las actividades a las que han asistido (incluso si la asistencia no está confirmada) más alumnos.
        """
        data = MySQLScriptRunner.run_script_to_query_database(
            script="""
                SELECT
                    a.nombre AS actividad,
                    COUNT(ac.ci_alumno) AS num_alumnos_participantes
                FROM 
                    ALUMNOS_CLASES AS ac
                LEFT JOIN
                    CLASES AS c ON ac.id_clase = c.id
                LEFT JOIN
                    ACTIVIDADES AS a ON c.id_actividad = a.id
                GROUP BY
                    a.id
                ORDER BY
                    num_alumnos_participantes DESC
            """
        )
        if (data is None):
            return None
        return DataFormatter.format_data(data)