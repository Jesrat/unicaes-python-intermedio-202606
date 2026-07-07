# SCOPE
# L E G B
# L - Local: dentro de la función actual
# E - Enclosing: función que contiene otra función (closures)
# G - Global: nivel de módulo/archivo paquete
# B - Built-in: funciones nativas


contador = 7

def incrementar_contador():
    step = 15
    print(contador)
    nueva_var = contador + step
    return step, nueva_var


capturado = incrementar_contador()
print(capturado)
# print(contador)
