changes = []
freqs = [0]
freq = 0
dupe = None

with open('01.txt') as fp:
    for line in fp:
        changes.append(int(line.strip()))

j = 0
while True:
    for i in range(0, len(changes)):
        j += 1
        freq += changes[i]
        if freq in freqs:
            dupe = freq
            break
        freqs.append(freq)

    if dupe is not None:
        break

print(dupe, j)
