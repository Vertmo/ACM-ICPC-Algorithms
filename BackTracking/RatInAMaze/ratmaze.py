"""
Solving the Maze problem using backtracking
maze = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]],
where 1s are the safe cells
"""

# Maze size
N = 4

def isSafe(maze, x, y):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

def solveMaze(maze):
    sol = [[0 for j in range(4)] for i in range(4)]

    if solveMazeUtil(maze, 0, 0, sol) is False:
        print("Solution doesn't exist")
        return False

    printSolution(sol)
    return True


def solveMazeUtil(maze, x, y, sol):
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y) is True:
        sol[x][y] = 1

        if solveMazeUtil(maze, x + 1, y, sol) is True:
            return True

        if solveMazeUtil(maze, x, y + 1, sol) is True:
            return True

        sol[x][y] = 0
        return False
