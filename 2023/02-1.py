with open("02.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]	


rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

solution = 0

for line in lines:
    game_ok = True

    game, game_draws = line.split(": ")
    game_number = int(game.split(" ")[1])

    draws = game_draws.split("; ")
    for draw in draws:
        dice = draw.split(", ")
        dice_dict = {d.split(" ")[1]: int(d.split()[0]) for d in dice}

        if any([num > rules[col] for col, num in dice_dict.items()]):
            print(game_number, dice_dict, [num > rules[col] for col, num in dice_dict.items()])
            game_ok = False


    if game_ok:
        solution += game_number

print(solution)
