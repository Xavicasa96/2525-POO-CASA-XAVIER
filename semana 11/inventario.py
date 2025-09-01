# inventario.py
import csv
import os
from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = {}  # dict {ID: Producto}

    def agregar(self, producto: Producto):
        self.productos[producto.id] = producto

    def eliminar(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("⚠️ Producto no encontrado")

    def actualizar_cantidad(self, id, nueva_cantidad):
        if id in self.productos:
            self.productos[id].cantidad = nueva_cantidad
        else:
            print("⚠️ Producto no encontrado")

    def actualizar_precio(self, id, nuevo_precio):
        if id in self.productos:
            self.productos[id].precio = nuevo_precio
        else:
            print("⚠️ Producto no encontrado")

    def buscar_por_nombre(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_csv(self, archivo="inventario.csv"):
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Cantidad", "Precio"])  # encabezado
            for p in self.productos.values():
                writer.writerow(p.to_list())

    def cargar_csv(self, archivo="inventario.csv"):
        if not os.path.exists(archivo):
            return
        with open(archivo, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # saltar encabezado
            for row in reader:
                producto = Producto.from_list(row)
                self.agregar(producto)
