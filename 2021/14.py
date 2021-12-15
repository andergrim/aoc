from parse import parse
from collections import defaultdict


rules = []
with open('14.txt') as fp:
    for line in fp:
        if "->" in line:
            pair, insert = parse("{} -> {}", line.strip())
            rules.append((pair, insert))
        elif line != "\n":
            polymer_template = line.strip()

pairs = defaultdict(int)
occurences = defaultdict(int)

for c in range(0, len(polymer_template) - 1):
    pairs[polymer_template[c:c+2]] += 1

for c in polymer_template:
    occurences[c] += 1

for i in range(0, 40):
    pairs_adjust = defaultdict(int)
    
    """ Apply rules """
    for pair, insert in rules:
        num_cur_pair = pairs[pair]
        if num_cur_pair > 0:
            occurences[insert] += num_cur_pair
            pairs_adjust[pair] -= num_cur_pair
            pairs_adjust[pair[0] + insert] += num_cur_pair
            pairs_adjust[insert + pair[1]] += num_cur_pair

    for adj_pair, adj in pairs_adjust.items():
        pairs[adj_pair] += adj

most_common = max([v for v in occurences.values()])
least_common = min([v for v in occurences.values()])
print(occurences)
print(most_common - least_common)
