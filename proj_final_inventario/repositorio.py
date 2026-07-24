import json
from pathlib import Path
from modelos import Producto
from decoradores import log_operacion

RUTA_JSON = Path('datos/inventario.json')


@log_operacion
def cargar_todos():
    """
    Carga todos los productos desde JSON.
    """
    if not RUTA_JSON.exists():
        return []
    datos = json.loads(RUTA_JSON.read_text(encoding='utf-8'))
    return [Producto.from_dict(d) for d in datos]


def generar_productos(ruta=RUTA_JSON):
    """
    Generador: produce productos de uno en uno desde JSON.
    """
    if not ruta.exists():
        return
    datos = json.loads(RUTA_JSON.read_text(encoding='utf-8'))
    for d in datos:
        yield Producto.from_dict(d)


@log_operacion
def guardar_todos(productos):
    """
    Guarda la lista de productos en JSON
    """
    RUTA_JSON.parent.mkdir(parents=True, exist_ok=True)
    datos = [p.to_dict() for p in productos]
    RUTA_JSON.write_text(
        json.dumps(datos, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )


@log_operacion
def agregar_producto(producto, productos):
    """
    Agrega un producto si no existe ya (por id)
    """
    if producto in productos:
        raise ValueError(f"Ya existe un producto con id {producto.id}")
    productos.append(producto)
    guardar_todos(productos)
    return productos
