# clima

class SemanaClima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de cada día de la semana:")
        for i in range(1, 8):
            temp = float(input(f"Día {i}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / 7

    def mostrar_resultado(self):
        print("\n--- Resultado ---")
        print(f"Temperaturas ingresadas: {self.temperaturas}")
        print(f"Promedio semanal: {self.calcular_promedio():.2f}°C")

# Programa principal
semana = SemanaClima()
semana.ingresar_temperaturas()
semana.mostrar_resultado()
