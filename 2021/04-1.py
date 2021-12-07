from pprint import pformat


class Board:
    rows = []
    matches = []

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

    def get_index(self):
        return self.index

    def check_bingo(self):
        for r in range (0, 5):
            if all(self.matches[r]) or all([n[r] for n in self.matches]):
                print("Bingo")
                return True
        return False


def main():
    numbers = []
    boards = []

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
            board.add_number(number)
            if board.check_bingo():
                answer = board.get_sum() * number
                print(answer)
                exit(0)
        print(f"{number} ", end="")

if __name__ == "__main__":
    main()
