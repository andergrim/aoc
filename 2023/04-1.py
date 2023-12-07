import re


with open("04.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

pattern = re.compile(r"Card\s{1,3}(\d)+:([\s\d]+)\|([\s\d]+)")

cards_list = {}
score = 0

for line in lines:
    cards = pattern.findall(line)
    card_number, drawn, ours = cards[0]

    drawn = drawn.split()
    ours = ours.split()

    correct = [n in drawn for n in ours].count(True)

    if correct > 0:
        score += 2 ** (correct - 1)

print(score)

