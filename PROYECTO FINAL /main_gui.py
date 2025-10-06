# main_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Inventario - POO")
        self.geometry("500x400")

        self.inventory = Inventory()

        # Widgets
        self.create_widgets()
        self.refresh_list()

    def create_widgets(self):
        # Formulario para agregar productos
        tk.Label(self, text="Nombre:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Cantidad:").pack()
        self.qty_entry = tk.Entry(self)
        self.qty_entry.pack()

        tk.Label(self, text="Precio:").pack()
        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        tk.Button(self, text="Agregar Producto", command=self.add_product).pack(pady=5)
        tk.Button(self, text="Eliminar Seleccionado", command=self.delete_selected).pack(pady=5)

        # Lista de productos
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(fill="both", expand=True)

    def add_product(self):
        name = self.name_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()
        if not name or not qty or not price:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        try:
            qty = int(qty)
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser numéricos")
            return
        self.inventory.add_product(name, qty, price)
        self.refresh_list()
        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleccione un producto para eliminar")
            return
        product_id = int(self.tree.item(selected[0])["values"][0])
        self.inventory.remove_product(product_id)
        self.refresh_list()

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in self.inventory.list_products():
            self.tree.insert("", "end", values=(p.id, p.name, p.quantity, p.price))

if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
