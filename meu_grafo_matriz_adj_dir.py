from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''

        e = [[1 if obj else 0 for obj in row] for row in self.arestas]
        qnt_verts = len(self.vertices)
        

        for i in range(qnt_verts):
            for j in range(qnt_verts):
                if e[j][i]:
                    for k in range(qnt_verts):
                        e[j][k] = max(e[j][k], e[i][k])
        return e


if __name__ == '__main__':
    # grafo1 = MeuGrafo()
    # grafo1.adiciona_vertice('A')
    # grafo1.adiciona_vertice('B')
    # grafo1.adiciona_vertice('C')
    # grafo1.adiciona_vertice('D')
    # grafo1.adiciona_aresta('a1', 'A', 'B')
    # grafo1.adiciona_aresta('a2', 'B', 'C')
    # grafo1.adiciona_aresta('a3', 'C', 'D')
    # grafo1.warshall()
    ...