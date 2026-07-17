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


