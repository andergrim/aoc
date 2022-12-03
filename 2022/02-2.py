scoring = {
    "A": 1,
    "B": 2,
    "C": 3,
}

score = 0

with open('02.txt') as fp:
    for line in fp:
        opponent, strategy = line.strip().split(" ")

        if strategy == "X":
            score_m = scoring[opponent] - 1
            if score_m < 1:
                score_m = 3

        elif strategy == "Y":
            score += 3
            score_m = scoring[opponent]
        else:
            score += 6
            score_m = scoring[opponent] + 1
            if score_m > 3:
                score_m = 1

        score += score_m


print(score)
