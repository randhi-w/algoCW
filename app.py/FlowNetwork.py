from collections import defaultdict
import random
from flow_utilities import generate_flow_network, delete_node_from_network,modify_link_from_network,generate_flow_randomly
import time
from flow_visualize import generate_graph, generate_flow_distribution

class Graph:
    """This class uses a 2D array in python to represent a directed graph which denotes a adjaceny matrix representation"""
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        self.COL = len(graph[0])

    """Returns true if there is a path from source 's' (source) to sink 't' (sink) in 
    residual graph and fills parent[] to store the path """

    def breadth_first_search(self, s, t, parent):

        visited = [False] * (self.ROW)      # Create array with indicex and mark them as unvisited

        queue = [] # standard queue for the BFS

        # Mark and enque the source: 's'
        queue.append(s)
        visited[s] = True

        while queue:            #standard BFS loop
            u = queue.pop(0)
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, value in enumerate(self.graph[u]):
                if visited[ind] == False and value > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        if visited[t] == True:           #If the sink is reached from source via BFS ->
            return True
        else:
            return False


    def FordFulkerson(self, source, sink):
        """return the maximum flow of given graph between the given nodes source and sink
           with the final residual graph.
        """

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)
        # This array stores the flow paths added
        flow_dist = [[0 for i in range(self.ROW)] for j in range(self.ROW)]
        # set initial flow to zero
        max_flow = 0

        # Augment the flow while there is path from source to sink
        while self.breadth_first_search(source, sink, parent):
            # Find minimum capacity in the path filled by BFS
            path_flow = float("Inf")
            s = sink
            path = []
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                path.append([s, parent[s]])
                s = parent[s]
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges to current graph
            # update flow graph to keep track of flow paths
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                flow_dist[u][v] -= path_flow
                self.graph[v][u] += path_flow
                flow_dist[v][u]+= path_flow
                v = parent[v]

        return max_flow,flow_dist








