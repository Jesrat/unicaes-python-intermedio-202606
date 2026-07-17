
class Product:
    def __init__(self, precio, *args, **kwargs):
        self.iva = 1.13
        self.precio = precio

    @property
    def precio_total(self):
        return self.precio * self.iva

    def check_stock(self):
        pass

    def exhaust_stock(self):
        pass


class Laptop(Product):
    pass


class TV(Product):

    @property
    def precio_total(self):
        precio_total = super().precio_total
        return precio_total - 10


class Telefono(Product):

    @property
    def precio_total(self):
        return self.precio


