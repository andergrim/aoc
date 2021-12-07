import re


points = []
intersections = {}

def add_point(point):
    if point in points:
        # print(f" Point {point} intersects")
        intersections[point] = intersections.get(point, 1) + 1
    else:
        # print(f" Adding point {point}")
        points.append(point)

pattern = re.compile(r"^([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)\n$", flags=re.MULTILINE)
with open('05-test.txt', encoding="utf-8") as fp:
    for line in fp:
        matches = pattern.match(line).groups()
        start_x, start_y, end_x, end_y = [int(m) for m in matches]

        if start_x == end_x or start_y == end_y:
            if start_y > end_y:
                step_y = -1
            else:
                step_y = 1

            if start_x > end_x:
                step_x = -1
            else:
                step_x = 1

            for x in range(start_x, end_x + step_x, step_x):
                for y in range(start_y, end_y + step_y, step_y):
                    add_point((x, y))

print(f"Added {len(points)} points and {len(intersections)} intersections.")
