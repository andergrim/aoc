import re

stack_data = []
stack_numbers = []
moves = []

""" Parse input data """
with open('05.txt') as fp:
    for line in fp:
        if "[" in line:
            stack_data.append(line)
        elif line.strip() == "":
            pattern = re.compile("move (\d+?) from (\d+?) to (\d+?)\\n")
            for line in fp:
                moves.append([int(m) for m in re.findall(pattern, line)[0]])
        elif line[1].isnumeric:
            stack_numbers = [m for m in re.finditer("\d", line)]

""" Build stacks """
stacks = {}
for stack in stack_numbers:
    stack_index = int(stack.group())
    stack_pos = stack.span()[0]

    stacks[stack_index] = []

    for stack_row in stack_data:
        crate = stack_row[stack_pos]
        if crate != " ":
            stacks[stack_index].append(crate)

    stacks[stack_index].reverse()

""" Perform moves """
for move in moves:
    num, origin, target = move
    
    for i in range(0, num):
        crate = stacks[origin].pop()
        stacks[target].append(crate)

""" Get top crates from each stack """
top_crates = [s[-1] for s in stacks.values()]
print("".join(top_crates))

