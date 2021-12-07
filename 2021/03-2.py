def filter_nums(position, pool, most_common):
    if len(pool) == 1:
        return pool[0]

    filtered = [[b for b in pool if b[position] == "0"], [b for b in pool if b[position] == "1"]]

    if most_common:
        if len(filtered[1]) >= len(filtered[0]):
            return filter_nums(position + 1, filtered[1], most_common)

        return filter_nums(position + 1, filtered[0], most_common)

    if len(filtered[0]) <= len(filtered[1]):
        return filter_nums(position + 1, filtered[0], most_common)

    return filter_nums(position + 1, filtered[1], most_common)


nums = []

with open('03.txt', encoding="utf-8") as fp:
    for line in fp:
        nums.append(line.strip())

oxygen = int("0b" + filter_nums(0, nums, True), 2)
scraper = int("0b" + filter_nums(0, nums, False), 2)

print(oxygen * scraper)
