"""
Main Runner of the Uninformed Search (Breath First Search and Depth First Search)
"""

from searching_algorithms.uninformed_searching.graph import Graph
from searching_algorithms.uninformed_searching.depth_first_search import DepthFirstSearch
from searching_algorithms.uninformed_searching.breath_first_search import BreathFirstSearch

if __name__ == "__main__":

    # Creating instance of classes
    g = Graph()
    dfs = DepthFirstSearch()
    bfs = BreathFirstSearch()

    # Adding nodes in the graph
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('G', 'I')

    # Perform DFS
    dfs.dfs_wrapper(g.graph, 'A', 'I')
    print("")

    # Perform BFS
    bfs.bfs_wrapper(g.graph, 'A', 'I')
