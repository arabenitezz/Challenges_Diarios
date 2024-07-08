# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.

def dfs(grafo, nodo_inicial):

  visitados = set()  # Conjunto para almacenar los nodos ya visitados
  pila = [nodo_inicial]  # Pila para almacenar los nodos por explorar

  while pila:
    nodo_actual = pila.pop()  # Se extrae el último nodo de la pila
    visitados.add(nodo_actual)  # Se marca el nodo actual como visitado

    for nodo_adyacente in grafo[nodo_actual]:
      if nodo_adyacente not in visitados:
        pila.append(nodo_adyacente)  # Se agrega el nodo adyacente a la pila

  print("Recorrido DFS:", end=" ")
  for nodo in visitados:
    print(nodo, end=" ")

# Creamos un grafo para llamar a la funcion
grafo = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
dfs(grafo, 'A')

