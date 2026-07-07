# enumerate

# DRY (Don't Repeat Yourself)

students = [
    ("Student1", False, "Data Analysis", "M"),
    ("Student2", False, "Data Analysis", "F"),
    ("Student3", False, "Programador", "M"),
    ("Student4", True, "Gerente General", "M"),
    ("Student5", False, "Data Analysis", "F"),
    ("Student6", True, "Ing Industrial", "M"),
    ("Student6", False, "Ciberseguridad", "M"),
]

"""
for i, student in enumerate(students):
    print(f"{i}, {student}")
"""


import random
from time import sleep, time

nombres = ["Carlos", "Maria", "Jose", "Ana", "Luis", "Laura", "Pedro", "Sofia", "Diego", "Valentina",
           "Miguel", "Camila", "Andres", "Fernanda", "Javier", "Paula", "Ricardo", "Daniela", "Jorge", "Gabriela"]

apellidos = ["Garcia", "Martinez", "Rodriguez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez",
             "Ramirez", "Torres", "Flores", "Rivera", "Gomez", "Diaz", "Reyes", "Cruz", "Morales", "Ortiz"]

n = 1_000_000

registros = [f"{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}" for _ in range(n)]

total = len(registros)
inicio = time()

print(f"start")

"""
for i, row in enumerate(registros):
    # work here
    print(f"{i} of {total}", flush=True, end="\r")
    sleep(0.001)
"""

"""
for i, row in enumerate(registros, start=1):
    # work here
    porcentaje = i / total
    barra_len = 40
    llenado = int(barra_len * porcentaje)
    barra = "█" * llenado + "-" * (barra_len - llenado)
    print(f"\r[{barra}] {porcentaje*100:6.2f}% ({i}/{total})", end="", flush=True)
    sleep(0.00001)
"""


for i, row in enumerate(registros, start=1):
    # work here

    porcentaje = i / total
    barra_len = 40
    llenado = int(barra_len * porcentaje)
    barra = "█" * llenado + "-" * (barra_len - llenado)

    transcurrido = time() - inicio
    velocidad = i / transcurrido if transcurrido > 0 else 0
    restante = (total - i) / velocidad if velocidad > 0 else 0

    def formatear(segundos):
        m, s = divmod(int(segundos), 60)
        h, m = divmod(m, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    print(f"\r[{barra}] {porcentaje*100:6.2f}% ({i}/{total}) "
          f"| Transcurrido: {formatear(transcurrido)} "
          f"| Restante: {formatear(restante)}", end="", flush=True)

    sleep(0.00001)
