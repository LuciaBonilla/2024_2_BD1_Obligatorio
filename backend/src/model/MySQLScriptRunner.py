import os
import mysql.connector
class MySQLScriptRunner:
    """
        Responsabilidad: Conectarse a la base de datos, y ejecutar los scripts MySQL e inyectar los valores que le llegan.
        
        Si ejecuta scripts para consultar datos de la base, entonces retorna los datos consultados.
        
        Si ejecuta scripts para modificar la base, entonces retorna el resultado de la operación (exitosa/no exitosa).
        
        Estado: clase completada.
    """
    
    # ->>> ATRIBUTOS DE CLASE.

    # Obtiene las variables de entorno para la base de datos, definidas en docker-compose.yml.
    __DB_HOST = os.environ.get("DB_HOST")
    __DB_PORT = os.environ.get("DB_PORT")
    __DB_USER = os.environ.get("DB_USER")
    __DB_PASSWORD = os.environ.get("DB_PASSWORD")
    __DB_NAME = os.environ.get("DB_NAME")

    # Conexión a la base de datos.
    __CONNECTION = None

    # ->>> MÉTODOS DE CLASE.
    # cls se refiere a la clase, no a una instancia; permite obtener los atributos y llamar a los métodos de clase.
    # cls se debe colocar en todos los métodos de clase como parámetro del método.

    @classmethod
    def __start_database_connection(cls) -> None:
        """
            Establece una conexión a la base de datos.

            Estado: método completado.
        """
        if (cls.__CONNECTION is None or not cls.__CONNECTION.is_connected()):
            try:
                cls.__CONNECTION = mysql.connector.connect(
                    host=cls.__DB_HOST,
                    port=cls.__DB_PORT,
                    user=cls.__DB_USER,
                    password=cls.__DB_PASSWORD,
                    database=cls.__DB_NAME
                )
            except mysql.connector.Error:
                cls.__CONNECTION = None

    @classmethod
    def __end_database_connection(cls) -> None:
        """
            Apaga la conexión con la base de datos.

            Estado: método completado.
        """
        if (cls.__CONNECTION and cls.__CONNECTION.is_connected()):
            cls.__CONNECTION.close()
            cls.__CONNECTION = None

    @classmethod
    def get_database_connection_status(cls) -> bool:
        """
            Dice si la conexión a la base de datos fue exitosa.

            Salida:
                - `True` si la conexión es exitosa, `False` en caso contrario.

            Estado: método completado.
        """
        status = None
        try:
            cls.__start_database_connection()
            status = cls.__CONNECTION is not None and cls.__CONNECTION.is_connected()
        except mysql.connector.Error:
            status = False
        finally:
            cls.__end_database_connection()
        return status

    @classmethod
    def run_script_to_query_database(cls, script: str, params: tuple =None) -> list[dict]:
        """
            Ejecuta un script de MySQL con el objetivo de consultar datos de la base.

            Entradas:
                - `script`: el script MySQL a ejecutar.
                - `params`: tupla que contiene los valores que reemplazarán los placeholders `%s` en la consulta MySQL.
                
            El uso de `params` permite que el controlador de MySQL maneje estos valores de manera segura, protegiendo contra inyección SQL.

            Salida:
                - los datos consultados (lista de diccionarios, donde cada diccionario es un registro de la tabla) o `None`.

            Estado: método completado.
        """
        data = None
        try:
            # Establece la conexión con la base de datos.
            cls.__start_database_connection()

            # Crea un objeto cursor para ejecutar el script SQL.
            cursor = cls.__CONNECTION.cursor(dictionary=True)

            # Ejecuta el script de consulta.
            if (params is None):
                cursor.execute(script)
            else:
                cursor.execute(script, params=params)

            # Obtiene todos los resultados de la consulta como una lista de diccionarios, donde cada diccionario representa un registro de la tabla.
            data = cursor.fetchall()

            if (data == []):
                data = None

            # Cierra el cursor.
            cursor.close()
        except mysql.connector.Error as error:
            current_app.logger.error(f"Error al ejecutar el script de consulta: {error}")
        finally:
            # Asegura que la conexión se cierre en cualquier caso.
            cls.__end_database_connection()
        return data

    @classmethod
    def run_script_to_modify_database(cls, script: str, params: tuple =None) -> bool:
        """
            Ejecuta un script de MySQL con el objetivo de modificar datos en la base de datos.
            
            Puede realizar operaciones como, por ejemplo, INSERT, UPDATE o DELETE.

            Entradas:
                - `script`: el script MySQL a ejecutar.
                - `params`: tupla que contiene los valores que reemplazarán los placeholders `%s` en la consulta MySQL.
                
            El uso de `params` permite que el controlador de MySQL maneje estos valores de manera segura, protegiendo contra inyección SQL.

            Salida:
                - `True` si la operación fue exitosa, y `False` en caso de error.

            Estado: método terminado.
        """
        result = None
        try:
            # Establece la conexión con la base de datos.
            cls.__start_database_connection()

            # Crea el cursor para ejecutar el comando SQL.
            cursor = cls.__CONNECTION.cursor()

            # Ejecuta el script de modificación.
            if (params is None):
                cursor.execute(script)
            else:
                cursor.execute(script, params)

            # Confirma (commit) los cambios en la base de datos.
            cls.__CONNECTION.commit()

            # Cierra el cursor.
            cursor.close()
            result = True
        except mysql.connector.Error as error:
            print(f"Error al ejecutar el script de modificación: {error}")

            # Realiza un rollback para revertir los cambios en caso de error.
            if cls.__CONNECTION:
                cls.__CONNECTION.rollback()

            result = False
        finally:
            # Asegura que la conexión se cierre en cualquier caso.
            cls.__end_database_connection()
        return result
