import re

with open("03.txt") as fp:
    mem = "".join([l.strip() for l in fp.readlines()])

print(sum([int(g[0]) * int(g[1]) for g in re.findall(r'mul\((\d+),(\d+)\)', mem)]))
