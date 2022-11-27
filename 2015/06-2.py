lights = {}

for y in range(0, 1000):
    for x in range(0, 1000):
        lights[(x, y)] = 0


with open('06.txt') as fp:
    for line in fp:
        # Cleanup
        line = line.strip()
        line = line.replace("turn ", "")
        line = line.replace("through ", "")

        # Parse
        operation, start, end = line.split(" ")
        start = tuple(int(n) for n in start.split(","))
        end = tuple(int(n) for n in end.split(","))

        num = 0
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                num += 1
                if operation == "on":
                    lights[(x, y)] += 1
                elif operation == "off":
                    if lights[(x, y)] > 0:
                        lights[(x, y)] -= 1
                else:
                    lights[(x, y)] += 2

        print(f"{operation} ({num} lights)")

print(f"Sumarizing {len(lights)} lights...")
brightness = sum(lights.values())
print(brightness)
