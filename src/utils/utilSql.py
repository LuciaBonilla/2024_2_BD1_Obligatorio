class utilSql:
    def insert_creator(value_to_insert: dict, table_name: str) -> str:
        keys_as_strings = list(vars(value_to_insert).keys())
        keys = ', '.join(keys_as_strings)
        s = ', '.join(['%s'] * len(keys_as_strings))
        script = f"""
            INSERT INTO {table_name} ({keys})
            VALUES ({s})
        """
        return script

    def get_params(value_to_insert):
        return tuple(value_to_insert.__dict__.values())
    
    
