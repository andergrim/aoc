x = {}
y = {}
x["santa"] = 0
y["santa"] = 0
x["robosanta"] = 0
y["robosanta"] = 0

houses = {(0, 0): 2}
direction = {}

with open('03.txt') as fp:
    while True:
        chars = fp.read(2)
        print(chars)

        if not chars or len(chars) < 2:
            break

        direction["santa"] = chars[0]
        direction["robosanta"] = chars[1]

        for figure in ["santa", "robosanta"]:
            if direction[figure] == "^":
                y[figure] += 1
            elif direction[figure] == "v":
                y[figure] -= 1
            elif direction[figure] == ">":
                x[figure] += 1
            elif direction[figure] == "<":
                x[figure] -= 1

            coords = (x[figure], y[figure])
            if coords in houses.keys():
                houses[coords] += 1
            else:
                houses[coords] = 1

print(len(houses))
