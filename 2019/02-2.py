initial_state = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 9, 19, 1, 5, 19,
                 23, 1, 6, 23, 27, 1, 27, 10, 31, 1, 31, 5, 35, 2, 10, 35, 39, 1, 9, 39,
                 43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 51, 6, 55, 1, 13, 55, 59, 2, 6, 59,
                 63, 1, 63, 5, 67, 2, 10, 67, 71, 1, 9, 71, 75, 1, 75, 13, 79, 1, 10,
                 79, 83, 2, 83, 13, 87, 1, 87, 6, 91, 1, 5, 91, 95, 2, 95, 9, 99, 1, 5,
                 99, 103, 1, 103, 6, 107, 2, 107, 13, 111, 1, 111, 10, 115, 2, 10, 115,
                 119, 1, 9, 119, 123, 1, 123, 9, 127, 1, 13, 127, 131, 2, 10, 131, 135,
                 1, 135, 5, 139, 1, 2, 139, 143, 1, 143, 5, 0, 99, 2, 0, 14, 0]


def run(noun, verb):
    pointer = 0
    prog = initial_state.copy()
    prog[1] = noun
    prog[2] = verb

    while True:
        instruction = prog[pointer:pointer+4]

        operation = instruction[0]

        if operation == 99:
            return prog[0]

        operation, in_x, in_y, output_pos = instruction

        if operation == 1:
            prog[output_pos] = prog[in_x] + prog[in_y]
        elif operation == 2:
            prog[output_pos] = prog[in_x] * prog[in_y]
        else:
            print(f'ERROR Illegal operation {operation} at pos {pointer}')
            exit(1)

        pointer += 4


noun = 0
while noun < 99:
    verb = 0
    while verb < 99:
        res = run(noun, verb)
        if res == 19690720:
            print(100 * noun + verb)
            exit(0)
        verb += 1
    noun += 1
