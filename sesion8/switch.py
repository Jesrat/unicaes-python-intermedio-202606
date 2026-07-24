def saludar():
    return "Hola"


def despedirse():
    return "Adios"


def nose():
    return "No se"


def switch(key):
    try:
        return {
            "a": saludar,
            "b": despedirse,
            "c": "Hello",
            "d": "Bye"
        }[key]
    except KeyError:
        return nose


switch("a")()
switch("b")()
switch("z")()
