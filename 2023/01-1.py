import re

with open("01.txt", "r") as fh:
    lines = [l.strip() for l in fh.readlines()]

digits = []
for line in lines:
    match = re.findall(r"\d", line)
    digits.append(int(f"{match[0]}{match[-1]}"))

print(sum(digits))
