
"""
funciones
- estructurar mejor el código
- DRY

estructuras de datos (un poco más complejas)
"""

nombre_estudiante_1 = "Baltazar"
nombre_estudiante_2 = "Jose"
nombre_estudiante_3 = "Ismael"

nombres_estudiantes = ["Baltazar", "Jose", "Ismael"]


nombre_producto = "Laptop"
precio_producto = 500.00
stock_producto = 5


def aplicar_descuento(precio, porcentaje):
    return precio * (1 - porcentaje / 100)


def mostrar_producto(nombre, precio, stock):
    print(f"{nombre}: ${precio} ({stock} en stock)")


def venta(producto, cantidad, stock):
    stock_bf_sale = stock
    stock_af_sale = stock - cantidad
    print(
        f"venta de {producto} "
        f"stock antes de venta {stock_bf_sale}"
        f"stock después de venta {stock_af_sale}"
    )
    return stock_af_sale


def get_data_as_json2():
    pass


# definición de clase
class Product:
    pass


# instanciar objetos
laptop = Product()
mouse = Product()
teclado = Product()


# arrancar o encender
# usar combustible
# acelerar
# transportar carga
# darle mantenimiento
# competir



class Car:
    def __init__(self, brand, model, year, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.owner = owner
        self.esta_encendido = False

    def encender(self):
        self.esta_encendido = True


class VideoGame:
    def __init__(self):
        self.name = None
        self.portada = None
        self.color = None
        self.producido_por = None
        self.consola = None


class Audifonos:
    def __init__(self, *args, **kwargs):
        self.marca = None
        self.type = None
        self.noise_cancellation = None
        self.color = None
        self.potencia = None


class SinCombustible(Exception):
    pass


class TanqueCombustible:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.nivel = 0
        self.litros = 0

    def calcular_nivel(self):
        self.nivel = (self.litros / self.capacidad) * 100

    def echar_combustible(self, litros):
        if (self.litros + litros) > self.capacidad:
            raise Exception("no le puedes poner mas combustible del que soporta")
        self.litros += litros
        self.calcular_nivel()

    def consumir_combustible(self, litros):
        self.litros -= litros
        self.calcular_nivel()


class Car:
    def __init__(self):
        self.esta_encendido = False
        self.esta_frenado = False
        self.kilometraje = 0
        self.tanque_combustible = TanqueCombustible(100)
        self.datos_de_mantenimiento = {
            "necesita": False,
            "ultimo_mantenimiento_km": 0,
            "frecuencia_km": 20
        }

    @property
    def proximo_mantenimiento(self):
        return self.datos_de_mantenimiento["ultimo_mantenimiento_km"] \
            + self.datos_de_mantenimiento["frecuencia_km"]

    def encender(self):
        if self.esta_encendido:
            print(f"Hacer ruido")
            return
        if self.tanque_combustible.litros == 0:
            raise SinCombustible()
        self.esta_encendido = True

    def apagar(self):
        self.esta_encendido = False

    def avanzar(self):
        self.kilometraje += 1
        if self.kilometraje >= self.proximo_mantenimiento:
            self.datos_de_mantenimiento["necesita"] = True

    def acelerar(self):
        if not self.esta_frenado:
            self.avanzar()
        self.tanque_combustible.consumir_combustible(0.1)

    def dar_mantenimiento(self):
        self.datos_de_mantenimiento["necesita"] = False
        self.datos_de_mantenimiento["ultimo_mantenimiento_km"] = self.kilometraje


my_car = Car()


