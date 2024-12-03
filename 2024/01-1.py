with open("01.txt") as fp:
    left, right = zip(*(map(int, line.split()) for line in fp.readlines()))

left = sorted(left)
right = sorted(right)

print(sum([abs(x - y) for x, y in zip(left, right)]))
