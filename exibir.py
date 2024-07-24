import matplotlib.pyplot as plt
import networkx as nx
from meu_grafo_lista_adj import *
# Função para visualizar um grafo


def visualizar_grafo(grafo):
    G = nx.Graph()
    for v in grafo.vertices:
        G.add_node(str(v))
    for a in grafo.arestas.values():
        G.add_edge(str(a.v1.rotulo), str(a.v2.rotulo))
    nx.draw(G, with_labels=True)
    plt.show()


# Exemplo de uso
grafo1 = MeuGrafo()
grafo1.adiciona_vertice("J")
grafo1.adiciona_vertice("C")
grafo1.adiciona_vertice("E")
grafo1.adiciona_vertice("P")
grafo1.adiciona_aresta('a1', 'J', 'C')
grafo1.adiciona_aresta('a2', 'J', 'E')
grafo1.adiciona_aresta('a3', 'J', 'P')
grafo1.adiciona_aresta('a4', 'E', 'C')
grafo1.adiciona_aresta('a5', 'P', 'C')
grafo1.adiciona_aresta('a6', 'P', 'E')
['C', 'a1', 'J', 'a2', 'E', 'a6', 'P']
visualizar_grafo(grafo1)
