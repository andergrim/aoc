x = 0
y = 0
houses = {(x, y): 1}
with open('03.txt') as fp:
    while True:
        char = fp.read(1)
        if not char:
            break
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1

        coords = (x, y)
        if coords in houses.keys():
            houses[coords] += 1
        else:
            houses[coords] = 1

print(len(houses))
