from flask import current_app


class utilSql:
    def createInsertQuery(entity: object, tableName: str) -> str:
        fieldNames = list(vars(entity).keys())
        keys = ', '.join(fieldNames)
        # Generates string like "%s, %s, %s, %s" * field in the obj
        s = ', '.join(['%s'] * len(fieldNames))
        script = f"""
            INSERT INTO {tableName} ({keys})
            VALUES ({s})
        """
        return script

    def getNewAttributesValues(entity: object):
        """Gets attributes of a object, like from Instructor will by nombre, apellido, etc.

        """
        current_app.logger.info(f"Getting attributes from {entity.__dict__.values()}")
        return tuple(entity.__dict__.values())

    def createUpdateQuery(entity: object, filterKey: str, tableName: str) -> tuple:
        """
            Generates an UPDATE script for the given entity.

            entity: object - The object to update.
            filterKey: str - The key to filter the entity.
            tableName: str - The table name where the entity is
        """
        set_clause = ', '.join(
            [f"{key} = %s" for key in vars(entity).keys() if key != filterKey])
        params = tuple(value for key, value in vars(
            entity).items() if key != filterKey)
        params += (getattr(entity, filterKey),)
        script = f"""
            UPDATE {tableName}
            SET {set_clause}
            WHERE {filterKey} = %s
        """
        current_app.logger.info(f"Generated UPDATE script: {script}")
        current_app.logger.info(f"Parameters for UPDATE script: {params}")
        return script, params

    def removeNullValues(listOfDictionaries: list) -> list:
        for dictionary in listOfDictionaries:
            keysToDelete = [key for key,
                            value in dictionary.items() if value is None]
            for key in keysToDelete:
                del dictionary[key]
        return listOfDictionaries
