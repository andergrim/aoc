def similarity(a, b):
    common = ""
    for i in range(0, len(b)):
        if a[i] == b[i]:
            common += a[i]
    return common

with open("02-1.txt", "r") as f:
    boxes = f.readlines() 

for box in boxes:
    for other in boxes:
        if box != other:
            diff = similarity(box, other)
            if len(diff) == len(box) - 1:
                print(diff)
                exit(0)
