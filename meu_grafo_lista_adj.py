from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não 
        adjacentes
        '''
        todas_comb: set[str] = set()
        conj_adj: set[str] = set()

        for ver1 in self.vertices:
            for ver2 in self.vertices:
                string_v = f'{str(ver1)}-{str(ver2)}'
                if ver1 != ver2 and string_v[::-1] not in todas_comb:
                    todas_comb.add(string_v)

        for aresta in self.arestas.values():
            string_a = f'{str(aresta.v1)}-{str(aresta.v2)}'
            conj_adj.add(string_a)
            conj_adj.add(string_a[::-1])

        resultado = todas_comb - conj_adj
        return resultado

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        print(self.arestas)
        for aresta in self.arestas.values():
            if aresta.v1 == aresta.v2:
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

        cont = 0
        for aresta in self.arestas.values():
            if aresta.v1.rotulo == V:
                cont += 1
            if aresta.v2.rotulo == V:
                cont += 1
        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no 
        grafo.
        '''
        vertices_arestas: tuple(Vertice) = [(str(aresta.v1), str(aresta.v2))
                                            for aresta in self.arestas.values()]

        tamanho_lista = len(vertices_arestas)  # Quantidade de arestas
        for i in range(tamanho_lista):
            incidencia = vertices_arestas[i]
            for j in range(i + 1, tamanho_lista):
                if incidencia == vertices_arestas[j] or \
                        tuple(reversed(incidencia)) == vertices_arestas[j]:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre 
        o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        lista: str = set()
        for aresta in self.arestas.values():
            if (aresta.v1.rotulo == V) or (aresta.v2.rotulo == V):
                lista.add(aresta.rotulo)
        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if self.ha_laco() or self.ha_paralelas():
            return False
        qnt_ver = len(self.vertices)
        qnt_are = len(self.arestas)

        return True if (qnt_ver * (qnt_ver - 1)) // 2 == qnt_are else False

    def dfs(self, V=''):
        novo_grafo = MeuGrafo()  # Novo grafo que será retornado

        # if self.ha_laco():
        #     return False

        if not self.existe_rotulo_vertice(V):  # Verificar se a raiz existe
            raise VerticeInvalidoError
        novo_grafo.adiciona_vertice(V)

        def percorrer(raiz):  # Função recursiva que percorre o grafo
            arestas_vertice: str = sorted(
                list(self.arestas_sobre_vertice(raiz)))
            # Lista com os vértices que incidem na raiz atual

            for aresta in arestas_vertice:
                # Itera a lista de arestas do vertice
                ver1 = str(self.arestas[aresta].v1)  # V1 da aresta
                ver2 = str(self.arestas[aresta].v2)  # V2 da aresta

                if novo_grafo.existe_rotulo_vertice(ver1) and \
                        novo_grafo.existe_rotulo_vertice(ver2):
                    continue

                prox = ver1 if ver1 != raiz else ver2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[aresta])
                percorrer(prox)

        percorrer(V)

        if len(self.vertices) != len(novo_grafo.vertices):
            return False

        return novo_grafo

    def bfs(self, V=''):
        novo_grafo = MeuGrafo()  # Novo grafo que será retornado

        if not self.existe_rotulo_vertice(V):  # Verificar se a raiz existe
            raise VerticeInvalidoError

        # if self.ha_laco():
        #     return False

        novo_grafo.adiciona_vertice(V)
        prox_vert: str = list()

        prox_vert.append(V)
        while prox_vert:
            vert_atual = prox_vert.pop(0)
            arestas_vertice: str = sorted(
                list(self.arestas_sobre_vertice(vert_atual)))

            for aresta in arestas_vertice:
                ver1 = str(self.arestas[aresta].v1)  # V1 da aresta
                ver2 = str(self.arestas[aresta].v2)  # V2 da aresta

                if novo_grafo.existe_rotulo_vertice(ver1) and \
                        novo_grafo.existe_rotulo_vertice(ver2):
                    continue

                prox = ver1 if ver1 != vert_atual else ver2
                novo_grafo.adiciona_vertice(prox)
                novo_grafo.adiciona_aresta(self.arestas[aresta])
                prox_vert.append(prox)

        if len(self.vertices) != len(novo_grafo.vertices):
            return False

        return novo_grafo

    def ha_ciclo(self):
        if (len(self.vertices) <= 2) and not (self.ha_laco()) and not \
                (self.ha_paralelas()) or (not len(self.arestas)):
            return False

        vertices_original = sorted([str(ver) for ver in self.vertices])

        vertice_raiz = vertices_original[0]
        caminho_ciclo = list()
        ciclo_encontrado = [False]
        arestas_visitadas = set()

        # Função recursiva que percorre o grafo
        def percorrer(raiz, encontrado):
            arestas_vertice: str = sorted(
                list(self.arestas_sobre_vertice(raiz)))
            # Lista com os vértices que incidem na raiz atual

            caminho_ciclo.append(raiz)
            for aresta in arestas_vertice:
                # Itera a lista de arestas do vertice
                ver1 = str(self.arestas[aresta].v1)  # V1 da aresta
                ver2 = str(self.arestas[aresta].v2)  # V2 da aresta

                if encontrado[0]:
                    return
                if aresta in arestas_visitadas:
                    continue
                if ver1 in caminho_ciclo and ver2 in caminho_ciclo:
                    caminho_ciclo.append(aresta)
                    caminho_ciclo.append(ver2 if ver1 == raiz else ver1)
                    encontrado[0] = True
                    return

                arestas_visitadas.add(aresta)
                prox = ver1 if ver1 != raiz else ver2
                caminho_ciclo.append(aresta)
                percorrer(prox, encontrado)

            if not encontrado[0]:
                if raiz != vertice_raiz:
                    caminho_ciclo.pop()
                caminho_ciclo.pop()

        percorrer(vertice_raiz, ciclo_encontrado)

        if not caminho_ciclo:
            return False

        inicio_ciclo = caminho_ciclo.index(caminho_ciclo[-1])
        caminho_ciclo = caminho_ciclo[inicio_ciclo:]

        return caminho_ciclo

    def caminho(self, n):

        if n < 1:
            return False

        lista_vertices = sorted([str(vert) for vert in self.vertices])
        arestas_visitadas = list()
        verts_visitados = set()
        vertice_raiz = lista_vertices[0]
        caminho_n = list()
        contador = 0

        def percorrer(raiz, tamanho):
            nonlocal contador, vertice_raiz
            arestas_vertice: str = sorted(
                list(self.arestas_sobre_vertice(raiz)))
            # Lista com os vértices que incidem na raiz atual

            caminho_n.append(raiz)
            for aresta in arestas_vertice:
                # Itera a lista de arestas do vertice
                ver1 = str(self.arestas[aresta].v1)  # V1 da aresta
                ver2 = str(self.arestas[aresta].v2)  # V2 da aresta

                if ver1 in caminho_n and ver2 in caminho_n:
                    continue

                if contador == tamanho:
                    break

                if aresta in arestas_visitadas:
                    continue

                arestas_visitadas.append(aresta)
                verts_visitados.add(ver1)
                verts_visitados.add(ver2)
                contador += 1
                prox = ver1 if ver1 != raiz else ver2
                caminho_n.append(aresta)
                percorrer(prox, n)

            if contador != n:
                if len(caminho_n) > 1:
                    caminho_n.pop()
                caminho_n.pop()
                if len(arestas_visitadas) > 0:
                    arestas_visitadas.pop()
                if contador > 0:
                    contador -= 1
            return contador

        resultado = percorrer(vertice_raiz, n)
        return caminho_n if caminho_n else False

    def conexo(self):
        vertices_original = self.vertices
        raiz = str(self.vertices[0])
        grafo_dfs = self.dfs(raiz)

        return False if not grafo_dfs else True


if __name__ == '__main__':
    grafo1 = MeuGrafo()
    grafo1.adiciona_vertice('A')
    grafo1.adiciona_vertice('B')
    grafo1.adiciona_vertice('C')
    grafo1.adiciona_aresta('a1', 'A', 'A')
    grafo1.adiciona_aresta('a2', 'A', 'B')
    grafo1.adiciona_aresta('a3', 'A', 'C')
    print(grafo1.conexo())
