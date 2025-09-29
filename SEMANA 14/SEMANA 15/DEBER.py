import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea
def agregar_tarea(event=None):
    tarea = entry_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Agregar al Listbox
        entry_tarea.delete(0, tk.END)       # Limpiar la caja de texto
    else:
        messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

# Función para marcar como completada
def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        idx = seleccion[0]
        tarea = lista_tareas.get(idx)
        if tarea.endswith("✔"):
            lista_tareas.delete(idx)
            lista_tareas.insert(idx, tarea.replace(" ✔", ""))  # Quitar marca
        else:
            lista_tareas.delete(idx)
            lista_tareas.insert(idx, tarea + " ✔")  # Agregar marca
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea para marcarla.")

# Función para eliminar tarea
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showinfo("Aviso", "Selecciona una tarea para eliminarla.")

# Crear ventana
root = tk.Tk()
root.title("Lista de Tareas")

# Caja de texto
entry_tarea = tk.Entry(root, width=40)
entry_tarea.grid(row=0, column=0, padx=10, pady=10)
entry_tarea.bind("<Return>", agregar_tarea)  # Enter añade tarea

# Botón añadir
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=1, padx=10, pady=10)

# Listbox (lista de tareas)
lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botones de acción
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Iniciar aplicación
root.mainloop()
