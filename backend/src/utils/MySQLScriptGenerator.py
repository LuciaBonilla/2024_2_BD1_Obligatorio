class MySQLScriptGenerator:
    """
        Clase auxiliar para crear los scripts de SELECT *, INSERT, UPDATE Y DELETE en MySQL, y crear los valores a inyectar en los scripts.
        
        También es clase auxiliar para obtener los nombres y valores de los atributos de una entidad.
        
        Nota: Se mantiene la seguridad brindando los scripts con los placeholders `%s` y los parámetros a inyectar en los scripts.
        
        En otras palabras, no usamos `f-strings` para colocar en los scriptos los valores brindados por los usuarios.
        
        Nota: Una entidad representa algo de la vida real (ej. instructor, equipamiento, etc.) que se insertará, actualizará o eliminará en la base de datos
        como un registro de 'x' tabla.
        
        Estado: clase terminada.
    """
    
    @staticmethod
    def get_attributes_name(entity: object) -> tuple:
        """
            Obtiene los nombres de los atributos de una entidad.

            Ej. para la entidad Instructor sería nombre, apellido, etc.
            
            Entrada:
                - `entity`: entidad.
                
            Salida:
                - tupla con los nombres de los atributos de la entidad.
                
            Estado: método terminado.
        """
        return tuple(entity.__dict__.keys())
    
    @staticmethod
    def get_attributes_value(entity: object) -> tuple:
        """
            Obtiene los valores de los atributos de una entidad.
    
            Ej. para la entidad Instructor sería "Juan" (nombre), "Peréz" (apellido), etc.
            
            Entrada:
                - `entity`: entidad.
                
            Salida:
                - tupla con los valores de los atributos de la entidad.
                
            Estado: método terminado.
        """
        return tuple(entity.__dict__.values())
    
    @staticmethod
    def create_select_all_columns_script(filter_key: str, filter_value: any, table_name: str) -> tuple:
        """
            Crea un script MySQL de SELECT *.
            
            Entradas:
                - `filter_key`: nombre del atributo para filtrar la entidad.
                - `filter_value`: valor del atributo para filtrar la entidad.
                - `table_name`: tabla en la base de datos a la que pertenece la entidad.
                
            Salida: 
                - el script de SELECT * y los valores a inyectar.
                
            Estado: método terminado.
        """
        # Línea de WHERE en el script.
        where_sentence = filter_key + " = %s"
        
        script = f"""
            SELECT *
            FROM {table_name}
            WHERE {where_sentence}
        """
        
        # El valor a inyectar en el script.
        params = (filter_value,)
        
        return (script, params)
    
    @staticmethod
    def create_insert_script(entity: object, table_name: str) -> tuple:
        """
            Crea un script MySQL de INSERT.
            
            Entradas:
                - `entity`: entidad que se insertará en la base de datos como un registro de `table_name`.
                - `table_name`: tabla en la base de datos a la que pertenece la entidad.
                
            Salida: 
                - el script de INSERT y los valores a inyectar.
                
            Estado: método terminado.
        """
        # Cantidad de valores a insertar en la tabla (cantidad por registro en la tabla).
        fields_quantity = len(MySQLScriptGenerator.get_attributes_name(entity=entity))
        
        # Nombres de los atributos.
        fields_name = MySQLScriptGenerator.get_attributes_name(entity=entity)
        
        # Línea de COLUMNS en el script.
        columns_sentence = ", ".join(fields_name)
        
        # Línea de VALUES en el script.
        values_sentence = ", ".join(["%s"] * fields_quantity)
        
        script = f"""
            INSERT INTO {table_name} ({columns_sentence})
            VALUES ({values_sentence})
        """

        # Los valores a inyectar en el script. Están en orden según los "%s" en el script.
        params = MySQLScriptGenerator.get_attributes_value(entity=entity)
        
        return (script, params)

    @staticmethod
    def create_update_script(entity: object, filter_key: str, filter_value: any, table_name: str) -> tuple:
        """
            Crea un script MySQL de UPDATE.
            
            Entradas:
                - `entity`: entidad que se actualizará en la base de datos como un registro de `table_name`.
                - `table_name`: tabla en la base de datos a la que pertenece la entidad.
                - `filter_key`: nombre del atributo para filtrar la entidad.
                - `filter_value`: valor del atributo para filtrar la entidad.
                
            Salida: 
                - el script de UPDATE y los valores a inyectar.
                
            Estado: método terminado.
        """
        # Nombres de los atributos a actualizar.
        fields_to_set = MySQLScriptGenerator.get_attributes_name(entity=entity)
        
        # Línea SET en el formato deseado: campo1 = %s, campo2 = %s, ...
        set_sentence = ", ".join([(field + " = %s") for field in fields_to_set])
        
        # Línea de WHERE en el script.
        where_sentence = filter_key + " = %s"
        
        script = f"""
            UPDATE {table_name}
            SET {set_sentence}
            WHERE {where_sentence}
        """
        
        # Valores de los atributos a setear.
        values_to_set = MySQLScriptGenerator.get_attributes_value(entity=entity)
        
        # Los valores a inyectar en el script. Están en orden según los "%s" en el script.
        params = values_to_set + (filter_value,)
        
        return (script, params)
    
    @staticmethod
    def create_delete_script(filter_key: str, filter_value: str, table_name: str) -> tuple:
        """
            Crea un script MySQL de DELETE.
            
            Entradas:
                - `table_name`: tabla en la base de datos a la que pertenece la entidad.
                - `filter_key`: nombre de la columna para filtrar la entidad.
                - `filter_value`: valor de la columna para filtrar la entidad.
                
            Salida: 
                - el script de DELETE y los valores a inyectar.
                
            Estado: método terminado.
        """
        
        # Línea de WHERE en el script.
        where_sentence = filter_key + " = %s"
        
        script = f"""
            DELETE FROM {table_name}
            WHERE {where_sentence}
        """
        
        # Los valores a inyectar en el script.
        params = (filter_value,)
        
        return (script, params)
