with open('06-test.txt') as fp:
    data = fp.read().strip().split("\n\n")

groups = [g.split("\n") for g in data]
respondents = [len(g) for g in groups]

# for a, b in zip(groups, respondents):
answers = []
for group in groups:
    group_persons = []

    for person in group:

        person_answers = [a for a in person]
        print(person_answers)

    group_persons.append(person_answers)


print(group_persons)

