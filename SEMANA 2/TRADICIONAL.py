# clima

def obtener_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de cada día de la semana:")
    for i in range(1, 8):
        temp = float(input(f"Día {i}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / 7

# Programa principal
temperaturas = obtener_temperaturas()
promedio = calcular_promedio(temperaturas)
print("\n--- Resultado ---")
print(f"Temperaturas ingresadas: {temperaturas}")
print(f"Promedio semanal: {promedio:.2f}°C")
