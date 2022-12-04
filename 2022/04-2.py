overlaps = 0

with open('04.txt') as fp:
    for pair in fp:
        section_ranges = [n.split("-") for n in pair.strip().split(",")]
        first_range = {n for n in range(int(section_ranges[0][0]), int(section_ranges[0][1])+1)}
        second_range = {n for n in range(int(section_ranges[1][0]), int(section_ranges[1][1])+1)}

        if set.intersection(first_range, second_range):
            overlaps += 1

print(overlaps)
