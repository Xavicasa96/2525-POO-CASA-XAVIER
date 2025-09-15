import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplicación GUI Básica")

        # Crear componentes
        self.crear_componentes()

        # Iniciar ventana
        self.root.mainloop()

    def crear_componentes(self):
        """Crea los elementos de la interfaz gráfica"""

        # Etiqueta
        self.label = tk.Label(self.root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.btn_agregar = tk.Button(self.root, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.pack(pady=5)

        # Lista para mostrar datos
        self.lista_datos = tk.Listbox(self.root, width=50, height=10)
        self.lista_datos.pack(pady=5)

        # Botón Limpiar
        self.btn_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_lista)
        self.btn_limpiar.pack(pady=5)

    def agregar_dato(self):
        """Agrega lo escrito en el campo a la lista"""
        dato = self.entry.get()
        if dato.strip() == "":
            messagebox.showwarning("Atención", "Debe ingresar un dato válido.")
        else:
            self.lista_datos.insert(tk.END, dato)
            self.entry.delete(0, tk.END)

    def limpiar_lista(self):
        """Elimina la selección o toda la lista"""
        seleccion = self.lista_datos.curselection()
        if seleccion:
            self.lista_datos.delete(seleccion)
        else:
            self.lista_datos.delete(0, tk.END)
