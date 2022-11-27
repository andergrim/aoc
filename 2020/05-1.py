seats = []
seat = 0

for i in range(0, 128):
    row = []
    for j in range(0, 8):
        row.append(seat)
        seat += 1
    seats.append(row)

reservations = []
with open('05.txt') as fp:
    for line in fp:
        row = line[0:7]
        col = line.strip()[7:]
        reservations.append((row, col))

selections = []
for rows, cols in reservations:
    selected = seats
    for row in rows:
        split = len(selected) // 2
        if row == "F":
            selected = selected[0:split]
        else:
            selected = selected[split:]
    
    selected = selected[0]
    for col in cols:
        split = len(selected) // 2
        if col == "L":
            selected = selected[0:split]
        else:
            selected = selected[split:]

    selections.append(selected[0])

print(max(selections))
