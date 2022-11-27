num_correct = 0

with open('02.txt') as fp:
    for line in fp:
        policy, pw = line.strip().split(": ")
        nums, letter = policy.split(" ")
        num_1, num_2 = nums.split("-")
        num_1 = int(num_1) - 1
        num_2 = int(num_2) - 1

        if (bool(pw[num_1] == letter) ^ bool(pw[num_2] == letter)):
            print(num_1, num_2, letter, pw)
            num_correct += 1

print(num_correct)
