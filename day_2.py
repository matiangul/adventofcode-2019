from sys import stdin

HALT = 99
ADD = 1
MULTIPLY = 2


def calculate(opcode, first, second):
    if (opcode == ADD):
        return first + second
    if (opcode == MULTIPLY):
        return first * second
    raise RuntimeError("Unknown opcode!", opcode)


def intcode_computer(integers):
    iterator = 0
    while (integers[iterator] != HALT):
        opcode = integers[iterator]
        first = integers[integers[iterator + 1]]
        second = integers[integers[iterator + 2]]
        integers[integers[iterator + 3]] = calculate(opcode, first, second)
        iterator += 4
    return integers


def find_noun_and_verb(integers, desired_output):
    for noun in range(0, 100, 1):
        for verb in range(0, 100, 1):
            ints = integers.copy()
            ints[1] = noun
            ints[2] = verb
            iterator = 0
            while (ints[iterator] != HALT):
                if (ints[iterator + 1] >= len(ints) or
                        ints[iterator + 2] >= len(ints) or
                        ints[iterator + 3] >= len(ints)):
                    break
                opcode = ints[iterator]
                first = ints[ints[iterator + 1]]
                second = ints[ints[iterator + 2]]
                ints[ints[iterator + 3]
                     ] = calculate(opcode, first, second)
                iterator += 4
            if (ints[0] == desired_output):
                return (noun, verb)


if __name__ == "__main__":
    program_input = list(map(int, stdin.readline().split(',')))
    first_program_input = program_input.copy()
    first_program_input[1] = 12
    first_program_input[2] = 2
    resulting_intcode = intcode_computer(first_program_input)
    print("Part 1: ", resulting_intcode[0])
    noun, verb = find_noun_and_verb(program_input.copy(), 19690720)
    print("Part 2: ", 100 * noun + verb)
