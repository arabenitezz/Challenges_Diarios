
# Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.

def dfs(grafo, nodo_inicial):

  visitados = set()  # Conjunto para almacenar los nodos ya visitados
  cola = [nodo_inicial]  # cola para almacenar los nodos por explorar

  while cola:
    nodo_actual = cola.pop(0)  # Se extrae el primer nodo de la cola
    visitados.add(nodo_actual)  # Se marca el nodo actual como visitado

    for nodo_adyacente in grafo[nodo_actual]:
      if nodo_adyacente not in visitados:
        cola.append(nodo_adyacente)  # Se agrega el nodo adyacente a la cola

  print("Recorrido DFS:", end=" ")
  for nodo in visitados:
    print(nodo, end=" ")

# Creamos un grafo para llamar a la funcion
grafo = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
dfs(grafo, 'A')