# data = "123456789012"
# width = 3
# height = 2

with open("08-input.txt", "r") as fp:
    data = fp.read().replace("\n", "")

width = 25
height = 6

layers = []

num_layers = len(data) / (width * height)
i = 0
while i < num_layers:
    start = i * (width * height)
    end = start + (width * height)
    layers.append(tuple(data[start:end]))
    i += 1

fewest_zero_layer = min([(l.count("0"), l) for l in layers])
solution = fewest_zero_layer[1].count("1") * fewest_zero_layer[1].count("2")
print(solution)
