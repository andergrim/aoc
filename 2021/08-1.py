unique_lengths = [2, 4, 3, 7]
matches = 0
with open("08.txt") as fp:
    for line in fp:
        signal_patterns, output_values = line.strip().split("|")
        output_values = output_values.strip().split(" ")
        filtered_lengths = [o for o in output_values if len(o) in unique_lengths]
        matches += len(filtered_lengths)

print(matches)
