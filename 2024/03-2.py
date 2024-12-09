import re

with open("03.txt") as fp:
    mem = "".join([l.strip() for l in fp.readlines()])

# instructions = [m for m in re.findall(r'(mul)\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', mem)]
pattern = r'(?P<instruction>mul|don\'t|do)\(([\d,]*)\)'
instructions = [(op, param.split(',')) for op, param in re.findall(pattern, mem)]

sum = 0
enabled = True

for instruction, params in instructions:
    match instruction:
        case "don't":
            enabled = False
        case "do":
            enabled = True
        case "mul":
            if enabled:
                x, y = map(int, params)
                sum += x * y

print(sum)
