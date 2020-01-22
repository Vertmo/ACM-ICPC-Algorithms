"""
Floyd-Warshall algorithm : computes the minimum cost between every
pair of vertices in the graph, according to the costs of edges
"""

import numpy as np
import random, math

def floyd_warshall(cost, A, n):
	for i in range(n):
		for j in range(n):
			A[i][j] = cost[i][j]

	for k in range(n):
		for i in range(n):
			for j in range(n):
				A[i][j] = min(A[i][k] + A[k][j], A[i][j])

	return np.matrix(A)
