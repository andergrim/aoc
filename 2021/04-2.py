from pprint import pformat


class Board:
    rows = []
    matches = []
    _bingo = False

    def __repr__(self):
        return f"{pformat(self.rows)}\n{pformat(self.matches)}\n"

    def __init__(self, rows):
        self.rows = rows
        self.matches = [[False, False, False, False, False] for i in range(0, 5)]

    def get_sum(self):
        nums = [n for l in self.rows for n in l]
        matches = [n for l in self.matches for n in l]
        unchecked = [num for num, used in zip(nums, matches) if not used]
        return sum(unchecked)

    def add_number(self, number):
        for row_index, row in enumerate(self.rows):
            if number in row:
                self.matches[row_index][row.index(number)] = True

        if self.check_bingo():
            self._bingo = True

    def get_index(self):
        return self.index

    def check_bingo(self):
        for r in range (0, 5):
            if all(self.matches[r]) or all([n[r] for n in self.matches]):
                print("Bingo")
                return True
        return False

    @property
    def bingo(self):
        return self._bingo



def main():
    numbers = []
    boards = []
    scores = []

    with open("04-numbers.txt", encoding="utf-8") as fp:
        for number in fp.read().strip().split(","):
            numbers.append(int(number))

    with open("04-boards.txt", encoding="utf-8") as fp:
        board = []
        for line in fp:
            if line.strip() == "":
                boards.append(Board(board))
                board = []
            else:
                line = line.strip().replace("  ", " ")
                board.append([int(n) for n in line.split(" ")])

    for number in numbers:
        for board in boards:
            if not board.bingo:
                board.add_number(number)
                if board.bingo:
                    scores.append(board.get_sum() * number)
        print(f"{number} ", end="")

    print(f"Final score {scores[-1]}")

if __name__ == "__main__":
    main()
