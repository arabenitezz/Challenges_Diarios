# Pedir al usuario un número
pregunta = int(input('Ingrese un numero: '))

# Crear la función de tabla de multiplicar
def tabla_multiplicar(numero):
    for n in range(1, 11):  # De 1 a 10
        print(f'{numero} * {n} = {numero * n}')

# Llamar a la función con el número ingresado
tabla_multiplicar(pregunta)
