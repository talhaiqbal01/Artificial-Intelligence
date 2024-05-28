"""
Dijkstra Search Class
"""

import heapq


class DijkstraSearch:

    @staticmethod
    def dijkstra_search(graph, start, target):
        """
        Applies Dijkstra's algorithm on the given graph, starting node and target node
        :param graph: Dictionary representing the graph with edge weights
        :param start: Starting node
        :param target: Target node
        :return: Shortest path from start to target and its cost
        """
        priority_queue = []
        heapq.heappush(priority_queue, (0, start, [start]))
        visited = set()

        while priority_queue:
            (cost, current_node, path) = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == target:
                print("Found target:", target, "with cost:", cost, "and path:", path)
                return cost, path

            for (neighbor, weight) in graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))

        print("Target", target, "not found in the graph.")
        return float('inf'), []

    def dijkstra_wrapper(self, graph, start, target):
        """
        Starts Dijkstra's algorithm on the given graph
        :param graph: Dictionary representing the graph with edge weights
        :param start: Starting node
        :param target: Target node
        :return: Shortest path from start to target and its cost
        """
        print("Dijkstra Search:")
        return self.dijkstra_search(graph, start, target)
