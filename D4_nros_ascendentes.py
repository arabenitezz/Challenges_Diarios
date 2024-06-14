# Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

# Pedir una lista de números al usuario
usuario_nros = input('Escribe una serie de números separados por un espacio: ')

# Convertir lo que te da el usuario a una lista de números
lista_numeros = [int(num) for num in usuario_nros.split()]

# Función con algoritmo de ordenamiento burbuja
def ordenar_nros(numeros):
    intercambio = True
    while intercambio:
        intercambio = False
        for elemento in range(len(numeros) - 1):
            if numeros[elemento] > numeros[elemento + 1]:
                # Intercambiar los elementos
                numeros[elemento], numeros[elemento + 1] = numeros[elemento + 1], numeros[elemento]
                intercambio = True

# Llamar a la función y ordenar la lista
ordenar_nros(lista_numeros)

# Imprimir la lista ordenada
print(lista_numeros)

