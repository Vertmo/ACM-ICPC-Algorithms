"""
d[t,k] is the distance from src to t using k edges or less. 
The graph is represented by an edge list
"""

from collections import defaultdict

class Graph:

    def initial(self, vertices):
        self.V = vertices
        self.graph = []

    def add(self, u, v, w):
        self.graph.append([u, v, w])

    def printsol(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print "Graph contains negative weight cycle"
                return

        self.printArr(dist)
