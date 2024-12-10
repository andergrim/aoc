with open("04.txt") as fp:
    lines = [l.strip() for l in fp.readlines()]

key = "MAS"
offset = int(len(key) / 2)
middle = key[offset:offset + 1]

num_rows = len(lines)
num_cols = len(lines[0])

directions = [
    "northeast",
    "northwest",
    "southwest",
    "southeast",
]


def get_at(row, col):
    return lines[row][col]


def find_at(row, col):
    findings = 0

    up = row - offset
    down = row + offset
    left = col - offset
    right = col + offset

    in_bound_left = left >= 0
    in_bound_right = right + 1 <= num_cols
    in_bound_top = up >= 0
    in_bound_bottom = down + 1 <= num_rows

    letter = {}

    for dir in directions:
        print(f"\n{row}, {col}, {dir}")


        if dir == "northeast" and in_bound_top and in_bound_right:
            letter[dir] = lines[up][right]
        elif dir == "northwest" and in_bound_top and in_bound_left:
            letter[dir] = lines[up][left]
        elif dir == "southwest" and in_bound_bottom and in_bound_left:
            letter[dir] = lines[down][left]
        elif dir == "southeast" and in_bound_bottom and in_bound_right:
            letter[dir] = lines[down][right]

    words = (
        letter.get('northeast', '') + middle + letter.get('southwest', ''),
        letter.get('northwest', '') + middle + letter.get('southeast', '')
    )

    if all([w == key or w == key[::-1] for w in words]):
        findings += 1

    return findings


def main():
    matches = 0
    for line in range(num_rows):
        for char in range(num_cols):
            if get_at(line, char) == middle:
                matches += find_at(line, char)

    print(matches)

if __name__ == "__main__":
    main()
