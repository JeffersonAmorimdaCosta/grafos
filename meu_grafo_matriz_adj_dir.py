from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o
        seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        nao_adjacentes = set()
        vertices = [str(vertice) for vertice in self.vertices]

        for vertice in vertices:
            adjacentes = set()
            for str_aresta in sorted(self.arestas_sobre_vertice(vertice)):
                aresta = self.get_aresta(str_aresta)
                v1 = str(aresta.v1)
                v2 = str(aresta.v2)

                if v2 == vertice:
                    continue

                adjacentes.add(v1 if v1 != vertice else v2)

            for vert in vertices:
                if vert not in adjacentes and vert != vertice:
                    nao_adjacentes.add(f'{vertice}-{vert}')
        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        vertices = [str(vertice) for vertice in self.vertices]
        str_arestas = [
            aresta for vertice in vertices for aresta in
            self.arestas_sobre_vertice(vertice)]

        for str_aresta in str_arestas:
            aresta = self.get_aresta(str_aresta)
            if aresta.v1 == aresta.v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = self.arestas_sobre_vertice(V)
        cont = 0

        for rotulo_aresta in arestas:
            aresta = self.get_aresta(rotulo_aresta)
            if str(aresta.v1) == V:
                cont += 1
            if str(aresta.v2) == V:
                cont += 1
        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no
        grafo.
        '''

        for row in self.arestas:
            for obj in row:
                if len(obj) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o
        vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = set()
        for linha in self.arestas:
            for dicionario in linha:
                for aresta in dicionario.values():
                    if str(aresta.v1) == V or str(aresta.v2) == V:
                        arestas.add(aresta.rotulo)
        return arestas

    def arestas_sobre_vertice_dir(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas direcionados que saem
        do vértice passado como parâmetro.
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        arestas = set()
        for linha in self.arestas:
            for dicionario in linha:
                for aresta in dicionario.values():
                    if str(aresta.v1) == V:
                        arestas.add(aresta.rotulo)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        if len(self.vertices_nao_adjacentes()) > 0 or self.ha_laco() or \
                self.ha_paralelas():
            return False
        return True

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade
        de Warshall associada ao grafo
        '''

        e = [[1 if obj else 0 for obj in row] for row in self.arestas]
        qnt_verts = len(self.vertices)

        for i in range(qnt_verts):
            for j in range(qnt_verts):
                if e[j][i]:
                    for k in range(qnt_verts):
                        e[j][k] = max(e[j][k], e[i][k])
        return e

    def dijkstra(self, u: str, v: str) -> list[str] | bool:
        """
        Encontra o menor caminho entre o vértice u e v.
        :param u: Primeiro vértice do caminho.
        :param v: último vértice do caminho.
        :return : Uma lista com a ordem dos vértices do menor caminho ou False
        se o caminho não existir.
        :raises: VerticeInvalidoException se os vértices não existirem no grafo
        """

        if not self.existe_rotulo_vertice(u) or not self.existe_rotulo_vertice(v):
            raise VerticeInvalidoError

        vertices: dict = {}

        def get_beta(v: str):
            return vertices[v]['beta']

        def get_phi(v: str):
            return vertices[v]['phi']

        def get_pi(v: str):
            return vertices[v]['pi']

        # Definindo os valores iniciais para beta, phi e pi

        for vertice in self.vertices:
            str_vertice: str = str(vertice)

            if str_vertice == u:
                vertices.update(
                    {str_vertice: {'beta': 0.0, 'phi': 1, 'pi': None}})
            else:
                vertices.update({str_vertice: {'beta': float('inf'), 'phi': 0,
                                               'pi': None}})

        # Definindo w como u
        w = u
        vertices_nao_visitados: set[str] = {str(vert) for vert in
                                            self.vertices}
        while w != v:
            vertices_nao_visitados.remove(w)

            # Definindo os betas dos vértices adjacentes a w
            arestas: list[str] = sorted(self.arestas_sobre_vertice_dir(w))

            for aresta in arestas:
                obj_aresta = self.get_aresta(aresta)
                v_adjacente = str(obj_aresta.v2)

                if get_beta(v_adjacente) > get_beta(w) + obj_aresta.peso:
                    vertices[v_adjacente]['beta'] = obj_aresta.peso + \
                        get_beta(w)
                    vertices[v_adjacente]['pi'] = w

            # Escolhendo o próximo w com base no menor beta e phi = 0
            menor: str | None = None
            for vertice in vertices_nao_visitados:
                if not get_phi(vertice) and get_pi(vertice) is not None and \
                        (menor is None or get_beta(vertice) < get_beta(menor)):
                    menor = vertice

            # Definindo o próximo w
            if menor is not None:
                w = menor
                vertices[w]['phi'] = 1
            else:
                return False

        # Criando o caminho pegando a partir do último vértice
        atual = w
        caminho: list[str] = []
        while atual != u:
            caminho.append(atual)
            atual = get_pi(atual)

        caminho.append(u)
        caminho.reverse()
        return caminho

    def bellman_ford(self, u: str, v: str) -> list[str] | bool:
        """
        Encontra o menor caminho entre o vértice u e v.
        :param u: Primeiro vértice do caminho.
        :param v: último vértice do caminho.
        :return : Uma lista com a ordem dos vértices do menor caminho ou False
        se o caminho não existir ou se houver ciclos negativos.
        :raises: VerticeInvalidoException se os vértices não existirem no grafo
        """

        if not self.existe_rotulo_vertice(u) or not self.existe_rotulo_vertice(v):
            raise VerticeInvalidoError

        vertices: dict = {}

        def get_beta(v: str):
            return vertices[v]['beta']

        def get_pi(v: str):
            return vertices[v]['pi']

        # Definindo os valores iniciais para beta, phi e pi
        for vertice in self.vertices:
            str_vertice: str = str(vertice)

            if str_vertice == u:
                vertices.update(
                    {str_vertice: {'beta': 0.0, 'phi': 1, 'pi': None}})
            else:
                vertices.update({str_vertice: {'beta': float('inf'), 'phi': 0,
                                               'pi': None}})

        qnt_vertices: int = len(self.vertices)
        vertices_alterados: set[str] = set()
        vertices_alterados.add(u)

        for _ in range(qnt_vertices):
            ultimos_vertices: set[str] = set()

            for vert in vertices_alterados:
                arestas: list[str] = sorted(
                    list(self.arestas_sobre_vertice_dir(vert)))

                for aresta in arestas:
                    obj_aresta = self.get_aresta(aresta)
                    vert_adjacente = str(obj_aresta.v2)

                    novo_beta = get_beta(vert) + obj_aresta.peso

                    if get_beta(vert_adjacente) > novo_beta:
                        vertices[vert_adjacente]['beta'] = novo_beta
                        vertices[vert_adjacente]['pi'] = vert

                        ultimos_vertices.add(vert_adjacente)

            if not ultimos_vertices:
                # Criando o caminho pegando a partir do último vértice
                atual = v
                caminho: list[str] = []

                while atual != u:
                    if atual is None:
                        return False
                    caminho.append(atual)
                    atual = get_pi(atual)

                caminho.append(u)
                caminho.reverse()
                return caminho
            vertices_alterados = ultimos_vertices

        return False
