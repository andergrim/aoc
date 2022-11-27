import math


def fuel_for_mass(mass):
    fuel = math.floor(mass / 3) - 2

    if fuel < 1:
        return 0
    else:
        return fuel + fuel_for_mass(fuel)


print('Mass       Fuel')
print('------------------------')

fuel_total = 0
with open('01.txt') as fp:
    # fp = ['12', '14', '1969', '100756']
    for line in fp:
        mass = int(line.strip())
        fuel = fuel_for_mass(mass)
        fuel_total += fuel
        print(f'{mass} {fuel} {fuel_total}')


print('------------------------')
print(f'Total fuel: {fuel_total}')
