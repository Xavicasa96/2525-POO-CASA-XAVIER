# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase derivada: Empleado, que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario  # Atributo encapsulado

    def obtener_salario(self):
        return self.__salario

    def establecer_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser positivo.")

    # Sobrescribimos el método para demostrar polimorfismo
    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: ${self.__salario}")

# Otra clase derivada: Consultor
class Consultor(Persona):
    def __init__(self, nombre, edad, proyecto):
        super().__init__(nombre, edad)
        self.proyecto = proyecto

    def mostrar_informacion(self):
        print(f"Consultor: {self.nombre}, Proyecto: {self.proyecto}")

# -------------------- DEMOSTRACIÓN ----------------------

# Crear instancias
persona1 = Persona("Ana", 30)
empleado1 = Empleado("Luis", 40, 2500)
consultor1 = Consultor("María", 35, "Transformación Digital")

# Mostrar información (polimorfismo)
persona1.mostrar_informacion()
empleado1.mostrar_informacion()
consultor1.mostrar_informacion()

# Encapsulación en acción
print("\nSalario actual:", empleado1.obtener_salario())
empleado1.establecer_salario(3000)
print("Salario actualizado:", empleado1.obtener_salario())

# Intento de establecer un salario inválido
empleado1.establecer_salario(-500)
