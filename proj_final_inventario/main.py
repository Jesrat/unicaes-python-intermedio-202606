from modelos import Producto
from repositorio import cargar_todos, agregar_producto
from servicios import (
    buscar_por_nombre,
    filtrar_por_categoria,
    filtrar_disponibles,
    aplicar_descuento_categoria,
    resumen_por_categoria,
    valor_total_inventario
)


def mostrar_menu():
    print("\n=== SISTEMA DE INVENTARIO ===")
    print("1. Ver todos los productos")
    print("2. Buscar producto")
    print("3. Filtrar por categoría")
    print("4. Ver solo disponibles")
    print("5. Agregar producto")
    print("6. Aplicar descuento por categoría")
    print("7. Resumen por categoría")
    print("8. Valor total del inventario (generador)")
    print("0. Salir")
    return input("\nOpción: ").strip()


def main():
    productos = cargar_todos()

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            if not productos:
                print("No hay productos.")
            for p in sorted(productos, key=lambda p: p.nombre):
                print(p)
        elif opcion == "2":
            termino = input("Buscar: ")
            resultados = buscar_por_nombre(productos, termino)
            print(f"{len(resultados)} resultado(s):")
            for p in resultados:
                print(p)
        elif opcion == "3":
            cat = input("Categoría: ")
            for p in filtrar_por_categoria(productos, cat):
                print(p)
        elif opcion == "4":
            for p in filtrar_disponibles(productos):
                print(p)
        elif opcion == "5":
            try:
                nuevo = Producto(
                    id=input("ID: "),
                    nombre=input("Nombre: "),
                    precio=float(input("Precio: ")),
                    stock=int(input("Stock: ")),
                    categoria=input("Categoría [General]: ") or "General"
                )
                productos = agregar_producto(nuevo, productos)
                print("Producto agregado.")
            except ValueError as e:
                print(f"Error {e}")
        elif opcion == "6":
            cat = input("Categoría: ")
            pct = float(input("Descuento %: "))
            productos = aplicar_descuento_categoria(productos, cat, pct)
            from repositorio import guardar_todos
            guardar_todos(productos)
            print("Descuento aplicado y guardado")
        elif opcion == "7":
            resumen = resumen_por_categoria(productos)
            for cat, datos in sorted(resumen.items()):
                print(
                    f"{cat}: {datos['cantidad']} productos | "
                    f"valor: ${datos['total']:.2f} | "
                    f"promedio: ${datos['promedio']:.2f}"
                )
        elif opcion == "8":
            total = valor_total_inventario()
            print(f"Valor total del inventario: ${total:.2f}")
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida")


if __name__ == '__main__':
    main()
