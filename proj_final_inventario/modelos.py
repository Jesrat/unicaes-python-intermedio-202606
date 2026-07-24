class Producto:
    def __init__(self, id, nombre, precio, stock, categoria='General'):
        self.id = id
        self.nombre = nombre
        self._precio = float(precio)
        self._stock = int(stock)
        self.categoria = categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, v):
        if not isinstance(v, (int, float)) or v < 0:
            raise ValueError(f"Precio invalido: {v}")
        self._precio = float(v)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, v):
        if not isinstance(v, int) or v < 0:
            raise ValueError(f"Stock invalido: {v}")
        self._stock = v

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self._precio,
            "stock": self._stock,
            "categoria": self.categoria
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["id"],
            d["nombre"],
            d["precio"],
            d["stock"],
            d.get("categoria", "General")
        )

    def __str__(self):
        return f"[{self.id}] {self.nombre} | ${self.precio:.2f} |stock: {self._stock} | {self.categoria}"

    def __repr__(self):
        return f"Producto({self.id}, {self.nombre}, {self._precio}, {self.stock})"

    def __eq__(self, other):
        return isinstance(other, Producto) and self.id == other.id
