last = None
incs = 0

with open('01.txt') as fp:
    for line in fp:
        current = int(line)
        if last and current > last:
            incs += 1
        last = current

print(incs)
