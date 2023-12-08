import regex as re

with open("01.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numbers_lookup = {}
numbers_lookup.update(numbers.items())
numbers_lookup.update({str(n): n for n in numbers.values()})

digits = []
pattern = f"\\d|{'|'.join(numbers.keys())}"

for line in lines:
    match = re.findall(pattern, line, overlapped=True)
    digits.append(int(f"{numbers_lookup[match[0]]}{numbers_lookup[match[-1]]}"))

print(sum(digits))
