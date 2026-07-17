

class NoHayProducto(Exception):
    pass


class StockReservado(Exception):
    pass


class ProductoEnAveria(Exception):
    pass



try:
    raise NoHayProducto()
except NoHayProducto:
    print(f"su compra no puede ser realizada porque no hay existencias")
except StockReservado:
    print(f"este producto no puede ser vendido porque está reservado")
except ProductoEnAveria:
    print(f"este producto no puede ser vendido porque no cumple los estandares QA")
