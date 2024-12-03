with open("01.txt") as fp:
    left, right = zip(*(map(int, line.split()) for line in fp.readlines()))

print(sum([x * right.count(x) for x in left]))
