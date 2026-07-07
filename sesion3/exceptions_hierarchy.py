

# Exception
"""
try:
    print("Intento hacer algo")
    file = open('datos.json')
except FileNotFoundError:
    print("el archivo no existe")
except Exception:
    print("hubo una excepcion")
"""


def dividir(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")
        return None
    except TypeError:
        print("los argumentos deben ser números")
        return None
    else:
        return result


def dividir(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        print("Error: los argumentos son incorrectos")
        return None
    else:
        return result


def login(usuario, password):
    try:
        assert usuario == 'user'
        assert password == 'm1Contr4'
    except AssertionError:
        print(f"el usuario o la contraseña son incorrectos")
    else:
        print("login exitoso")


def divide(a: float, b: float) -> [float, None]:
    """
    :param a:
    :param b:
    :return: None in case of error, returns float datatype if everything works fine
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        print("Error: los argumentos son incorrectos")
        return None
    else:
        return result


# divide("hola", 5)
"""
ValueError
int('hello')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'

TypeError
'hello' + 5
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

KeyError
{"hello": "hola", "goodbye": "adios"}["hi"]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 'hi'

IndexError
["hello", "hola", "goodbye"][3]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: list index out of range

FileNotFoundError
archivo no existe

PermissionError
sin permisos para leer o escribir un archivo

ZeroDivisionError
no se puede dividir entre cero

AttributeError
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
yo = Persona("Josue")
yo.nombre
'Josue'
yo.apellido
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'Persona' object has no attribute 'apellido'


json.JSONDecodeError
error al parsear

StopIteration
El iterador no tiene mas elementos
"""


def calcular_descuento(precio, porcentaje):
    if precio <= 0:
        raise ValueError(f"El precio debe ser positivo: {precio}")
    if not (0 <= porcentaje <= 100):
        raise ValueError(f"El porcentaje de descuento debe estar entre 0 y 100, usted ingresó: {porcentaje}")
    return precio * (1 - porcentaje / 100)
