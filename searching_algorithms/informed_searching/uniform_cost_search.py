"""
Uniform Cost Search Class
"""
import heapq


class UniformCostSearch:
    @staticmethod
    def uniform_cost_search(graph, start, target):
        """
        Applies Uniform Cost Search on the given graph, starting node and target node
        :param graph:
        :param start:
        :param target:
        :return:
        """
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            (cost, current, path) = heapq.heappop(priority_queue)
            if current in visited:
                continue

            visited.add(current)
            path = path + [current]
            print("Visiting:", current)

            if current == target:
                print("Found target:", target, "with cost:", cost, "at path:", path)
                return

            for (neighbor, weight) in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + weight, neighbor, path))

        print("Target", target, "not found in the graph.")

    def ucs_wrapper(self, graph, start, target):
        """
        Starts Uniform Cost Search on the given graph
        :param graph:
        :param start:
        :param target:
        :return:
        """
        print("Uniform Cost Search:")
        self.uniform_cost_search(graph, start, target)
