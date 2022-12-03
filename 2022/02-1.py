scoring = {
    "A": 1,
    "X": 1,
    "B": 2,
    "Y": 2,
    "C": 3,
    "Z": 3,
}

score = 0

with open('02.txt') as fp:
    for line in fp:
        opponent, me = line.strip().split(" ")
        score_o = scoring[opponent]
        score_m = scoring[me]

        score += score_m

        if score_m - score_o == 0:
            score += 3
        elif score_m - score_o in [1, -2]:
            score += 6

print(score)
