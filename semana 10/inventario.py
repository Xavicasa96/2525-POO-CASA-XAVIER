import csv
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.csv"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo CSV"""
        try:
            with open(self.archivo, "r", newline="", encoding="utf-8") as f:
                lector = csv.reader(f)
                for fila in lector:
                    if fila:  # evita líneas vacías
                        id_p, nombre, cantidad, precio = fila
                        self.productos.append(Producto(int(id_p), nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            # Si no existe el archivo, se crea vacío
            open(self.archivo, "w").close()
        except PermissionError:
            print("❌ No tienes permiso para leer el archivo.")

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo CSV"""
        try:
            with open(self.archivo, "w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                for p in self.productos:
                    escritor.writerow([p.id, p.nombre, p.cantidad, p.precio])
        except PermissionError:
            print("❌ No tienes permiso para escribir en el archivo.")

    def agregar(self, producto):
        """Agrega un producto nuevo al inventario"""
        for p in self.productos:
            if p.id == producto.id:
                print("❌ Error: ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(f"✅ Producto '{producto.nombre}' agregado y guardado en {self.archivo}.")

    def mostrar_todos(self):
        """Muestra todos los productos"""
        if not self.productos:
            print("📭 El inventario está vacío.")
        else:
            print("📦 Inventario completo:")
            for p in self.productos:
                print(p)
