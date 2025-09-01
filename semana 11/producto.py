# producto.py

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_list(self):
        """Convierte el producto a lista para guardar en CSV"""
        return [self.id, self.nombre, str(self.cantidad), str(self.precio)]

    @staticmethod
    def from_list(data):
        """Crea un producto a partir de una fila de CSV"""
        return Producto(data[0], data[1], int(data[2]), float(data[3]))

    def __str__(self):
        return f"{self.id} - {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"
