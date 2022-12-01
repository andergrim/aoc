elves = []

with open('01.txt') as fp:
    stash = []
    for line in fp:
        if line.strip().isnumeric():
            stash.append(int(line.strip()))
        else:
            elves.append(sum(stash))
            stash = []

print(sum(sorted(elves, reverse=True)[0:3]))
