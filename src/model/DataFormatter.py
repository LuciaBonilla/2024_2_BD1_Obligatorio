from datetime import timedelta, date

"""
Responsabilidad: Realiza formateo de data a una lista de diccionarios.
"""
class DataFormatter:
    @classmethod
    def __timedeltaToHMS(cls, tdelta):
        """
        Convierte un objeto timedelta a una cadena con el formato HH:MM:SS.
            
        Parámetros:
            tdelta (timedelta): El objeto timedelta a convertir.
            
        Retorna:
            Una cadena con el formato HH:MM:SS.
            
        Estado: método completado.
        """
        total_seconds = int(tdelta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    @classmethod
    def __dateToString(cls, dateObj):
        """
        Convierte un objeto de tipo date a una cadena con el formato YYYY-MM-DD.
        
        Parámetros:
            dateObj (date): El objeto date a convertir.
        
        Retorna:
            Una cadena con el formato YYYY-MM-DD.
            
        Estado: método completado.
        """
        return dateObj.strftime("%Y-%m-%d")

    @classmethod
    def formatData(cls, data):
        """
        Recorre una lista de diccionarios y convierte los valores de tipo timedelta y date
        a sus formatos correspondientes: HH:MM:SS para timedelta y YYYY-MM-DD para date.
        
        Parámetros:
            data (list): Lista de diccionarios con los datos a formatear.
        
        Retorna:
            list: Lista de diccionarios con los datos formateados.
            
        Estado: método completado, ya que además de las fechas o tiempos, no hay otra data a formatear.
        """
        for record in data:
            for key, value in record.items():
                if isinstance(value, timedelta):  # Si es un timedelta
                    record[key] = cls.__timedeltaToHMS(value)
                elif isinstance(value, date):  # Si es una fecha
                    record[key] = cls.__dateToString(value)
        return data