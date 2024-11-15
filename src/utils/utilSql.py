class utilSql:
    def createInsertQuery(newValue: dict, tableName: str) -> str:
        fieldNames = list(vars(newValue).keys())
        keys = ', '.join(fieldNames)
        s = ', '.join(['%s'] * len(fieldNames)) # Generates string like "%s, %s, %s, %s" * field in the obj
        script = f"""
            INSERT INTO {tableName} ({keys})
            VALUES ({s})
        """
        return script

    def getParams(newValue):
        return tuple(newValue.__dict__.values())

    def createUpdateQuery(valueToUpdate, tableName, paramKeyWhere, paramValueWhere):
        fieldNames = list(vars(valueToUpdate).keys())
        s = ', '.join(['%s = %s'] * len(fieldNames)) # Generates string like "%s = %s, %s = %s" * field in the obj
        script = f"""
            UPDATE {tableName}
            SET {s}
            WHERE {"%s"} = {"%s"}
        """
        params = utilSql.getParamsForSetLineScript(valueToUpdate)
        params.append(paramKeyWhere)
        params.append(paramValueWhere)
        return script, params
    
    def getParamsForSetLineScript(valueToUpdate):
        params = []
        for key, value in vars(valueToUpdate):
            
            params.append(key)
            params.append(value)
        return tuple(params)


    def removeNullValues(listDictionary: dict) -> dict:
        for dictonary in listDictionary:
            keysToDelete = [key for key,
                              value in dictonary.items() if value is None]
            for key in keysToDelete:
                del dictonary[key]
        return listDictionary
