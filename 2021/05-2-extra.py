import re
from PIL import Image


points = []
intersections = {}
img = Image.new("RGB", (1000, 1000))

def add_point(point):
    if point in points:
        # print(f" Point {point} intersects")
        intersections[point] = intersections.get(point, 1) + 1
        img.putpixel(point, (255, 0, 0))
    else:
        # print(f" Adding point {point}")
        points.append(point)
        img.putpixel(point, (255, 255, 255))

pattern = re.compile(r"^([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)\n$", flags=re.MULTILINE)

with open('05.txt', encoding="utf-8") as fp:
    for line in fp:
        matches = pattern.match(line).groups()
        start_x, start_y, end_x, end_y = [int(m) for m in matches]

        # Set step depending on line direction
        if start_x > end_x:
            step_x = -1
        else:
            step_x = 1

        if start_y > end_y:
            step_y = -1
        else:
            step_y = 1

        if start_x == end_x or start_y == end_y:
            # Horizontal and vertical lines
            for x in range(start_x, end_x + step_x, step_x):
                for y in range(start_y, end_y + step_y, step_y):
                    add_point((x, y))
        else:
            # Diagonal line
            range_x = range(start_x, end_x + step_x, step_x)
            range_y = range(start_y, end_y + step_y, step_y)
            for point in zip(range_x, range_y):
                add_point(point)

print(f"Added {len(points)} points and {len(intersections)} intersections.")
img.save("05-output.png")
