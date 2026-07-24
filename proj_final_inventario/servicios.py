from repositorio import generar_productos


def buscar_por_nombre(productos, termino):
    """
    Filtra productos cuyo nombre contiene el término (case-insensitive)
    """
    return list(
        filter(
            lambda p: termino.lower() in p.nombre.lower(),
            productos
        )
    )


def filtrar_por_categoria(productos, categoria):
    return list(
        filter(
            lambda p: p.categoria == categoria,
            productos
        )
    )


def filtrar_disponibles(productos):
    return list(
        filter(
            lambda p: p.stock > 0,
            productos
        )
    )


def aplicar_descuento_categoria(productos, categoria, porcentaje):
    """
    Aplica un descuento a todos los productos de una categoría
    """
    def descuento(p):
        if p.categoria == categoria:
            p.precio = round(p._precio * (1 - porcentaje / 100), 2)
        return p
    return list(map(descuento, productos))


def resumen_por_categoria(productos):
    """
    Devuelve un dict {categoria: {total, cantidad, promedio}}
    """
    resumen = {}
    for p in productos:
        cat = p.categoria
        if cat not in resumen:
            resumen[cat] = {"total": 0, "cantidad": 0}
        resumen[cat]["total"] += p._precio * p._stock
        resumen[cat]["cantidad"] += 1
    for cat, datos in resumen.items():
        datos["promedio"] = round(datos["total"] / datos["cantidad"], 2)
    return resumen


def valor_total_inventario():
    """
    Calcula el valor total usando el generador (sin cargar todo en memoria)
    """
    return sum(
        p._precio * p._stock
        for p in generar_productos()
    )
