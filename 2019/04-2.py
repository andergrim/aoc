range_min = 168630
range_max = 718098

valid_combinations = []
i = range_min
while i <= range_max:
    has_pair = False
    is_incrementing = True
    digits = tuple(int(n) for n in str(i))
    for j, digit in enumerate(digits):
        if j > 0:
            if not digit >= digits[j - 1]:
                is_incrementing = False

        if j < len(digits) - 1:
            pair = int(f"{digit}{digits[j + 1]}")
            if (pair / 11) == digit:
                has_pair = True

        # Check for uneven number adjacent duplicates

    if has_pair and is_incrementing:
        valid_combinations.append(i)
    i += 1

print(len(valid_combinations))
