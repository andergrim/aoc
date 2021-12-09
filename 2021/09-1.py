
matrix = []
with open("09.txt") as fp:
    for line in fp:
        matrix.append([int(n) for n in line.strip()])

width = len(matrix[0])
height = len(matrix)

def get_neighbours(r, c):
    neighbours = []
    if r > 0:
        neighbours.append(matrix[r-1][c])
    if r < height-1:
        neighbours.append(matrix[r+1][c])
    if c > 0:
        neighbours.append(matrix[r][c-1])
    if c < width-1:
        neighbours.append(matrix[r][c+1])
    return neighbours


risk_level = 0

r = 0
for row in matrix:
    c = 0
    for col in row:
        if all([col < n for n in get_neighbours(r, c)]):
            risk_level += col + 1

        c += 1
    r += 1

print(risk_level)
