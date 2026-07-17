

class Car:
    iva = "13"

    def __init__(self, model, year):
        self.model = model
        self.year = year



class Producto:
    iva = 1.13
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if not isinstance(valor, int):
            raise TypeError("el precio debe ser un numero entero")
        if (((self._precio - valor) / self._precio)*100) > 20:
            raise Exception("no se asignar un nuevo precio que sea menor al 20% del precio actual")
        self._precio = valor

    @property
    def precio_total(self):
        return self._precio * self.iva


laptop = Producto("macbook", 700)
laptop._precio = 600

