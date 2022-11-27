freq = 0

with open('01.txt') as fp:
    for line in fp:
        freq += int(line.strip())
print(freq)
