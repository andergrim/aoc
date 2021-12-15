# Test 10
# caves = [
#     "start-A",
#     "start-b",
#     "A-c",
#     "A-b",
#     "b-d",
#     "A-end",
#     "b-end",
# ]

# Test 19
# caves = [
#     "dc-end",
#     "HN-start",
#     "start-kj",
#     "dc-start",
#     "dc-HN",
#     "LN-dc",
#     "HN-end",
#     "kj-sa",
#     "kj-HN",
#     "kj-dc",
# ]

# Test 226
# caves = [
#     "fs-end",
#     "he-DX",
#     "fs-he",
#     "start-DX",
#     "pj-DX",
#     "end-zg",
#     "zg-sl",
#     "zg-pj",
#     "pj-he",
#     "RW-he",
#     "fs-DX",
#     "pj-RW",
#     "zg-RW",
#     "start-pj",
#     "he-WI",
#     "zg-he",
#     "pj-fs",
#     "start-RW",
# ]

# Puzzle input
caves = [
    "RT-start",
    "bp-sq",
    "em-bp",
    "end-em",
    "to-MW",
    "to-VK",
    "RT-bp",
    "start-MW",
    "to-hr",
    "sq-AR",
    "RT-hr",
    "bp-to",
    "hr-VK",
    "st-VK",
    "sq-end",
    "MW-sq",
    "to-RT",
    "em-er",
    "bp-hr",
    "MW-em",
    "st-bp",
    "to-start",
    "em-st",
    "st-end",
    "VK-sq",
    "hr-st",
]

connections = []
for cave in caves:
    connections.append(cave.split("-"))

def navigate(start, visited):
    print(start, end=", ")
    if start in visited:
        return 0

    if start == "end":
        print("")
        return 1

    if start.islower():
        visited.add(start)

    num_paths = 0

    neighbours = [s for s, t in connections if t == start]
    neighbours += [t for s, t in connections if s == start]

    for neighbour in neighbours:
        num_paths += navigate(neighbour, visited)

    visited.discard(start)

    return num_paths

print("\n", navigate("start", set()))
