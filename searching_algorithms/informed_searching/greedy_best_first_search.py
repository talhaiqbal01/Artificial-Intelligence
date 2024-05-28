"""
Greed Best First Search Class
"""
import heapq


class GreedyBestFirstSearch:
    @staticmethod
    def greedy_best_first_search(graph, start, target, heuristics):
        """
        Applies Greedy Best-First Search on the given graph, starting node and target node
        :param graph:
        :param start:
        :param target:
        :param heuristics:
        :return:
        """
        priority_queue = [(heuristics.get(start, float('inf')), start, [])]
        visited = set()

        while priority_queue:
            (heuristic, current, path) = heapq.heappop(priority_queue)
            if current in visited:
                continue

            visited.add(current)
            path = path + [current]
            print("Visiting:", current)

            if current == target:
                print("Found target:", target, "at path:", path)
                return

            for (neighbor, weight) in graph.get(current, []):
                if neighbor not in visited:
                    heuristic_cost = heuristics.get(neighbor, float('inf'))
                    heapq.heappush(priority_queue, (heuristic_cost, neighbor, path))

        print("Target", target, "not found in the graph.")

    def greedy_wrapper(self, graph, start, target, heuristics):
        """
        Starts Greedy Best-First Search on the given graph
        :param graph:
        :param start:
        :param target:
        :param heuristics:
        :return:
        """
        print("Greedy Best-First Search:")
        self.greedy_best_first_search(graph, start, target, heuristics)
