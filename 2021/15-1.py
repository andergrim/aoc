matrix = []
costs = {}

start = (0, 0)
goal = (99, 99)

with open('15.txt') as fp:
    for line in fp:
        positions = [int(n) for n in line.strip()]
        matrix.append(positions)

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        costs[(i, j)] = float("inf")


costs[start] = 0


visited = set()
while goal not in visited:
    vertex, cost = sorted({k: v for k, v in costs.items() if k not in visited}.items(), key=lambda x: x[1])[0]
    visited.add(vertex)

    closest = [(vertex[0], vertex[1] + 1), (vertex[0] + 1, vertex[1])]
    neighbours = [c for c in closest if c in costs]  # Lazily filter out invalid neighbours by comparing to matrix

    for neighbour in neighbours:
        total_cost = cost + matrix[neighbour[0]][neighbour[1]]
        if total_cost < costs[neighbour]:
            costs[neighbour] = total_cost

print(costs[goal])
