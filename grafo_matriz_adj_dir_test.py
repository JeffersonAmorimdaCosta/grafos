import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
import sys


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        self.g_p5 = MeuGrafo()
        self.g_p5.adiciona_vertice("J")
        self.g_p5.adiciona_vertice("C")
        self.g_p5.adiciona_vertice("E")
        self.g_p5.adiciona_vertice("P")
        self.g_p5.adiciona_vertice("M")
        self.g_p5.adiciona_vertice("T")
        self.g_p5.adiciona_vertice("Z")
        self.g_p5.adiciona_aresta('a1', 'J', 'C')
        self.g_p5.adiciona_aresta('a2', 'Z', 'J')
        self.g_p5.adiciona_aresta('a3', 'C', 'E')
        self.g_p5.adiciona_aresta('a4', 'P', 'C')
        self.g_p5.adiciona_aresta('a5', 'C', 'T')
        self.g_p5.adiciona_aresta('a6', 'T', 'C')
        self.g_p5.adiciona_aresta('a7', 'E', 'M')
        self.g_p5.adiciona_aresta('a8', 'M', 'T')
        self.g_p5.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        self.g_c4 = MeuGrafo()
        self.g_c4.adiciona_vertice("J")
        self.g_c4.adiciona_vertice("C")
        self.g_c4.adiciona_vertice("E")
        self.g_c4.adiciona_vertice("P")
        self.g_c4.adiciona_aresta('a1', 'J', 'C')
        self.g_c4.adiciona_aresta('a2', 'J', 'E')
        self.g_c4.adiciona_aresta('a3', 'J', 'P')
        self.g_c4.adiciona_aresta('a4', 'C', 'J')
        self.g_c4.adiciona_aresta('a5', 'C', 'E')
        self.g_c4.adiciona_aresta('a6', 'C', 'P')
        self.g_c4.adiciona_aresta('a7', 'E', 'J')
        self.g_c4.adiciona_aresta('a8', 'E', 'C')
        self.g_c4.adiciona_aresta('a9', 'E', 'P')
        self.g_c4.adiciona_aresta('a10', 'P', 'J')
        self.g_c4.adiciona_aresta('a11', 'P', 'C')
        self.g_c4.adiciona_aresta('a12', 'P', 'E')

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Grafo ABCDEFG com varios ciclos
        self.g_a = MeuGrafo()
        self.g_a.adiciona_vertice("A")
        self.g_a.adiciona_vertice("B")
        self.g_a.adiciona_vertice("C")
        self.g_a.adiciona_vertice("D")
        self.g_a.adiciona_vertice("E")
        self.g_a.adiciona_vertice("F")
        self.g_a.adiciona_vertice("G")
        self.g_a.adiciona_aresta('a1', 'A', 'B')
        self.g_a.adiciona_aresta('a2', 'B', 'C')
        self.g_a.adiciona_aresta('a3', 'C', 'D')
        self.g_a.adiciona_aresta('a4', 'D', 'E')
        self.g_a.adiciona_aresta('a5', 'E', 'F')
        self.g_a.adiciona_aresta('a6', 'F', 'G')
        self.g_a.adiciona_aresta('a7', 'G', 'A')
        self.g_a.adiciona_aresta('a8', 'B', 'D')
        self.g_a.adiciona_aresta('a9', 'C', 'F')

        # Grafo XYZWVUT com varios ciclos
        self.g_x = MeuGrafo()
        self.g_x.adiciona_vertice("X")
        self.g_x.adiciona_vertice("Y")
        self.g_x.adiciona_vertice("Z")
        self.g_x.adiciona_vertice("W")
        self.g_x.adiciona_aresta('a1', 'X', 'W')
        self.g_x.adiciona_aresta('a2', 'W', 'Y')
        self.g_x.adiciona_aresta('a3', 'Z', 'W')
        self.g_x.adiciona_aresta('a4', 'Z', 'Y')

        # Grafo LMNOPQR com varios ciclos
        self.g_r = MeuGrafo()
        self.g_r.adiciona_vertice("L")
        self.g_r.adiciona_vertice("M")
        self.g_r.adiciona_vertice("N")
        self.g_r.adiciona_vertice("O")
        self.g_r.adiciona_vertice("P")
        self.g_r.adiciona_aresta('a1', 'L', 'P')
        self.g_r.adiciona_aresta('a2', 'P', 'M')
        self.g_r.adiciona_aresta('a3', 'M', 'L')
        self.g_r.adiciona_aresta('a4', 'N', 'O')

        # Grafo ABC com ciclo completo

        self.g_c_c = MeuGrafo()
        self.g_c_c.adiciona_vertice('A')
        self.g_c_c.adiciona_vertice('B')
        self.g_c_c.adiciona_vertice('C')
        self.g_c_c.adiciona_aresta('a1', 'A', 'B')
        self.g_c_c.adiciona_aresta('a2', 'A', 'C')
        self.g_c_c.adiciona_aresta('a3', 'B', 'A')
        self.g_c_c.adiciona_aresta('a4', 'B', 'C')
        self.g_c_c.adiciona_aresta('a5', 'C', 'A')
        self.g_c_c.adiciona_aresta('a6', 'C', 'B')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        # Matriz grafo paraiba sem Paralelas
        self.g_p_m2 = self.constroi_matriz(self.g_p_sem_paralelas)
        self.g_p_m2[0][1] = 1
        self.g_p_m2[0][2] = 1
        self.g_p_m2[1][2] = 1
        self.g_p_m2[3][1] = 1
        self.g_p_m2[3][2] = 1
        self.g_p_m2[4][1] = 1
        self.g_p_m2[4][2] = 1
        self.g_p_m2[4][5] = 1
        self.g_p_m2[4][6] = 1
        self.g_p_m2[5][1] = 1
        self.g_p_m2[5][2] = 1
        self.g_p_m2[5][6] = 1

        # Matriz grafo paraiba com ciclo
        self.g_p_m3 = self.constroi_matriz(self.g_p5)
        self.g_p_m3[0][0] = 1
        self.g_p_m3[0][1] = 1
        self.g_p_m3[0][2] = 1
        self.g_p_m3[0][4] = 1
        self.g_p_m3[0][5] = 1
        self.g_p_m3[0][6] = 1
        self.g_p_m3[1][0] = 1
        self.g_p_m3[1][1] = 1
        self.g_p_m3[1][2] = 1
        self.g_p_m3[1][4] = 1
        self.g_p_m3[1][5] = 1
        self.g_p_m3[1][6] = 1
        self.g_p_m3[2][0] = 1
        self.g_p_m3[2][1] = 1
        self.g_p_m3[2][2] = 1
        self.g_p_m3[2][4] = 1
        self.g_p_m3[2][5] = 1
        self.g_p_m3[2][6] = 1
        self.g_p_m3[3][0] = 1
        self.g_p_m3[3][1] = 1
        self.g_p_m3[3][2] = 1
        self.g_p_m3[3][4] = 1
        self.g_p_m3[3][5] = 1
        self.g_p_m3[3][6] = 1
        self.g_p_m3[4][0] = 1
        self.g_p_m3[4][1] = 1
        self.g_p_m3[4][2] = 1
        self.g_p_m3[4][4] = 1
        self.g_p_m3[4][5] = 1
        self.g_p_m3[4][6] = 1
        self.g_p_m3[5][0] = 1
        self.g_p_m3[5][1] = 1
        self.g_p_m3[5][2] = 1
        self.g_p_m3[5][4] = 1
        self.g_p_m3[5][5] = 1
        self.g_p_m3[5][6] = 1
        self.g_p_m3[6][0] = 1
        self.g_p_m3[6][1] = 1
        self.g_p_m3[6][2] = 1
        self.g_p_m3[6][4] = 1
        self.g_p_m3[6][5] = 1
        self.g_p_m3[6][6] = 1

        # Matriz grafo completo
        self.g_c_m = self.constroi_matriz(self.g_c)
        self.g_c_m[0][1] = 1
        self.g_c_m[0][2] = 1
        self.g_c_m[0][3] = 1
        self.g_c_m[2][1] = 1
        self.g_c_m[3][1] = 1
        self.g_c_m[3][2] = 1

        # Matriz grafo com laço
        self.g_l3_m = self.constroi_matriz(self.g_l3)
        self.g_l3_m[2][0] = 1
        self.g_l3_m[2][2] = 1
        self.g_l3_m[3][3] = 1

        # Matriz grafo desconexo
        self.g_d_m = self.constroi_matriz(self.g_d)
        self.g_d_m[0][1] = 1

        # Matriz com ciclo completo
        self.g_c_c_m = self.constroi_matriz(self.g_c_c)
        self.g_c_c_m[0][0] = 1
        self.g_c_c_m[0][1] = 1
        self.g_c_c_m[0][2] = 1
        self.g_c_c_m[1][0] = 1
        self.g_c_c_m[1][1] = 1
        self.g_c_c_m[1][2] = 1
        self.g_c_c_m[2][0] = 1
        self.g_c_c_m[2][1] = 1
        self.g_c_c_m[2][2] = 1

        # Matriz sem arestas
        self.g_c3_m = self.constroi_matriz(self.g_c3)

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        # Matrizes geradas
        self.g_a_m = self.constroi_matriz(self.g_a)
        for i in range(len(self.g_a_m)):
            for j in range(len(self.g_a_m)):
                self.g_a_m[i][j] = 1

        self.g_x_m = self.constroi_matriz(self.g_x)
        self.g_x_m[0][1] = 1
        self.g_x_m[0][3] = 1
        self.g_x_m[2][1] = 1
        self.g_x_m[2][3] = 1
        self.g_x_m[3][1] = 1

        self.g_r_m = self.constroi_matriz(self.g_r)
        self.g_r_m[0][0] = 1
        self.g_r_m[0][1] = 1
        self.g_r_m[0][4] = 1
        self.g_r_m[1][0] = 1
        self.g_r_m[1][1] = 1
        self.g_r_m[1][4] = 1
        self.g_r_m[2][3] = 1
        self.g_r_m[4][0] = 1
        self.g_r_m[4][1] = 1
        self.g_r_m[4][4] = 1

        # Grafos desconexos
        self.g_dijkstra = MeuGrafo()
        self.g_dijkstra.adiciona_vertice("A")
        self.g_dijkstra.adiciona_vertice("B")
        self.g_dijkstra.adiciona_vertice("C")
        self.g_dijkstra.adiciona_vertice("D")
        self.g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
        self.g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
        self.g_dijkstra.adiciona_aresta('3', 'B', 'D', 1)
        self.g_dijkstra.adiciona_aresta('2', 'C', 'D', 2)

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g._vertices)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice(
            "C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                                                              'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), {
                         'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_e.vertices_nao_adjacentes(), {
                         'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {
                         'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'),
                         {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(self.g_e.arestas_sobre_vertice('D'),
                         {'5', '6', '7', '8'})

    def test_eh_completo(self):
        self.assertFalse(self.g_c.eh_completo())
        self.assertFalse(self.g_c2.eh_completo())
        self.assertTrue(self.g_c3.eh_completo())
        self.assertTrue(self.g_c4.eh_completo())

    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)
        self.assertEqual(self.g_p_sem_paralelas.warshall(), self.g_p_m2)
        self.assertEqual(self.g_c.warshall(), self.g_c_m)
        self.assertEqual(self.g_l3.warshall(), self.g_l3_m)
        self.assertEqual(self.g_p5.warshall(), self.g_p_m3)
        self.assertEqual(self.g_d.warshall(), self.g_d_m)
        self.assertEqual(self.g_a.warshall(), self.g_a_m)
        self.assertEqual(self.g_x.warshall(), self.g_x_m)
        self.assertEqual(self.g_r.warshall(), self.g_r_m)
        self.assertEqual(self.g_c_c.warshall(), self.g_c_c_m)
        self.assertEqual(self.g_c3.warshall(), self.g_c3_m)

    def test_dijkstra(self):
        pass


if __name__ == '__main__':
    loader = unittest.TestLoader()
    teste = loader.loadTestsFromName(sys.argv[0].replace(
        '.py', '') + '.TestGrafo.' + sys.argv[1])
    # teste = loader.loadTestsFromName('grafo_matriz_adj_dir_test.TestGrafo.test_vertices_nao_adjacentes')
    runner = unittest.TextTestRunner()
    runner.run(teste)
