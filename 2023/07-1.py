from collections import Counter
from pprint import pprint


class Hand():

    FACE_VALUES = {
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

    HAND_VALUES = [
        "pair",
        "two_pairs",
        "three_of_a_kind",
        "full_house",
        "four_of_a_kind",
        "five_of_a_kind"
    ]

    cards = []
    bet = 0

    def __init__(self, cards: list, bet: int) -> None:
        self.cards = cards
        self.bet = bet
        # print(self.cards, sorted(list(Counter(self.cards).values())), self.get_hand_value(), self.get_card_values(), bet)

    def get_hand_value(self) -> int:
        match sorted(list(Counter(self.cards).values())):
            case [5]:
                return self.HAND_VALUES.index("five_of_a_kind") + 1
            case [1, 4]:
                return self.HAND_VALUES.index("four_of_a_kind") + 1
            case [2, 3]:
                return self.HAND_VALUES.index("full_house") + 1
            case [1, 1, 3]:
                return self.HAND_VALUES.index("three_of_a_kind") + 1
            case [1, 2, 2]:
                return self.HAND_VALUES.index("two_pairs") + 1
            case [1, 1, 1, 2]:
                return self.HAND_VALUES.index("pair") + 1
        return 0

    def get_card_values(self) -> list:
        return [self.FACE_VALUES[c] for c in self.cards]

    def __lt__(self, other) -> int:
        this_hand = self.get_hand_value()
        other_hand = other.get_hand_value()

        if other_hand > this_hand:
            print(other, other_hand, "is larger than", self, this_hand)
            return 1
        elif this_hand > other_hand:
            print(self, this_hand, "is larger than", other, other_hand)
            return -1
        else:
            print(self, this_hand, "is the same as", other, other_hand, "check card values")

        
        for vals in zip(self.get_card_values(), other.get_card_values()):
            this_val, other_val = vals
            if other_val > this_val:
                print(other, other_val, "is larger than", self, this_val)
                return 1
            elif this_val > other_val:
                print(self, this_val, "is larger than", other, other_val)
                return -1
            else:
                print(self, this_val, "is the same as", other, other_val, "check next")

        return 0

    def __repr__(self):
        return(repr(self.cards))


with open("07-test.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

hands = []

for line in lines:
    cards, bet = line.split(" ")
    hands.append(Hand([c for c in cards], int(bet)))

"""
Should be
['Q', 'Q', 'Q', 'J', 'A']
['T', '5', '5', 'J', '5']
['K', 'K', '6', '7', '7']
['K', 'T', 'J', 'J', 'T']
['3', '2', 'T', '3', 'K']

['Q', 'Q', 'Q', 'J', 'A']
['K', 'T', 'J', 'J', 'T'] *
['K', 'K', '6', '7', '7']
['T', '5', '5', 'J', '5'] *
['3', '2', 'T', '3', 'K']

"""
hands.sort()
pprint(hands)

total_score = sum([multiple * (hand.bet + 1) for multiple, hand in enumerate(hands)])
print(total_score)
