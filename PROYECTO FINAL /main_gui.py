import tkinter as tk
from tkinter import ttk, messagebox
from inventory import Inventory


class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Inventario - POO")
        # Ajustamos el tamaño para incluir los botones
        self.geometry("600x450")

        self.inventory = Inventory()

        # Widgets
        self.create_widgets()
        self.refresh_list()

    # ------------------------------------------------------------------
    # 1. CREACIÓN DE WIDGETS
    # ------------------------------------------------------------------
    def create_widgets(self):
        # Frame para las entradas y botones
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)

        # Entradas
        tk.Label(input_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Cantidad:").grid(row=1, column=0, padx=5, pady=5)
        self.qty_entry = tk.Entry(input_frame)
        self.qty_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Precio:").grid(row=2, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        # Botones
        tk.Button(button_frame, text="Agregar Producto", command=self.add_product).pack(side=tk.LEFT, padx=5)

        # 🟢 NUEVO BOTÓN para Modificar
        tk.Button(button_frame, text="Modificar Seleccionado", command=self.modify_product_gui).pack(side=tk.LEFT,
                                                                                                     padx=5)

        tk.Button(button_frame, text="Eliminar Seleccionado", command=self.delete_selected).pack(side=tk.LEFT, padx=5)

        # Lista de productos (Treeview)
        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "Cantidad", "Precio"), show="headings")
        self.tree.heading("ID", text="ID", anchor="center")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # 🟡 NUEVO: Evento para cargar datos al seleccionar
        self.tree.bind('<<TreeviewSelect>>', self.load_selected_to_entries)

        # Atajos de teclado
        self.bind("<Delete>", lambda event: self.delete_selected())
        self.bind("d", lambda event: self.delete_selected())  # Atajo 'd'
        self.bind("<Escape>", lambda event: self.quit())

    # ------------------------------------------------------------------
    # 2. MANEJO DE EVENTOS (CRUD)
    # ------------------------------------------------------------------
    def get_input_data(self):
        """Valida y devuelve los datos de entrada."""
        name = self.name_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()

        if not name or not qty or not price:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return None
        try:
            qty = int(qty)
            price = float(price)
            if qty < 0 or price < 0:
                messagebox.showerror("Error", "Cantidad y precio deben ser positivos")
                return None
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser numéricos válidos")
            return None

        return name, qty, price

    def clear_entries(self):
        """Limpia todos los campos de entrada."""
        self.name_entry.delete(0, tk.END)
        self.qty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def add_product(self):
        data = self.get_input_data()
        if data:
            name, qty, price = data
            self.inventory.add_product(name, qty, price)
            self.refresh_list()
            self.clear_entries()

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleccione un producto para eliminar")
            return

        # Obtenemos el ID de la primera columna del item seleccionado
        product_id = int(self.tree.item(selected[0])["values"][0])
        self.inventory.remove_product(product_id)
        self.refresh_list()
        self.clear_entries()

    # 🟢 NUEVO MÉTODO para cargar los datos en las entradas
    def load_selected_to_entries(self, event):
        """Carga los datos del producto seleccionado en el formulario."""
        selected = self.tree.selection()
        if selected:
            # Obtiene los valores de la fila seleccionada: (ID, Nombre, Cantidad, Precio)
            values = self.tree.item(selected[0], 'values')

            self.clear_entries()

            # Insertar los valores en los campos de entrada
            self.name_entry.insert(0, values[1])
            self.qty_entry.insert(0, values[2])
            self.price_entry.insert(0, values[3])

    # 🟢 NUEVO MÉTODO para modificar el producto
    def modify_product_gui(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Debe seleccionar un producto para modificar.")
            return

        data = self.get_input_data()
        if data:
            name, qty, price = data

            # Obtenemos el ID del producto que estamos modificando
            product_id = int(self.tree.item(selected[0])["values"][0])

            # Llamamos al método de la clase Inventory
            success = self.inventory.modify_product(product_id, name, qty, price)

            if success:
                messagebox.showinfo("Éxito", f"Producto ID {product_id} modificado correctamente.")
                self.refresh_list()
                self.clear_entries()
            else:
                messagebox.showerror("Error", "No se pudo modificar el producto (ID no encontrado).")

    # ------------------------------------------------------------------
    # 3. LISTADO Y REFRESH
    # ------------------------------------------------------------------
    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for p in self.inventory.list_products():
            # Insertamos los atributos del objeto Producto en el Treeview
            self.tree.insert("", "end", values=(p.id, p.name, p.quantity, p.price))


if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()