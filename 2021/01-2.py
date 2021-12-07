vals = []
with open('01.txt') as fp:
    for line in fp:
        vals.append(int(line))

incs = 0
last = False
for i in range(0, len(vals) - 2):
    group = []
    for j in range(0, 3):
        group.append(vals[i+j])
    current = sum(group)
    if last and current > last:
        incs += 1
    last = current

print(incs)
