class Fish:
    _value = 0
    
    def __init__(self, value=8):
        self._value = value

    def cycle(self):
        if self._value == 0:
            self._value = 6
        else:
            self._value -= 1

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return repr(self._value)


fishes = []

with open("06.txt") as fp:
    initial = [int(n) for n in fp.read().strip().split(",")]

for value in initial:
    fishes.append(Fish(value))

for i in range(0, 80):
    spawned = []
    for fish in fishes:
        if fish.value == 0:
            spawned.append(Fish())
        fish.cycle()
    fishes += spawned

print(len(fishes))
