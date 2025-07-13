class Persona:
    def __init__(self, nombre, edad):
        # Esto se ejecuta cuando se crea el objeto (el constructor)
        # Aquí simplemente guardamos el nombre y la edad que nos pasan
        self.nombre = nombre
        self.edad = edad
        print(f"[Constructor] Se ha creado la persona: {self.nombre}, {self.edad} años.")

    def mostrar_datos(self):
        # Esta función solo imprime el nombre y la edad
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __del__(self):
        # Esto se ejecuta cuando el objeto se destruye (al final del programa o cuando ya no se usa)
        print(f"[Destructor] Se ha eliminado la persona: {self.nombre}.")

# ===================
# Parte principal del programa
# ===================

def main():
    # Creamos una persona llamada Ana, que tiene 30 años
    persona1 = Persona("Ana", 30)

    # Mostramos sus datos en pantalla
    persona1.mostrar_datos()

    # No necesitamos borrar nada a mano, Python lo hace solo y llama al destructor al final

if __name__ == "__main__":
    main()
