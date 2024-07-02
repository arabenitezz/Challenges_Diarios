# Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si
# un número está en una lista ordenada de 10 elementos.

# Definir lista de 10 numeros
import random
lista = random.sample(range(1, 51), 10)
lista.sort()

# Pedir un numero al usuario
numero = int(input('Ingrese un numero del 1 al 50: '))

# Funcion con busqueda binaria

def busqueda_binaria(lista, numero):
    inicio = 0
    fin = len(lista) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == numero:
            return True
        elif lista[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
            
    return False

resultado = busqueda_binaria(lista, numero)
print(f"Lista ordenada: {lista}")
print(f"Resultado de la búsqueda: {'Encontrado' if resultado else 'No encontrado'}")
