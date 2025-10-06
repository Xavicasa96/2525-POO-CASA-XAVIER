# product.py
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convierte el producto a un diccionario para guardar en JSON"""
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Product a partir de un diccionario"""
        return Product(data["id"], data["name"], data["quantity"], data["price"])

    def __str__(self):
        return f"[{self.id}] {self.name} - Cantidad: {self.quantity} - Precio: {self.price}"
