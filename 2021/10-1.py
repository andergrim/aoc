subsystem = []
with open("10.txt") as fp:
    for line in fp:
        subsystem.append(line.strip())

tags = [
    ("(", ")", 3),
    ("[", "]", 57),
    ("{", "}", 1197),
    ("<", ">", 25137),
]

error_score = 0
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
                print(f"Found {char}, expected {[t[1] for t in tags if t[0] == opening][0]} at position {l}:{c}")
                error_score += tag[2]
                break
        c += 1
    l += 1

print(error_score)
