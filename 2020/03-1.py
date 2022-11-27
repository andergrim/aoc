map_grid = []
path_grid = []
trees_hit = 0

x_step = 3
y_step = 1

with open('03.txt') as fp:
    for line in fp:
        row = [n == "#" for n in line.strip()]
        map_grid.append(row)

for i in range(0, len(map_grid)):
    path_grid.append([False for n in range(0, len(map_grid[0]))])


x = 0
y = 0
for i in range(0, len(map_grid)):
    path_grid[y][x] = True

    y += y_step
    x += x_step
    x %= len(map_grid[0])

# Compare each position in the grids
for i in range(0, len(map_grid)):
    for j in range(0, len(map_grid[0])):

        if map_grid[i][j]:
            position = "#"
        else:
            position = "."

        if map_grid[i][j] & path_grid[i][j]:
            trees_hit += 1
            position = "O"
        elif path_grid[i][j]:
            position = "X"

        print(position, end="")
    print("")

print(trees_hit)
