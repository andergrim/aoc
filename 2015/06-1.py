lights = {}

for y in range(0, 1000):
    for x in range(0, 1000):
        lights[(x, y)] = False


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
                    lights[(x, y)] = True
                elif operation == "off":
                    lights[(x, y)] = False
                else:
                    if lights[(x, y)]:
                        lights[(x, y)] = False
                    else:
                        lights[(x, y)] = True
        print(f"{operation} ({num} lights)")

print("Counting...")
turned_on = list(lights.values()).count(True)
print(turned_on)
