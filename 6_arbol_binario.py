# Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.

# Creamos una clase nodo para los elementos del árbol binario
class Nodo: 
    def __init__(self, valor):
        self.izquierda = None
        self.derecha = None
        self.val = valor
    
# Función para insertar los elementos
def insertar(raiz, valor):
    # Si el árbol está vacío, darle un valor
    if raiz is None:
        return Nodo(valor)
    
    # Si ya tiene valor, recorre el árbol
    # Izquierda menor, Derecha mayor
    if valor < raiz.val:
        raiz.izquierda = insertar(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar(raiz.derecha, valor)

    # Devolvemos el nodo
    return raiz

# Creación del árbol e inserción de 5 elementos
raiz = None
elementos = [50, 30, 20, 40, 70]

for elemento in elementos:
    raiz = insertar(raiz, elemento)


