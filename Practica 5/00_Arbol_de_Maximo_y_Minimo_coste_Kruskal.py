## MAuricio Becerra g - 21310105 ###
class DisjointSet:
    def __init__(self, vertices):
        # Inicializa el conjunto disjunto con cada vertice como su propio padre y rango inicial 0
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v):
        # Encuentra la raiz del conjunto al que pertenece 'v' con compresion de ruta
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, root1, root2):
        # Une dos conjuntos basandose en los rangos
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

def kruskal(graph):
    # Lista de vertices en el grafo
    vertices = list(graph.keys())
    edges = []
    
    # Construir la lista de aristas (u, v, peso)
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))
    
    # Ordenar las aristas por peso
    edges.sort(key=lambda x: x[2])
    
    # Inicializar un DisjointSet para todos los vertices del grafo
    ds = DisjointSet(vertices)
    
    minimum_spanning_tree = []  # Lista para almacenar el arbol de minimo coste
    step_by_step = []  # Lista para almacenar los pasos intermedios
    
    # Iterar sobre las aristas ordenadas por peso
    for edge in edges:
        u, v, weight = edge
        
        # Encontrar las raices (conjuntos) de los vertices u y v
        root1 = ds.find(u)
        root2 = ds.find(v)
        
        # Si los vertices no estan en el mismo conjunto, unir los conjuntos y agregar la arista al arbol
        if root1 != root2:
            ds.union(root1, root2)
            minimum_spanning_tree.append(edge)
            step_by_step.append(minimum_spanning_tree[:])  # Copiar el estado actual del arbol paso a paso
            
            # Mostrar el estado actual del arbol paso a paso en la consola
            print(f"Edge added to MST: ({u}, {v}) - Weight: {weight}")
            print("Current MST:", minimum_spanning_tree)
            print()
    
    return minimum_spanning_tree, step_by_step

def print_steps(step_by_step):
    # Imprime los pasos intermedios para construir el arbol de minimo coste
    for i, step in enumerate(step_by_step):
        print(f"Step {i + 1}:")
        for edge in step:
            u, v, weight = edge
            print(f"({u}, {v}) - Weight: {weight}")
        print()

# Ejemplo de uso del algoritmo de Kruskal para encontrar el arbol de minimo coste
graph = {
    0: {1: 2, 3: 6},
    1: {0: 2, 2: 3, 3: 8, 4: 5},
    2: {1: 3, 4: 7},
    3: {0: 6, 1: 8, 4: 9},
    4: {1: 5, 2: 7, 3: 9},
}

minimum_spanning_tree, step_by_step = kruskal(graph)

# Imprimir los pasos intermedios para construir el arbol de minimo coste
print("Steps to build Minimum Spanning Tree (Kruskal's Algorithm):")
print_steps(step_by_step)
