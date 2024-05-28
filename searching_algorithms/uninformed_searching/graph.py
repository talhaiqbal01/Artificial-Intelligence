"""
Graph Class
"""


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """
        Adds an edge in the graph with the given neighbor
        :param node:
        :param neighbor:
        :return:
        """
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
