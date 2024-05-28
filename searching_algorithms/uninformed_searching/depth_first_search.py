"""
Depth First Search Class
"""


class DepthFirstSearch:

    def depth_first_search(self, graph, start, target, visited=None, path=None):
        """
        Applies Depth First Search on the given graph, starting node and target node
        :param graph:
        :param start:
        :param target:
        :param visited:
        :param path:
        :return:
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start)
        path = path + [start]
        print("Visiting:", start)

        if start == target:
            print("Found target:", target, "at path:", path)
            return

        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                self.depth_first_search(graph, neighbor, target, visited, path)

    def dfs_wrapper(self, graph, start, target):
        """
        Starts Depth First Search on the given graph
        :param graph:
        :param start:
        :param target:
        :return:
        """
        print("Depth First Search:")
        self.depth_first_search(graph, start, target)
