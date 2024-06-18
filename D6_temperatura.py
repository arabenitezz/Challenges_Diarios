# Conversión de Temperatura: Escribe un programa que convierta una
# temperatura dada en grados Celsius a grados Fahrenheit.

# Capturamos la temperatura del usuario
temperatura_usuario = int(input('Ingrese una temperatura en grados Celsius: '))

# Definición de la función de conversión
def convertir_temperatura(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Llamada a la función y muestra del resultado
temperatura_fahrenheit = convertir_temperatura(temperatura_usuario)
print(f"{temperatura_usuario}°C es igual a {temperatura_fahrenheit}°F")

