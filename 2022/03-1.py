chars = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
priority = {c[1]: c[0] + 1 for c in enumerate(chars)}

prio_sum = 0

with open('03.txt') as fp:
    for rucksack in fp:
        half = len(rucksack) // 2
        first = {c for c in rucksack[0:half]}
        second = {c for c in rucksack[half:]}

        common = first.intersection(second)
        prio_sum += priority[common.pop()]

print(prio_sum)
