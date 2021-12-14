import py_cui


# Test
# matrix = [
#     [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
#     [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
#     [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
#     [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
#     [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
#     [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
#     [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
#     [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
#     [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
#     [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
# ]

# Actual
matrix = [
    [3, 2, 6, 5, 2, 5, 5, 2, 7, 6],
    [1, 5, 3, 7, 4, 1, 2, 6, 6, 5],
    [7, 3, 3, 5, 7, 4, 6, 4, 2, 2],
    [6, 4, 2, 6, 3, 2, 5, 6, 5, 8],
    [3, 8, 5, 4, 4, 3, 4, 3, 6, 4],
    [8, 7, 1, 7, 3, 7, 7, 4, 8, 6],
    [4, 5, 2, 2, 2, 8, 6, 3, 2, 6],
    [6, 3, 3, 7, 7, 7, 2, 8, 4, 5],
    [8, 8, 2, 4, 3, 8, 7, 6, 6, 5],
    [6, 3, 5, 1, 5, 8, 6, 4, 8, 4],
]

class Flasher:
    matrix = []
    flashes = 0
    flashing = set()
    step = 0

    def __init__(self, root, matrix):
        self.matrix = matrix
        self.root = root
        self.root.add_key_command(py_cui.keys.KEY_SPACE, self.advance)
        self.root.add_key_command(py_cui.keys.KEY_ENTER, self.run)

        self.button_step = self.root.add_button(title="Advance", row=10, column=0, column_span=5, command=self.advance)
        self.button_end = self.root.add_button(title="Run", row=10, column=5, column_span=5, command=self.run)

        self.redraw()

    def redraw(self):
        self.root.set_title(f"Flashing dumbo octopuses - STEP {self.step} - FLASHES {self.flashes}")

        r = 0
        for row in self.matrix:
            c = 0
            for col in row:
                if col == 0:
                    color = py_cui.BLUE_ON_BLACK
                elif col < 4:
                    color = py_cui.WHITE_ON_BLACK
                elif col == 9:
                    color = py_cui.GREEN_ON_BLACK
                elif col < 10:
                    color = py_cui.CYAN_ON_BLACK
                else:
                    color = py_cui.MAGENTA_ON_BLACK

                self.root.add_label(str(col), r, c).set_color(color)
                c += 1
            r += 1

    def advance(self):
        """ Increase all one step """
        self.flashing = set()
        for row in range(0, 10):
            for col in range(0, 10):
                self.increment(row, col)
        self.step += 1

        for row, col in self.flashing:
            self.matrix[row][col] = 0

        self.flashes += len(self.flashing)
        self.redraw()

    def increment(self, row, col):
        num = self.matrix[row][col]
        num += 1
        self.matrix[row][col] = num
        if num > 9 and (row, col) not in self.flashing:
            self.flashing.add((row, col))
            for n_row, n_col in self.get_neighbours(row, col):
                self.increment(n_row, n_col)

    def get_neighbours(self, row, col):
        neighbours = set()
        if col > 0:
            neighbours.add((row, col-1))
        if col < 9:
            neighbours.add((row, col+1))

        if row > 0:
            neighbours.add((row-1, col))
            if col > 0:
                neighbours.add((row-1, col-1))
            if col < 9:
                neighbours.add((row-1, col+1))

        if row < 9:
            neighbours.add((row+1, col))
            if col > 0:
                neighbours.add((row+1, col-1))
            if col < 9:
                neighbours.add((row+1, col+1))

        return neighbours.difference(self.flashing)



    def run(self):
        for i in range(0, 100-self.step):
            self.advance()


def main():
    root = py_cui.PyCUI(11, 10)
    root.set_status_bar_text("<q> to exit, <space> to advance step, <enter> to run to end")
    root.toggle_unicode_borders()
    flasher = Flasher(root, matrix)
    root.start()


if __name__ == "__main__":
    main()
