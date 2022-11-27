range_min = 168630
range_max = 718098

valid_combinations = []
i = range_min
while i <= range_max:
    has_pair = False
    is_incrementing = True
    has_uneven_adjacent = False
    digits = tuple(int(n) for n in str(i))
    for pos in range(len(digits)):
        if pos > 0:
            if not digits[pos] >= digits[pos - 1]:
                is_incrementing = False

        if pos < len(digits) - 1:
            pair = int(f"{digits[pos]}{digits[pos + 1]}")
            if (pair / 11) == digits[pos]:
                has_pair = True

    if has_pair and is_incrementing:
        valid_combinations.append(i)
    i += 1

print(len(valid_combinations))
