"""
Dashboard Personalizado Básico
Mejoras simples:
- Muestra fecha de última modificación de los scripts.
- Permite visualizar y ejecutar scripts.
- Menú sencillo y claro.

Autor: Xavier Casa
"""

import os
import subprocess
import time

def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            contenido = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(contenido)
    except:
        print("Error al leer el archivo.")

def ejecutar_script(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.run(['python', ruta_script])
        else:
            subprocess.run(['python3', ruta_script])
    except:
        print("No se pudo ejecutar el script.")

def listar_scripts(ruta):
    if not os.path.exists(ruta):
        print("No existe la ruta especificada.")
        return []

    scripts = []
    for archivo in os.listdir(ruta):
        if archivo.endswith('.py'):
            ruta_completa = os.path.join(ruta, archivo)
            fecha = time.ctime(os.path.getmtime(ruta_completa))
            scripts.append((archivo, fecha))
    return scripts

def mostrar_menu_principal():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Unidad 1")
    print("2. Unidad 2")
    print("0. Salir")

def mostrar_scripts_de_unidad(unidad):
    ruta = os.path.join(os.getcwd(), unidad)
    scripts = listar_scripts(ruta)

    if not scripts:
        print("No hay scripts en esta unidad.")
        return

    while True:
        print(f"\n--- Scripts en {unidad} ---")
        for i, (script, fecha) in enumerate(scripts, start=1):
            print(f"{i}. {script} (Última modificación: {fecha})")
        print("0. Volver al menú principal")

        opcion = input("Selecciona un script para ver/ejecutar: ")
        if opcion == '0':
            break
        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta, scripts[idx][0])
                mostrar_codigo(ruta_script)
                ejecutar = input("¿Deseas ejecutar este script? (s/n): ")
                if ejecutar.lower() == 's':
                    ejecutar_script(ruta_script)
            else:
                print("Opción no válida.")
        except:
            print("Entrada inválida.")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrar_scripts_de_unidad('Unidad 1')
        elif opcion == '2':
            mostrar_scripts_de_unidad('Unidad 2')
        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()
