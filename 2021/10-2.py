subsystem = []
with open("10.txt") as fp:
    for line in fp:
        subsystem.append(line.strip())

tags = [
    ("(", ")", 1),
    ("[", "]", 2),
    ("{", "}", 3),
    ("<", ">", 4),
]


scores = []
l = 0
for line in subsystem:
    stack = []
    c = 0
    for char in line:
        if char in [c[0] for c in tags]:
            stack.append(char)
        else:
            tag = [t for t in tags if t[1] == char][0]
            opening = stack.pop()
            if opening != tag[0]:
                break
        c += 1
    if c == len(line):
        score = 0
        for i in range(len(stack), 0, -1):
            char = stack[i-1]
            tag = [t for t in tags if t[0] == char][0]
            score *= 5
            score += tag[2]
        scores.append(score)

    l += 1

middle = sorted(scores)[len(scores) // 2]
print(middle)
