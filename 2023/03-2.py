import re
from pprint import pprint


def is_part_number(lines: list, line_number: int, span) -> bool:
    start, end = span
    for num in range(line_number - 1, line_number + 2):
        print(lines[num][start - 1:end + 1])
        if (match := re.findall(r"[^\.0-9]+", lines[num][start - 1:end + 1])):
            print(match)
            return True
    return False


grid_size = 140

lines = []
lines.append("." * (grid_size + 2))
with open("03.txt", "r") as fh:
    lines += ([f".{l.strip()}." for l in fh.readlines()])
lines.append("." * (grid_size + 2))

# print(lines)

part_numbers = []

for num, line in enumerate(lines):
    # print(num, line)
    numbers = [m for m in re.finditer(r"\d+", line)]
    print(num, line, numbers)

    for match in numbers:
        if is_part_number(lines, num, match.span()):
            part_numbers.append(int(match.group()))

    print("\n")

print(sum(part_numbers))
