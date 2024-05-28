from searching_algorithms.informed_searching.graph import Graph
from searching_algorithms.informed_searching.uniform_cost_search import UniformCostSearch
from searching_algorithms.informed_searching.a_star_search import AStarSearch
from searching_algorithms.informed_searching.greedy_best_first_search import GreedyBestFirstSearch
from searching_algorithms.informed_searching.dijkstra_search import DijkstraSearch

if __name__ == "__main__":
    # Create graph and add edges with weights
    g = Graph()
    ucs = UniformCostSearch()
    astar = AStarSearch()
    greedy = GreedyBestFirstSearch()
    dijkstra = DijkstraSearch()

    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 2)
    g.add_edge('B', 'E', 5)
    g.add_edge('C', 'F', 6)
    g.add_edge('C', 'G', 3)
    g.add_edge('D', 'H', 1)
    g.add_edge('G', 'I', 2)

    # Set heuristic values for nodes
    g.set_heuristic('A', 7)
    g.set_heuristic('B', 6)
    g.set_heuristic('C', 2)
    g.set_heuristic('D', 5)
    g.set_heuristic('E', 3)
    g.set_heuristic('F', 1)
    g.set_heuristic('G', 0)
    g.set_heuristic('H', 8)
    g.set_heuristic('I', 4)

    # Perform UCS
    ucs.ucs_wrapper(g.graph, 'A', 'I')
    print("")

    # Perform A* Search
    astar.astar_wrapper(g.graph, 'A', 'I', g.heuristics)
    print("")

    # Perform Greedy Best-First Search
    greedy.greedy_wrapper(g.graph, 'A', 'I', g.heuristics)
    print("")

    # Perform Dijkstra's Algorithm
    dijkstra.dijkstra_wrapper(g.graph, 'A', 'I')
