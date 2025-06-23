# Abstracción: Clase base con comportamiento común
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass  # Esto lo implementarán las clases hijas

# Herencia + Polimorfismo: Perro y Gato heredan de Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Encapsulación: Clase para manejar la edad de las mascotas
class Mascota:
    def __init__(self, animal, edad):
        self.animal = animal
        self.__edad = edad  # Atributo privado

    def obtener_edad(self):
        return self.__edad

    def mostrar_info(self):
        print(f"Nombre: {self.animal.nombre}")
        print(f"Edad: {self.obtener_edad()} años")
        print(f"Sonido: {self.animal.hacer_sonido()}")
        print("-" * 30)

# Uso del programa
def main():
    perro = Perro("Max")
    gato = Gato("Luna")

    mascota1 = Mascota(perro, 5)
    mascota2 = Mascota(gato, 3)

    mascota1.mostrar_info()
    mascota2.mostrar_info()

# Ejecutar
main()
