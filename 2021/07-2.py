with open("07.txt") as fp:
    crabs = [int(n) for n in fp.read().strip().split(",")]

cost_per_crab = []
for start_position in range(0, max(crabs)+1):
    costs_for_crab = []
    for to_position in crabs:
        distance = abs(start_position - to_position)
        cost = sum([i for i in range(0, distance+1)])
        costs_for_crab.append(cost)
    cost_per_crab.append(costs_for_crab)

lowest = [sum(c) for c in cost_per_crab]
print(min(lowest))
