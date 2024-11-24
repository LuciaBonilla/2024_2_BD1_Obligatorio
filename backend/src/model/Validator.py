from model.MySQLScriptRunner import MySQLScriptRunner

class Validator:
    """
        Clase para validar que los usuarios puedan interactuar con la base de datos a través del backend.
        
        Estado: clase terminada.
    """
    
    @staticmethod
    def is_admin(body_request: dict) -> bool:
        """
            Dice si el usuario es un administrador para interactuar con la base de datos a través del backend.
            
            Entrada:
                - `body_request`: diccionario que debería contener los parámetros de autenticación.
                
            Salida:
                - `True` si el usuario es un administrador, en caso contrario, `False`.
                
            Estado: método terminado.
        """
        if ("login" not in body_request):
            return False

        if ("correo" not in body_request["login"]) or ("contrasena" not in body_request["login"]):
            return False
        
        data = MySQLScriptRunner.run_script_to_query_database(
            script="""
                SELECT correo
                FROM LOGIN
                WHERE correo = %s AND contrasena = %s
            """,
            params=(body_request["login"]["correo"], body_request["login"]["contrasena"])
        )
        
        if (data is None):
            return False
        else:
            return True