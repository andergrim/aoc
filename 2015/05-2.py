nice = 0


def have_two_doubles(word):
    for pos in range(0, len(word)-1):
        pair = word[pos:pos+2]
        if word.count(pair) >= 2:
            return True
    return False


def have_pair_in_triplet(word):
    for pos in range(0, len(word)-2):
        triplet = word[pos:pos+3]
        if triplet[0] == triplet[2]:
            return True
    return False


with open('05.txt') as fp:
    for line in fp:
        line = line.strip()

        if have_two_doubles(line) and have_pair_in_triplet(line):
            nice += 1
            print(line)

print(nice)
