from collections import Counter


class Hand():
    FACE_VALUES = {
        "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8,
        "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
    }

    HAND_VALUES = [
        "pair", "two_pairs", "three_of_a_kind", "full_house",
        "four_of_a_kind", "five_of_a_kind"
    ]

    cards = []
    bet = 0

    def __init__(self, cards: list, bet: int) -> None:
        self.cards = cards
        self.bet = bet

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

    def __lt__(self, other) -> bool:
        this_hand = self.get_hand_value()
        other_hand = other.get_hand_value()

        if other_hand > this_hand:
            return True
        elif this_hand > other_hand:
            return False
        
        for vals in zip(self.get_card_values(), other.get_card_values()):
            this_val, other_val = vals
            if other_val > this_val:
                return True
            elif this_val > other_val:
                return False

        return False

    def __eq__(self, _) -> bool:
        return False

    def __ne__(self, _) -> bool:
        return True

    def __repr__(self):
        return(repr(self.cards))


with open("07.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

hands = []

for line in lines:
    cards, bet = line.split(" ")
    hands.append(Hand([c for c in cards], int(bet)))

hands.sort()
total_score = sum([(multiple + 1) * hand.bet for multiple, hand in enumerate(hands)])
print(total_score)
