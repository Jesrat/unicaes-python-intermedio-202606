
class TransportBase:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Sedan(TransportBase):
    def __init__(self, brand, model, year, cantidad_puertas):
        super().__init__(brand, model, year)
        self.cantidad_puertas = cantidad_puertas


class Moto(TransportBase):
    def __init__(self, brand, model, year, tipo_cadena):
        super().__init__(brand, model, year)
        self.tipo_cadena = tipo_cadena


class Camion(TransportBase):
    def __init__(self, brand, model, year, capacidad_de_carga):
        super().__init__(brand, model, year)
        self.capacidad_de_carga = capacidad_de_carga


class Avion(TransportBase):
    def __init__(self, brand, model, year, posicion_de_alas):
        super().__init__(brand, model, year)
        self.posicion_de_alas = posicion_de_alas
