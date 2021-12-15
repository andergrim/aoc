from collections import defaultdict

# Test 36
# caves = [
#     "start-A",
#     "start-b",
#     "A-c",
#     "A-b",
#     "b-d",
#     "A-end",
#     "b-end",
# ]

# Test 103
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

# Test 3509
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

def navigate(start, visited, revisited=False):
    print(start, end=", ")
    if start == "end":
        print("")
        return 1

    if visited[start] > 0 and revisited:
        return 0

    if start.islower():
        visited[start] += 1
        revisited |= visited[start] == 2

    num_paths = 0

    neighbours = [s for s, t in connections if t == start and s != "start"]
    neighbours += [t for s, t in connections if s == start and t != "start"]

    for neighbour in neighbours:
        num_paths += navigate(neighbour, visited, revisited)

    visited[start] -= 1

    return num_paths

print("\n", navigate("start", defaultdict(int)))
