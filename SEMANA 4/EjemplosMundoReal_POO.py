# EjemplosMundoReal_POO

class Persona:
    """Clase que representa a una persona con nombre y edad."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """Método para que la persona se presente."""
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Código de prueba
if __name__ == "__main__":
    persona1 = Persona("Ana", 25)
    persona2 = Persona("Carlos", 30)

    persona1.saludar()
    persona2.saludar()
#Este ejemplo muestra cómo modelar una persona con sus atributos básicos (nombre y edad) y un
#método para que se presente con un saludo.
#Es una forma sencilla de entender cómo funcionan las clases, atributos y métodos en la Programación Orientada a
#Objetos aplicados a un contexto real.

