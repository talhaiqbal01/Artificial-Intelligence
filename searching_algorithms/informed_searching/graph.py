"""
Graph Class
"""


class Graph:
    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    def add_edge(self, node, neighbor, cost=1):
        """
        Adds an edge in the graph with the given neighbor and cost
        :param node:
        :param neighbor:
        :param cost:
        :return:
        """
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append((neighbor, cost))

    def set_heuristic(self, node, value):
        """
        Sets the heuristic value for a node
        :param node:
        :param value:
        :return:
        """
        self.heuristics[node] = value
