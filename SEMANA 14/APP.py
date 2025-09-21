import tkinter as tk
from tkinter import ttk, messagebox
from EVENTO import Event   # importamos nuestra clase Event

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # --- Lista de eventos ---
        self.tree = ttk.Treeview(root, columns=("fecha", "hora", "desc"), show="headings")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("desc", text="Descripción")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # --- Entradas ---
        frame_inputs = tk.Frame(root)
        frame_inputs.pack(pady=5)

        tk.Label(frame_inputs, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = tk.Entry(frame_inputs)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_inputs, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_inputs)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_inputs, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # --- Botones ---
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=10)
        tk.Button(frame_buttons, text="Eliminar Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=10)
        tk.Button(frame_buttons, text="Salir", command=root.quit).grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        """Agregar un nuevo evento a la lista"""
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        desc = self.desc_entry.get()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        # Usamos nuestra clase Event
        evento = Event(fecha, hora, desc)

        # Insertamos en el TreeView
        self.tree.insert("", "end", values=evento.as_tuple())

        # Limpiar campos
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        """Eliminar evento seleccionado"""
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Info", "Seleccione un evento para eliminar")
            return
        self.tree.delete(seleccionado)
