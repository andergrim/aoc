import math
from PIL import Image

matrix = []
with open("09.txt") as fp:
    for line in fp:
        matrix.append([int(n) for n in line.strip()])

width = len(matrix[0])
height = len(matrix)

in_basin = set()
basins = []


def get_basin(r, c, members=None):
    if not members:
        members = set()

    if matrix[r][c] < 9:
        members.add((r, c))
        in_basin.add((r, c))
    else:
        return members

    near = set()
    # Search north
    if r > 0 and (r-1, c) not in members:
         near = get_basin(r-1, c, members)

    # Search south
    if r < height-1 and (r+1, c) not in members:
         near = get_basin(r+1, c, members)

    # Search west
    if c > 0 and (r, c-1) not in members:
        near = get_basin(r, c-1, members)

    # Search east
    if c < width-1 and (r, c+1) not in members:
        near = get_basin(r, c+1, members)

    return set.union(members, near)


r = 0
for row in matrix:
    c = 0
    for col in row:
        if col < 9 and (r, c) not in in_basin:
            basin = get_basin(r, c)
            basins.append(basin)
        c += 1
    r += 1

img = Image.new("RGB", (width, height))
r = 0
for row in matrix:
    c = 0
    for col in row:
        if col == 9:
            img.putpixel((r, c), (0, 255, 0))
        else:
            img.putpixel((r, c), (0, 0, 255))
        c += 1
    r += 1
img.save("09-output.png")
