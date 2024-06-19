### Mauricio Becerra G - 21310105 ###
import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.costo = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])

class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("El costo del vértice "+str(self.vertices[v].id)+" es "+ str(self.vertices[v].costo)+" llegando desde "+str(self.vertices[v].padre))

    def camino(self, a, b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].costo]

    def minimo(self, l):
        if len(l) > 0:
            m = self.vertices[l[0]].costo
            v = l[0]
            for e in l:
                if m > self.vertices[e].costo:
                    m = self.vertices[e].costo
                    v = e
            return v
        return None

    def dijkstra(self, a):
        if a in self.vertices:
            self.vertices[a].costo = 0
            actual = a
            noVisitados = []
            
            for v in self.vertices:
                if v != a:
                    self.vertices[v].costo = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)

            while len(noVisitados) > 0:
                for vec in self.vertices[actual].vecinos:
                    if self.vertices[vec[0]].visitado == False:
                        if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
                            self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
                            self.vertices[vec[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)

                actual = self.minimo(noVisitados)
        else:
            return False

# Crear instancia de la clase Grafica y agregar vértices y aristas
g = Grafica()
g.agregarVertice(1)
g.agregarVertice(2)
g.agregarVertice(3)
g.agregarVertice(4)
g.agregarVertice(5)
g.agregarVertice(6)
g.agregarArista(1, 6, 14)
g.agregarArista(1, 2, 7)
g.agregarArista(1, 3, 9)
g.agregarArista(2, 3, 10)
g.agregarArista(2, 4, 15)
g.agregarArista(3, 4, 11)
g.agregarArista(3, 6, 2)
g.agregarArista(4, 5, 6)
g.agregarArista(5, 6, 9)

# Ejecutar el algoritmo de Dijkstra desde el vértice 1
print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
g.dijkstra(1)
print(g.camino(1, 6))
print("\nLos valores finales de la gráfica son los siguietes:")
g.imprimirGrafica()

# Crear un grafo dirigido para visualizar con NetworkX
G = nx.DiGraph()

# Agregar nodos con sus atributos (costo y padre)
for v in g.vertices:
    G.add_node(v, costo=g.vertices[v].costo, padre=g.vertices[v].padre)

# Agregar aristas con sus pesos
for v in g.vertices:
    for vecino, peso in g.vertices[v].vecinos:
        G.add_edge(v, vecino, weight=peso)

# Obtener posiciones de los nodos para la visualización
pos = nx.spring_layout(G)

# Dibujar el grafo con etiquetas de costos y padres
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)





# Mostrar el grafo
plt.title('Grafo con pesos (Dijkstra)')
plt.show()
