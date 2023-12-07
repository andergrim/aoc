class Hand():

    VALUES = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    cards = []
    bet = 0

    def __init__(self, cards: list, bet: int) -> None:
        self.cards = cards
        self.bet = bet
        print(self.cards, bet)




with open("07.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

hands = []

for line in lines:
    cards, bet = line.split(" ")
    hands.append(Hand([c for c in cards], int(bet)))

