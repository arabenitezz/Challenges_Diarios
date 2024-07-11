# Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que encuentre el camino más
# corto entre dos nodos especificados usando cualquier método que prefieras.
import heapq

# Crear grafo con 5 nodos y 6 aristas
grafo = {
    1: {2: 1, 3: 1, 4: 1},
    2: {1: 1, 4: 1},
    3: {1: 1, 5: 1},
    4: {1: 1, 2: 1, 5: 1},
    5: {3: 1, 4: 1}
}

# Crear funcion

def dijkstra(grafo, inicio, fin):
    cola_prioridad = [(0, inicio)]
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    camino = {nodo: None for nodo in grafo}
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            break
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    # Reconstruir el camino más corto
    camino_corto = []
    nodo = fin
    while nodo is not None:
        camino_corto.append(nodo)
        nodo = camino[nodo]
    
    return camino_corto[::-1]


print(grafo)

# Pedir al usuario que ingrese los nodos
nodo_1 = int(input('Elija un nodo de inicio: '))
nodo_2 = int(input('Elija un nodo de fin: '))

if nodo_1 not in grafo or nodo_2 not in grafo:
    print('Escriba un nodo válido')
else:
    camino_corto = dijkstra(grafo, nodo_1, nodo_2)
    print(f'El camino más corto entre {nodo_1} y {nodo_2} es: {camino_corto}')



