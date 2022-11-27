import re
from collections import Counter

claims = []

with open("03-1.txt", "r") as f:
    claims_raw = f.readlines() 

# Parse numbers
for claim in claims_raw:
    claim_id, dist_x, dist_y, width, height = (
        int(i) for i in re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", claim).groups()
    )
    
    # Add a (x, y) tuple for each occupied square inch
    for y in range(dist_y + 1, dist_y + height + 1):
        for x in range(dist_x + 1, dist_x + width + 1):
            claims.append((x, y))

stats = Counter(claims)
print(len([s for s in stats.values() if s > 1]))
