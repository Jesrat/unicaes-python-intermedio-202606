import os


def open_data_file():
    current_working_dir = os.getcwd()
    filename = 'datos.json'
    try:
        file = open('datos.json')
    except FileNotFoundError:
        # print(f"el archivo '{filename}' no existe en la ruta '{current_working_dir}'")
        # Notificación al administrador
        # Guardar el intento de apertura del archivo en una base de auditoría
        raise
    else:
        return file




try:
    print("Hola intentaremos abrir el archivo que solicitas")
    open_data_file()
except Exception:
    print("El archivo que intentaste abrir no pudo ser leído")




"""
def email (destinatario, mensaje):
    try:
        envio correo al dueño de la cuenta
    except:
        notificamos al admin que hay problemas con el envio de correo
        raise
    
def substract_balance:
    quita dinero de una cuenta de banco
    email()
     
def add_balance:
    agregar dinero a una de cuenta de banco
    email()

def transfer:
    substract_balance()
    add_balance()
"""
