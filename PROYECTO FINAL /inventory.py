# inventory.py
import json
from product import Product


class Inventory:
    def __init__(self, filename="inventory_data.json"):
        self.products = []
        self.next_id = 1
        self.filename = filename
        self.load_from_file()

    def add_product(self, name, quantity, price):
        product = Product(self.next_id, name, quantity, price)
        self.products.append(product)
        self.next_id += 1
        self.save_to_file()
        return product

    # 🚨 MÉTODO AGREGADO: Modificar producto
    def modify_product(self, product_id, name, quantity, price):
        """Busca y actualiza los atributos de un producto por su ID."""
        product_id = int(product_id)
        found = False
        for p in self.products:
            if p.id == product_id:
                p.name = name
                p.quantity = quantity
                p.price = price
                found = True
                break

        if found:
            self.save_to_file()
        return found

    # ------------------------------------

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]
        self.save_to_file()

    def list_products(self):
        return self.products

    def save_to_file(self):
        data = [p.to_dict() for p in self.products]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.products = [Product.from_dict(item) for item in data]
            if self.products:
                self.next_id = max(p.id for p in self.products) + 1
        except FileNotFoundError:
            self.products = []
            self.next_id = 1