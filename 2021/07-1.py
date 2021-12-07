from statistics import median

with open("07.txt") as fp:
    crabs = [int(n) for n in fp.read().strip().split(",")]

fuel_cost = 0
position = median(crabs)

for crab in crabs:
    distance = position - crab
    fuel_cost += abs(distance)

print(int(fuel_cost))
