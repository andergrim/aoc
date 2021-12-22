import numpy as np
import numpy.matlib
from queue import PriorityQueue


base_matrix = []
matrix = []

start = (0, 0)
goal = (499, 499)

tiles = (5, 5)

def increment(value, r, c):
    if c == 0:
        # First in row
        value += r
    else:
        value += c + r 

    if value > 9:
        return value % 9

    return value


with open('15.txt') as fp:
    for line in fp:
        positions = [int(n) for n in line.strip()]
        base_matrix.append(positions)

width = len(base_matrix[0])
height = len(base_matrix)

matrix = numpy.matlib.repmat(base_matrix, tiles[0], tiles[1])

width_matrix = len(matrix[0])
height_matrix = len(matrix)

"""
Pick subsections of matrix, run through vectorized function and put back
into matrix 
"""
for row in range(0, tiles[0]):
    for col in range(0, tiles[1]):
        v_increment = np.vectorize(increment)
        sub_matrix = matrix[col * width:col * width + width, row * height:row * height + height]
        sub_matrix = v_increment(sub_matrix, row, col)
        matrix[col * width:col * width + width, row * height:row * height + height] = sub_matrix

visited = set()  # All visited vertices
path = {}  # (vertex: shortest path to this vertex so far)
queue = PriorityQueue()  # (cost, vertex)
queue.put((0, start))

"""
Apply Dijkstras algorithm from start postition until we've reached goal
"""
while not queue.empty():
    cost, vertex = queue.get()
    if vertex == goal:
        print(cost)
        exit(0)

    neighbours = [
        (vertex[0], vertex[1] + 1), (vertex[0] + 1, vertex[1]),
        (vertex[0], vertex[1] - 1), (vertex[0] - 1, vertex[1])
    ]
    
    for neighbour in neighbours:
        vx, vy = neighbour
        if vx < 0 or vx >= width_matrix or vy < 0 or vy >= width_matrix or neighbour in visited:
            continue  # None-existing vertex or already visited

        try_cost = cost + matrix[vx][vy]
        lowest = path.get(neighbour)

        if lowest and try_cost >= lowest:
            continue  # Cheaper path exists

        path[neighbour] = try_cost
        queue.put((try_cost, neighbour))

    visited.add(vertex)
