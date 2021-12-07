GENERATIONS = 256

fishes = {i: 0 for i in range(0, 9)}

with open("06.txt") as fp:
    initial = [int(n) for n in fp.read().strip().split(",")]

for value in initial:
    fishes[value] += 1

for generation in range(0, GENERATIONS):
    next_generation = {i: 0 for i in range(0, 9)}

    for age in range(0, 9):
        if age == 0:
            next_generation[8] += fishes[0]
            next_generation[6] += fishes[0]
        else:
            next_generation[age - 1] += fishes[age]

    fishes = next_generation

print(fishes)            
print(sum(fishes.values()))
