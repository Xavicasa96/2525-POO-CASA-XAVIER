# product.py
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"[{self.id}] {self.name} - Cantidad: {self.quantity} - Precio: {self.price}"