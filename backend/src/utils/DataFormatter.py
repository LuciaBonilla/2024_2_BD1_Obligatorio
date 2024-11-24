from datetime import timedelta, date

class DataFormatter:
    """
        Clase auxiliar para formatear data de una lista de diccionarios (representación de registros de la base de datos) a un formato legible.
        
        Nota: Por ahora hace formateo de fechas. (timedelta o date -> YYYY-MM-SS)
        
        Estado: clase terminada.
    """
    
    @staticmethod
    def __timedelta_to_HMS(tdelta: timedelta) -> str:
        """
            Convierte un objeto timedelta a una cadena con el formato HH:MM:SS.
                
            Entrada:
                - `tdelta`: el objeto timedelta a convertir.
                
            Salida:
                - una cadena con el formato HH:MM:SS.
                
            Estado: método completado.
        """
        total_seconds = int(tdelta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    @staticmethod
    def __date_to_string(dateObj: date) -> str:
        """
            Convierte un objeto de tipo date a una cadena con el formato YYYY-MM-DD.
            
            Entrada:
                - `dateObj`: el objeto date a convertir.
            
            Salida:
                - Una cadena con el formato YYYY-MM-DD.
                
            Estado: método completado.
        """
        return dateObj.strftime("%Y-%m-%d")

    @staticmethod
    def format_data(data: list[dict]) -> list[dict]:
        """
            Recorre una lista de diccionarios (representación de registros de la base de datos) y
            convierte los valores de tipo timedelta y date a sus formatos correspondientes:
            HH:MM:SS para timedelta y YYYY-MM-DD para date.
            
            Entrada:
                - `data`: Lista de diccionarios con los datos a formatear.
            
            Salida:
                Lista de diccionarios con los datos formateados.
                
            Estado: método completado, ya que además de las fechas o tiempos, no hay otra data a formatear.
        """
        if (data is not None):
            for record in data:
                for (key, value) in record.items():
                    if isinstance(value, timedelta):  # Si es un timedelta
                        record[key] = DataFormatter.__timedelta_to_HMS(value)
                    elif isinstance(value, date):  # Si es una fecha
                        record[key] = DataFormatter.__date_to_string(value)
        return data