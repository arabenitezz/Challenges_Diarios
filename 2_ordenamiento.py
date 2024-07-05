# Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento que
# prefieras (por ejemplo, burbuja, inserción, selección).

# Definir la lista de 5 numeros
lista = str(input('Escribe 5 numeros enteros'))

# Convertir lo que da el usuario a una lista

lista_usuario = [int(num) for num in lista.split()]

def ordenamiento(lista):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                # Intercambiar elementos
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambio = True
    return lista


# Llamar a la función de ordenamiento
lista_ordenada = ordenamiento(lista_usuario)
print("Lista ordenada:", lista_ordenada)
