num_correct = 0

with open('02.txt') as fp:
    for line in fp:
        policy, pw = line.strip().split(": ")
        nums, letter = policy.split(" ")
        l_min, l_max = nums.split("-")
        l_min = int(l_min)
        l_max = int(l_max)

        count = pw.count(letter)
        if (count >= l_min and count <= l_max):
            print(l_min, l_max, letter, pw)
            num_correct += 1

print(num_correct)
