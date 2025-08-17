# inventario_demo.py

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        # Verifica si el ID ya existe
        for p in self.productos:
            if p.id == producto.id:
                print("Error: ID ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado.")  # <-- Aquí se imprime la confirmación

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario completo:")
            for p in self.productos:
                print(p)


def main():
    inventario = Inventario()

    while True:
        print("\n--- Inventario Simple ---")
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
                print("Error: datos inválidos.")
        elif opcion == "2":
            inventario.mostrar_todos()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
