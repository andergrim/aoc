import re
from collections import Counter

id_claims = {}

with open("03-1.txt", "r") as f:
    claims_raw = f.readlines() 

# Parse numbers
for claim in claims_raw:
    claim_id, dist_x, dist_y, width, height = (
        int(i) for i in re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", claim).groups()
    )
    
    id_claims[claim_id] = set()
    # Add a (x, y) tuple for each occupied square inch
    for y in range(dist_y + 1, dist_y + height + 1):
        for x in range(dist_x + 1, dist_x + width + 1):
            id_claims[claim_id].add((x, y))

for claim_id, claims in id_claims.items():
    matches = len([i for i, c in id_claims.items() if i != claim_id and len(claims.intersection(c)) > 0])
    if matches == 0:
        print(claim_id)
        exit(0)
