import math

print('Mass       Fuel')
print('------------------------')

fuel_total = 0
with open('01.txt') as fp:
    for line in fp:
        mass = int(line.strip())
        fuel = math.floor(mass / 3) - 2
        fuel_total += fuel
        print(f'{str(mass).ljust(10, " ")} {fuel} {fuel_total}')

print('------------------------')
print(f'Total fuel: {fuel_total}')
