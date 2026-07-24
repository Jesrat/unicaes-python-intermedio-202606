# WRAP / Envolver

def saludar():
    print("Hola!")


def ejecutar(func):
    print("Antes de Ejecutar")
    func()
    print("Despues de ejecutar")


def mi_decorador(funcion_original):
    def wrapper(*args, **kwargs):
        print(f">> Llamando a {funcion_original.__name__}")
        resultado = funcion_original(*args, **kwargs)
        print(f">> {funcion_original.__name__} termino")
        return resultado
    return wrapper


def saludar(nombre):
    print(f"Hola! {nombre}")


@mi_decorador
def saludar(nombre):
    print(f"Hola! {nombre}")
