freq = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

with open('03.txt', encoding="utf-8") as fp:
    for line in fp:
        bits = line.strip()
        pos = 0
        for bit in bits:
            freq[int(bit)][pos] += 1
            pos += 1

gamma_bits = []
epsilon_bits = []
for i in range(0, 12):
    if freq[0][i] > freq[1][i]:
        gamma_bits.append("0")
        epsilon_bits.append("1")
    else:
        gamma_bits.append("1")
        epsilon_bits.append("0")

gamma = int("0b"+"".join(gamma_bits), 2)
epsilon = int("0b"+"".join(epsilon_bits), 2)

print(gamma * epsilon)
