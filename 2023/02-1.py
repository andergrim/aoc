with open("02-test.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

limits = {"red": 12, "green": 13, "blue": 14}
solution = 0
games = {}

for line in lines:
    game, rounds = line.split(": ")
    game_number = int(game.split(" ")[1])

    game_rounds = {"red": 0, "green": 0, "blue": 0}
    for game_round in rounds.split("; "):
        for draw in game_round.split(", "):
            num, col = draw.split(" ")
            game_rounds[col] += int(num)

    if all([num <= limits[col] for col, num in game_rounds.items()]):
        solution += game_number

    games[int(game_number)] = game_rounds

print(solution)    
print(games)
