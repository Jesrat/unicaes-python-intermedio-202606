import json

# Parse
"""
file = open('data/datos.json')
raw_content = file.read()
file = open('data/datos.json')
content = json.load(file)
print(raw_content)
print(content)
"""

# TRY / EXCEPT / ELSE / FINALLY

file = None
try:
    print("Intento hacer algo")
    file = open('datos.json')
    print("El archivo existe y fue abierto exitosamente")
except FileNotFoundError:
    print("Esto se muestra si el try falló")
    print("Hubo un error")
except PermissionError:
    print("El archivo si se encontró pero no tienes permisos para leerlo")
except OSError:
    print("Aparentemente hay algún error con sistema operativo y disco")
except Exception:
    print("Alguna otra cosa falló")
else:
    print("Esto se ejecuta si lo que se intentaba hacer es exitoso")
    try:
        content = json.load(file)
        print("he hecho algo con el archivo")
    except json.decoder.JSONDecodeError:
        print("el archivo no pudo ser parseado")
finally:
    print("Esto se ejecuta siempre")
    if file:
        file.close()

print("el programa finalizó")

