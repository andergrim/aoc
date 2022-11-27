with open('06.txt') as fp:
    data = fp.read().split("\n\n")

groups = [g.split("\n") for g in data]

answers = 0
for group in groups:
    answers += len(set([q for q in "".join(group)]))

print(answers)
