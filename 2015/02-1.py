total_area = 0

with open('02.txt') as fp:
    for line in fp:
        sides = [int(s) for s in line.split("x")]
        l, w, h = sides
        sides.sort()
        smallest = sides[0:2]
        area = (2*l*w)+(2*w*h)+(2*h*l)+(smallest[0]*smallest[1])
        total_area += area

print(total_area)
