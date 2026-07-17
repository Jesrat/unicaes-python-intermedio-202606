import json


file = open('datos.json')
json_content = json.load(file)
# TRABAJO
file.close()

with open('datos.json') as file:
    json_content = json.load(file)


from datetime import datetime
from contextlib import contextmanager


@contextmanager
def medir_tiempo(nombre):
    inicio = datetime.now()
    print(f"[{nombre}] Iniciando ...")
    try:
        yield
    finally:
        fin = datetime.now()
        duracion = (fin - inicio).total_seconds()
        print(f"[{nombre}] Completado en {duracion:.3f}s")



class MedirTiempo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.inicio = datetime.now()
        print(f"[{self.nombre}] Iniciando ...")
        print(f"abriendo el archivo 'datos.json'")

    def __exit__(self, exc_type, exc_val, exc_tb):
        fin = datetime.now()
        duracion = (fin - self.inicio).total_seconds()
        print(f"cerrando el archivo 'datos.json'")
        print(f"[{self.nombre}] Completado en {duracion:.3f}s")
        print(f"{exc_type=}")
        print(f"{exc_val=}")
        print(f"{exc_tb=}")


class ConexionDatabase:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        print("recibí las credenciales para abrir la conexion")

    def __enter__(self):
        print(f"intentando la conexión a la base de datos con el usuario {self.user}")
        self.conn = True
        print("la conexion a la base de datos ha sido exitosa")
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn = False
        print(f"la conexion a la base de datos ha sido cerrada")
