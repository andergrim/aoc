import argparse

parser = argparse.ArgumentParser(prog = "AoC Day 6")
parser.add_argument("-c", "--count", type=int, required=True,
                    help="Number of unique entries to look up")

args = parser.parse_args()

queue = []

with open('06.txt') as fp:
    data = fp.read()

for i in range(0, len(data)):
    if len(queue) == args.count and len(queue) == len(set(queue)):
        print(i)
        exit()

    queue.append(data[i])
    if len(queue) > args.count:
        queue.pop(0)
