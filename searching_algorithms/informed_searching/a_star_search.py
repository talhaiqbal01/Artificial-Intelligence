"""
A* Search Class
"""
import heapq


class AStarSearch:
    @staticmethod
    def a_star_search(graph, start, target, heuristics):
        """
        Applies A* Search on the given graph, starting node and target node
        :param graph:
        :param start:
        :param target:
        :param heuristics:
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
                    total_cost = cost + weight
                    heuristic_cost = total_cost + heuristics.get(neighbor, float('inf'))
                    heapq.heappush(priority_queue, (heuristic_cost, neighbor, path))

        print("Target", target, "not found in the graph.")

    def astar_wrapper(self, graph, start, target, heuristics):
        """
        Starts A* Search on the given graph
        :param graph:
        :param start:
        :param target:
        :param heuristics:
        :return:
        """
        print("A* Search:")
        self.a_star_search(graph, start, target, heuristics)
