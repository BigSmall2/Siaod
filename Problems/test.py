from collections import defaultdict
from heapq import *
import math
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
import copy
from timeit import default_timer

# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = []  # словарь по умолчанию для хранения графов

    # Функция добавления ребра к графу
    def addEdge(self, u, v, w):   #v-число вершин в графе
        self.graph.append([u, v, w])

    # служебная функция, используемая для печати решения
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

        # Основная функция, которая находит кратчайшие расстояния от src до всех
        # остальных вершин, используя алгоритм Беллмана-Форда.
        # Функция также обнаруживает отрицательный цикл взвешивания.
    def BellmanFord(self, src):

        #Шаг 1: Инициализируйте расстояния от src до всех остальных вершин как INFINITE.
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Шаг 2: Ослабьте все ребра |V| - 1 раз.
        # Простой кратчайший путь из src в любую другую вершину может иметь не более чем |V| - 1 ребро
        for i in range(self.V - 1):
            # Обновите значение dist и родительский индекс смежных вершин выбранной вершины.
            # Учитывать только те вершины, которые еще находятся в очереди
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

                # Шаг 3: проверьте циклы отрицательного веса.
                # Вышеупомянутый шаг гарантирует кратчайшие расстояния, если граф не содержит отрицательный весовой цикл.
                # Если мы получим более короткий путь, то там является циклом.

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print
                "Graph contains negative weight cycle"
                return

        # распечатать все расстояние
        self.printArr(dist)

    def read_graph(filename):  # cчитывание графа из файла
        adj_matrix = list()
        graphfile = open(filename, 'r')
        for l in graphfile:
            l = l.split()
            for i in range(len(l)):
                l[i] = int(l[i])
            adj_matrix.append(l)
        graphfile.close()
        return adj_matrix

    def draw_graph(vertices, path):
        graph = nx.DiGraph(np.matrix(vertices))
        colors = []
        for item in graph.edges():
            catch = 0
            for i in range(len(path) - 1):
                if path[i] == item[0] and path[i + 1] == item[1]:
                    catch += 1
                    break
            if catch == 1:
                colors.append('red')
            else:
                colors.append('black')
        pos = nx.circular_layout(graph)  # positions for all nodes
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_nodes(graph, pos, node_size=250, node_color='royalblue')
        nx.draw_networkx_edges(graph, pos, edge_color=colors, arrows=True, arrowsize=10, width=2)
        nx.draw_networkx_labels(graph, pos, font_size=13, font_weight='bold', font_family='sans-serif')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=11, font_family='sans-serif')
        plt.axis('off')
        plt.show()

    def convert_adj_matrix(vertices):
        res = []
        for i in range(len(vertices)):
            res.append([])
            for j in range(len(vertices)):
                res[i].append(vertices[i][j])
                if vertices[i][j] == 0 and i != j:
                    res[i][j] = math.inf
        return res


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

# Print the solution
g.BellmanFord(0)

