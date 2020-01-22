"""
Breadth-First search algorithm in a graph represented as an adjacency dict
"""

import collections

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    # While we still have nodes to visit
    while queue: 
        vertex = queue.popleft()
        # Add neighbours of current node to queue if they
        # haven't been visited yet and mark them as visited.
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 
