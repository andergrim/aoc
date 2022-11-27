floor = 0
pos = 0
with open('01.txt') as fp:
    while True:
        char = fp.read(1)
        if not char:
            break
        pos += 1
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            break
print(pos)
