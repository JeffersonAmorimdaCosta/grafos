from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''
        nao_adjacentes = set()
        todos_vert = [str(v) for v in self.vertices]

        for v in todos_vert:
            arestas_vert = self.arestas_sobre_vertice(v)
            adjacentes = set()

            for a in arestas_vert:
                obj_aresta = self.get_aresta(a)
                rot_v1 = str(obj_aresta.v1)
                rot_v2 = str(obj_aresta.v2)
                if rot_v1 != v:
                    adjacentes.add(rot_v1)
                elif rot_v2 != v:
                    adjacentes.add(rot_v2)

            for nao_adj in set(todos_vert) - adjacentes:
                string = f'{v}-{nao_adj}'
                if nao_adj != v and string[::-1] not in nao_adjacentes:
                    nao_adjacentes.add(string)

        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.arestas)):
            if len(self.arestas[i][i]) > 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        indice = self.indice_do_vertice(self.get_vertice(V))
        contador = 0
        for dict_aresta in self.arestas[indice]:
            for aresta in dict_aresta.values():
                if str(aresta.v1) == V:
                    contador += 1
                if str(aresta.v2) == V:
                    contador += 1
        return contador

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.arestas)):
            for j in range(len(self.arestas)):
                if len(self.arestas[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        incidencia = set()
        indice = self.indice_do_vertice(self.get_vertice(V))
        for dict_aresta in self.arestas[indice]:
            for aresta in dict_aresta.keys():
                incidencia.add(aresta)
        return incidencia

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if self.ha_laco() and self.ha_paralelas():
            return False

        qnt_ver = len(self.vertices)
        qnt_are = sum([len(self.arestas_sobre_vertice(str(v))) /
                       2 for v in self.vertices])

        return True if (qnt_ver * (qnt_ver - 1)) / 2 == qnt_are else False


if __name__ == '__main__':
    g_p = MeuGrafo()
    g_p.adiciona_vertice("J")
    g_p.adiciona_vertice("C")
    g_p.adiciona_vertice("E")
    g_p.adiciona_vertice("P")
    g_p.adiciona_vertice("M")
    g_p.adiciona_vertice("T")
    g_p.adiciona_vertice("Z")
    g_p.adiciona_aresta('a1', 'J', 'C')
    g_p.adiciona_aresta('a2', 'C', 'E')
    g_p.adiciona_aresta('a3', 'C', 'E')
    g_p.adiciona_aresta('a4', 'P', 'C')
    g_p.adiciona_aresta('a5', 'P', 'C')
    g_p.adiciona_aresta('a6', 'T', 'C')
    g_p.adiciona_aresta('a7', 'M', 'C')
    g_p.adiciona_aresta('a8', 'M', 'T')
    g_p.adiciona_aresta('a9', 'T', 'Z')
    print(g_p.vertices_nao_adjacentes())
