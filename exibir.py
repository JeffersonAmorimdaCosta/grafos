import matplotlib.pyplot as plt
import networkx as nx
from meu_grafo_lista_adj import *
# Função para visualizar um grafo


def visualizar_grafo(grafo, layout='spring'):
    G = nx.DiGraph()  # Usar DiGraph para grafos direcionados
    for v in grafo.vertices:
        G.add_node(str(v))
    for a in grafo.arestas.values():
        G.add_edge(str(a.v1.rotulo), str(a.v2.rotulo),
                   weight=a.peso, label=str(a.peso))

    plt.figure(figsize=(10, 5))  # Ajustar o tamanho da figura

    # Escolher o layout
    if layout == 'spring':
        pos = nx.spring_layout(G, k=0.5, iterations=50)
    elif layout == 'shell':
        pos = nx.shell_layout(G)
    elif layout == 'spectral':
        pos = nx.spectral_layout(G)
    elif layout == 'kamada_kawai':
        pos = nx.kamada_kawai_layout(G)
    else:
        pos = nx.spring_layout(G, k=0.5, iterations=50)

    nx.draw(G, pos, with_labels=True, node_size=400, node_color='lightblue', font_size=10, font_weight='bold',
            arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='red')

    plt.show()


# Exemplo de uso
grafo1 = MeuGrafo()
grafo1.adiciona_vertice("J")
grafo1.adiciona_vertice("C")
grafo1.adiciona_vertice("E")
grafo1.adiciona_vertice("P")
grafo1.adiciona_aresta('a1', 'J', 'C', 1)
grafo1.adiciona_aresta('a2', 'J', 'E', 3)
grafo1.adiciona_aresta('a3', 'J', 'P', 5)
grafo1.adiciona_aresta('a4', 'E', 'C', 2)
grafo1.adiciona_aresta('a5', 'P', 'C', 8)
grafo1.adiciona_aresta('a6', 'P', 'E', 1)
visualizar_grafo(grafo1)
