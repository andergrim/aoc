from functools import reduce

map_grid = []
total_trees = []

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]  # x, y

with open("03.txt") as fp:
    for line in fp:
        row = [n == "#" for n in line.strip()]
        map_grid.append(row)

for slope in slopes:
    trees_hit = 0
    path_grid = []

    x_step, y_step = slope

    for i in range(0, len(map_grid)):
        path_grid.append([False for n in range(0, len(map_grid[0]))])

    x = 0
    y = 0
    for i in range(0, len(map_grid)):
        if y > len(map_grid):
            break

        path_grid[y][x] = True

        y += y_step
        x += x_step
        x %= len(map_grid[0])

    # Compare each position in the grids
    for i in range(0, len(map_grid)):
        for j in range(0, len(map_grid[0])):
            if map_grid[i][j] & path_grid[i][j]:
                trees_hit += 1

    print(slope, trees_hit)
    total_trees.append(trees_hit)

print(total_trees)
total = reduce((lambda x, y: x * y), total_trees)
print(f"Sum: {total}")
