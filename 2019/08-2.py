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

image = []
for index, pixel in enumerate(layers[0]):
    if int(pixel) < 2:
        image.append(pixel)
        continue
    else:
        for next_layer in range(0, int(num_layers)):
            next_pixel = layers[next_layer][index]
            if int(next_pixel) < 2:
                image.append(next_pixel)
                break

i = 0
for pixel in image:
    i += 1
    if pixel == "1":
        p = "#"
    else:
        p = " "
    print(p, end="")
    if i == width:
        print()
        i = 0
print()
