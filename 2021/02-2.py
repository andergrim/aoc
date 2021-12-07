from dataclasses import dataclass
from parse import parse


@dataclass
class Position:
    aim: int = 0
    depth: int = 0
    horizontal_position: int = 0

    def __repr__(self):
        return str(self.depth * self.horizontal_position)

    def move(self, direction, distance):
        match direction:
            case "up":
                self.aim -= distance
            case "down":
                self.aim += distance
            case "forward":
                self.horizontal_position += distance
                self.depth += self.aim * distance


position = Position()

with open('02.txt', encoding="utf-8") as fp:
    for line in fp:
        _direction, _distance = parse("{} {:d}", line.strip())
        position.move(_direction, _distance)

print(position)
