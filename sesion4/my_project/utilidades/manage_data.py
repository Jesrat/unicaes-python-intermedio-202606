import json


def get_data_as_json(file_name):
    try:
        file = open(file_name)
        return json.load(file)
    except FileNotFoundError as e:
        print(f"no se encontró el archivo {e.filename}")
    except PermissionError as e:
        print(f"usted no tiene permisos para leer el archivo {e.filename}")
    except json.JSONDecodeError:
        def print2(param):
            raise Exception("esto no existe")
        print(f"el archivo no pudo ser parseado a JSON favor verifique la estructura")
