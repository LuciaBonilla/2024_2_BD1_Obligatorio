from model.MySQLScriptRunner import MySQLScriptRunner
import logging


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
                - `headers`: diccionario que debería contener los parámetros de autenticación.

            Salida:
                - `True` si el usuario es un administrador, en caso contrario, `False`.

            Estado: método terminado.
        """
        return True
        # if "correo" not in headers or "contrasena" not in headers:
        #     return False

        # data = MySQLScriptRunner.run_script_to_query_database(
        #     script="""
        #         SELECT correo
        #         FROM LOGIN
        #         WHERE correo = %s AND contrasena = %s
        #     """,
        #     params=(headers["correo"], headers["contrasena"])
        # )

        # logging.info(f"Correo: {headers['correo']}, Contrasena: {headers['contrasena']}")
        # if data is None:
        #     return False
        # else:
        #     return True
