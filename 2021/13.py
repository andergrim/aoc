from parse import parse

coords = set()
instructions = []

with open('13.txt') as fp:
    for line in fp:
        if "," in line:
            x, y = parse("{:d},{:d}", line.strip())
            coords.add((x, y))
        elif "=" in line:
            instruction, num = parse("fold along {}={:d}", line.strip())
            instructions.append((instruction, num))

    fold = 0
    for axis, position in instructions:
        max_row = max([y for x, y in coords])
        max_col = max([x for x, y in coords])

        if axis == "y":
            upper = [c for c in coords if c[1] < position]
            lower = [(x, max_row - y) for x, y in coords if y > position]
            coords = set(upper + lower)
        else:
            left = [c for c in coords if c[0] < position]
            right = [(max_col - x, y) for x, y in coords if x > position]
            coords = set(left + right)

        fold += 1
        print(f"{len(coords)} dots visible after fold {fold}")


for l in range(0, max_row+1):
    for c in range(0, max_col+1):
        if (c, l) in coords:
           print("#", end="")
        else:
           print(".", end="")
    print("")

