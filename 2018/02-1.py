pairs = 0
triples = 0

with open("02-1.txt", "r") as f:
    boxes = f.readlines() 

for box in boxes:
    unique_letters = set(x for x in box)
    groups = [box.count(c) for c in unique_letters if box.count(c) in [2, 3]]

    if 2 in groups:
        pairs += 1
    if 3 in groups:
        triples += 1

print(f"Checksum {pairs * triples}")
