from itertools import islice

chars = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
priority = {c[1]: c[0] + 1 for c in enumerate(chars)}

prio_sum = 0

with open('03.txt') as fp:
    while True:
        group = [{c for c in l.strip()} for l in islice(fp, 3)]

        if not group:
            break

        common = set.intersection(*group)
        prio_sum += priority[common.pop()]

print(prio_sum)
