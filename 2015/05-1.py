nice = 0
wovels = ["a", "e", "i", "o", "u"]
forbidden = ["ab", "cd", "pq", "xy"]


def num_wovels(word):
    num = 0
    for w in wovels:
        num += word.count(w)
    return num


def num_forbidden(word):
    num = 0
    for f in forbidden:
        num += word.count(f)
    return num


def have_doubles(word):
    for pos in range(0, len(word)-1):
        pair = word[pos:pos+2]
        if pair[0] == pair[1]:
            return True
    return False


with open('05.txt') as fp:
    for line in fp:
        line = line.strip()

        if num_forbidden(line) == 0 and num_wovels(line) >= 3 and have_doubles(line):
            nice += 1
            print(line)

print(nice)
