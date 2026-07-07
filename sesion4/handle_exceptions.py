

def my_logging(message):
    # abrir un archivo, escribir la fecha del error y el mensaje del error
    print(message)


try:
    file = open('data/datos.json')
    file = open('mas_datos.json')
except FileNotFoundError as e:
    my_logging(
        f"no se pudo abrir el archivo {e.filename}"
    )
