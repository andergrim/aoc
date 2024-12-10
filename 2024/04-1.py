with open("04.txt") as fp:
    lines = [l.strip() for l in fp.readlines()]

key = "XMAS"
num_rows = len(lines)
num_cols = len(lines[0])

directions = [
    "north",
    "northeast",
    "northwest",
    "east",
    "west",
    "south",
    "southwest",
    "southeast",
]


def get_at(row, col):
    return lines[row][col]


def find_at(row, col):
    findings = []

    in_bound_left = (col + 1 - len(key)) >= 0
    in_bound_right = (col + len(key)) <= num_cols
    in_bound_top = (row + 1 - len(key)) >= 0
    in_bound_bottom = (row + len(key)) <= num_rows

    up = range(row, row - len(key), -1)
    down = range(row, row + len(key))
    left = range(col, col - len(key), -1)
    right = range(col, col + len(key))

    for dir in directions:
        if dir == "north" and in_bound_top:
            if key == "".join([lines[r][col] for r in up]):
                findings.append([row, col, dir])
        
        elif dir == "east" and in_bound_right:
            if key == "".join([lines[row][c] for c in right]):
                findings.append([row, col, dir])

        elif dir == "south" and in_bound_bottom:
            if key == "".join([lines[r][col] for r in down]):
                findings.append([row, col, dir])

        elif dir == "west" and in_bound_left:
            if key == "".join([lines[row][c] for c in left]):
                findings.append([row, col, dir])

        elif dir == "northeast" and in_bound_top and in_bound_right:
            if key == "".join([lines[r][c] for r, c in zip(up, right)]):
                findings.append([row, col, dir])

        elif dir == "northwest" and in_bound_top and in_bound_left:
            if key == "".join([lines[r][c] for r, c in zip(up, left)]):
                findings.append([row, col, dir])

        elif dir == "southwest" and in_bound_bottom and in_bound_left:
            if key == "".join([lines[r][c] for r, c in zip(down, left)]):
                findings.append([row, col, dir])

        elif dir == "southeast" and in_bound_bottom and in_bound_right:
            if key == "".join([lines[r][c] for r, c in zip(down, right)]):
                findings.append([row, col, dir])

    return len(findings)


def main():
    matches = 0
    for line in range(num_rows):
        for char in range(num_cols):
            if get_at(line, char) == key[0]:
                matches += find_at(line, char)

    print(matches)

if __name__ == "__main__":
    main()
