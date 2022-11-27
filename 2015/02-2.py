total_length = 0

with open('02.txt') as fp:
    for line in fp:
        sides = [int(s) for s in line.split("x")]
        l, w, h = sides
        sides.sort()
        smallest = sides[0:2]
        length = (sides[0]*2) + (sides[1]*2) + (l*w*h)
        total_length += length

print(total_length)
