data = [
    {
        "nombre": "Laptop",
        "precio": 100,
        "marca": "Apple",
        "modelo": "macbookpro",
        "is_active": False,
        "serie": "MX845679"
    },
    {
        "nombre": "Televisor",
        "precio": 500,
        "marca": "LG",
        "modelo": "model1",
        "is_active": True,
        "serie": "MX845679"
    },
    {
        "nombre": "Laptop",
        "precio": 100,
        "marca": "Apple",
        "modelo": "macbookpro",
        "is_active": False,
        "serie": "MX845679"
    },
    {
        "nombre": "Laptop",
        "precio": 100,
        "marca": "Apple",
        "modelo": "macbookpro",
        "is_active": False,
        "serie": "MX845779"
    },
]


class Producto:
    def __init__(self, data):
        self.data = data
        self.nombre = None
        self.precio = None
        self.marca = None
        self.modelo = None
        self.is_active = True
        self.serie = None
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        return f"<Producto: {self.nombre}>"

    def __repr__(self):
        return f"Producto({self.data})"

    def __bool__(self):
        is_cheap = self.precio < 100
        return is_cheap

    def __eq__(self, other_product):
        return self.serie == other_product.serie

    def __lt__(self, other):
        return self.precio < other.precio

    def __gt__(self, other):
        return self.precio > other.precio


producto1 = Producto(data[0])
producto2 = Producto(data[1])
producto3 = Producto(data[2])
producto4 = Producto(data[3])

producto4 > producto1
