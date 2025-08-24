from producto import Producto
from inventario import Inventario

def main():
    inventario = Inventario()

    while True:
        print("\n--- Inventario con CSV ---")
        print("1. Agregar producto")
        print("2. Mostrar todos")
        print("3. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar(Producto(id_p, nombre, cantidad, precio))
            except ValueError:
                print("❌ Error: datos inválidos.")
        elif opcion == "2":
            inventario.mostrar_todos()
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
