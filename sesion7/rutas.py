import os
from pathlib import Path

file = Path('/Users/jgomez/gitrepos/unicaes')
file_json = file / 'pythonIntermedio' / 'sesion7' / 'datos.json'

"""
file_json.name
file_json.stem
file_json.suffix
file_json.parent
file_json.parts
file_json.parents
"""

ruta = Path('/Users/jgomez/gitrepos/unicaes/sesion7/pruebadir/subdir/')
ruta.mkdir(parents=True)


# listar contenido de directorio
for archivo in ruta.iterdir():
    print(f"{archivo.name}, {archivo}")


# listar contenido con glob
for archivo in ruta.glob('*.py'):
    print(f"{archivo.name}, {archivo}")
