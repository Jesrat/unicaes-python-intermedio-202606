data = [
    {
        "nombre": "Laptop",
        "precio": 100,
        "marca": "Apple",
        "modelo": "macbookpro",
        "is_active": False
    },
    {
        "nombre": "Televisor",
        "precio": 500,
        "marca": "LG",
        "modelo": "model1",
        "is_active": True
    }
]


class Producto:
    def __init__(self, data):
        self.data = data
        self.nombre = None
        self.precio = None
        self.marca = None
        self.modelo = None
        self.is_active = True
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        return f"<Producto: {self.nombre}>"

    def __repr__(self):
        return f"Producto({self.data})"

    def __bool__(self):
        is_cheap = self.precio < 100
        return is_cheap

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass



# instances = [Producto(i) for i in data]

instancia = Producto(data[0])
import requests

response = request.get("https://google.com")
if response:
    print("respuesta exitosa")

