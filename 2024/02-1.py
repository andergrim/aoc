with open("02.txt") as fp:
    reports = [tuple(map(int, line.split())) for line in fp.readlines()]

safe_reports = 0

for report in reports:

    """ Find the difference between each pair """
    diffs = [report[offset] - report[offset + 1] for offset in range(len(report) - 1)]

    """ Make sure all diffs for level is either between -3 and -1 OR 1 and 3 """
    if all([n < 0 and n >= -3 for n in diffs]) or all([n > 0 and n <= 3 for n in diffs]):
        safe_reports += 1

print(safe_reports)
