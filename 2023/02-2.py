with open("02.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]	


rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

solution = 0

for line in lines:
    game, game_draws = line.split(": ")
    game_number = int(game.split(" ")[1])

    cubes_in_game = {"red": set(), "green": set(), "blue": set()}

    draws = game_draws.split("; ")
    for draw in draws:
        dices = draw.split(", ")
        for dice in dices:
            num, col = dice.split(" ")
            cubes_in_game[col].add(int(num))

    max_dice = [max(cubes_in_game[col]) for col in rules.keys()]
    solution += max_dice[0] * max_dice[1] * max_dice[2]

print(solution)
