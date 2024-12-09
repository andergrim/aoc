with open("02.txt") as fp:
    reports = [list(map(int, line.split())) for line in fp.readlines()]

safe_reports = 0

for report in reports:

    candidates = [report]
    for i in range(len(report)):
        alt_report = [el for el in report]
        del(alt_report[i])
        candidates.append(alt_report)

    diffs = []
    for candidate in candidates:
        diffs.append(
            [candidate[offset] - candidate[offset + 1] for offset in range(len(candidate) - 1)]
        )

    results = [] 
    for diff in diffs:
        results.append(
            all([n < 0 and n >= -3 for n in diff]) or all([n > 0 and n <= 3 for n in diff])
        )


    if(any(results)):
        safe_reports += 1

print(safe_reports)
