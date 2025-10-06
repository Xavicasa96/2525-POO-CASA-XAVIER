# main_gui.py
from producto import Producto
from inventario import Inventario


def menu():
    inv = Inventario()
    inv.cargar_csv()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos")
        print("7. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar(Producto(id, nombre, cantidad, precio))

        elif opcion == "2":
            id = input("ID a eliminar: ")
            inv.eliminar(id)

        elif opcion == "3":
            id = input("ID: ")
            nueva = int(input("Nueva cantidad: "))
            inv.actualizar_cantidad(id, nueva)

        elif opcion == "4":
            id = input("ID: ")
            nuevo = float(input("Nuevo precio: "))
            inv.actualizar_precio(id, nuevo)

        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            inv.buscar_por_nombre(nombre)

        elif opcion == "6":
            inv.mostrar_todos()

        elif opcion == "7":
            inv.guardar_csv()
            print("💾 Inventario guardado en inventario.csv. ¡Adiós!")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
