"""
Breath First Search Class
"""


class BreathFirstSearch:

    @staticmethod
    def breath_first_search(graph, start, target):
        """
        Applies Breath First Search on the given graph, starting node and target node
        :param graph:
        :param start:
        :param target:
        :return:
        """
        visited = set()
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            print("Visiting:", current)
            if current == target:
                print("Found target:", target, "at path:", path)
                return
            if current not in visited:
                visited.add(current)
                neighbors = graph.get(current, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        print("Target", target, "not found in the graph.")

    def bfs_wrapper(self, graph, start, target):
        """
        Starts Breath First Search on the given graph
        :param graph:
        :param start:
        :param target:
        :return:
        """
        print("Breath First Search:")
        self.breath_first_search(graph, start, target)
