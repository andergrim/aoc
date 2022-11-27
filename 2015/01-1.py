floor = 0
with open('01.txt') as fp:
    while True:
        char = fp.read(1)
        if not char:
            break
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
print(floor)
