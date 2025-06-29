# Programa para convertir grados Celsius a Fahrenheit
# Autor: [Tu nombre]
# Este programa pide al usuario una temperatura en grados Celsius y muestra su equivalente en Fahrenheit.

def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicitar temperatura al usuario
temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir la temperatura
temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

# Mostrar el resultado
print("La temperatura en grados Fahrenheit es:", temperatura_fahrenheit)

# Tipos de datos adicionales
es_frio = temperatura_celsius < 15  # booleano
mensaje = "Hace frío" if es_frio else "Hace calor"  # string
print("Comentario:", mensaje)
