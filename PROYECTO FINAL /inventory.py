# inventory.py
from product import Product  # Importa la clase Product desde product.py

class Inventory:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def add_product(self, name, quantity, price):
        product = Product(self.next_id, name, quantity, price)
        self.products.append(product)
        self.next_id += 1
        return product

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]

    def list_products(self):
        return self.products