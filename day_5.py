from sys import stdin

HALT = 99
ADD = 1
MULTIPLY = 2
SAVE_INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8


def get_opcode_steps(opcode):
    if (opcode == ADD):
        return 4
    if (opcode == MULTIPLY):
        return 4
    if (opcode == SAVE_INPUT):
        return 2
    if (opcode == OUTPUT):
        return 2
    if (opcode == JUMP_IF_TRUE):
        return 3
    if (opcode == JUMP_IF_FALSE):
        return 3
    if (opcode == LESS_THAN):
        return 4
    if (opcode == EQUALS):
        return 4
    raise RuntimeError("Unknown opcode!", opcode)


def get_next_iterator(iterator, integers, parameter_modes, opcode, parameters):
    regular = iterator + get_opcode_steps(opcode)
    if (opcode == JUMP_IF_TRUE):
        to_compare = integers[parameters[0]
                              ] if parameter_modes[0] == 0 else parameters[0]
        new_pointer = integers[parameters[1]
                               ] if parameter_modes[1] == 0 else parameters[1]
        return new_pointer if to_compare != 0 else regular
    elif (opcode == JUMP_IF_FALSE):
        to_compare = integers[parameters[0]
                              ] if parameter_modes[0] == 0 else parameters[0]
        new_pointer = integers[parameters[1]
                               ] if parameter_modes[1] == 0 else parameters[1]
        return new_pointer if to_compare == 0 else regular
    else:
        return regular


def run(integers, program_input, program_output, parameter_modes, opcode, parameters):
    if (opcode == ADD):
        first = integers[parameters[0]
                         ] if parameter_modes[0] == 0 else parameters[0]
        second = integers[parameters[1]
                          ] if parameter_modes[1] == 0 else parameters[1]
        integers[parameters[2]] = first + second
    elif (opcode == MULTIPLY):
        first = integers[parameters[0]
                         ] if parameter_modes[0] == 0 else parameters[0]
        second = integers[parameters[1]
                          ] if parameter_modes[1] == 0 else parameters[1]
        integers[parameters[2]] = first * second
    elif (opcode == SAVE_INPUT):
        integers[parameters[0]] = int(program_input.pop(0))
    elif (opcode == OUTPUT):
        to_output = integers[parameters[0]
                             ] if parameter_modes[0] == 0 else parameters[0]
        program_output.append(to_output)
    elif (opcode == LESS_THAN):
        first = integers[parameters[0]
                         ] if parameter_modes[0] == 0 else parameters[0]
        second = integers[parameters[1]
                          ] if parameter_modes[1] == 0 else parameters[1]
        integers[parameters[2]] = 1 if first < second else 0
    elif (opcode == EQUALS):
        first = integers[parameters[0]
                         ] if parameter_modes[0] == 0 else parameters[0]
        second = integers[parameters[1]
                          ] if parameter_modes[1] == 0 else parameters[1]
        integers[parameters[2]] = 1 if first == second else 0
    elif (opcode == JUMP_IF_TRUE):
        return
    elif (opcode == JUMP_IF_FALSE):
        return
    else:
        raise RuntimeError("Unknown opcode!", opcode)


def intcode_computer(integers, program_input):
    program_output = []
    iterator = 0
    while (integers[iterator] != HALT):
        opcode = integers[iterator] % 10
        opcode_steps = get_opcode_steps(opcode)
        parameter_count = opcode_steps - 1
        parameter_modes = [0] * parameter_count
        for m in range(2, parameter_count + 2):
            parameter_modes[m-2] = integers[iterator] // 10**m % 10
        parameters = integers[iterator+1:iterator+opcode_steps]
        run(integers, program_input, program_output,
            parameter_modes, opcode, parameters)
        iterator = get_next_iterator(
            iterator, integers, parameter_modes, opcode, parameters)
    return (integers, program_output)


if __name__ == "__main__":
    intcode = list(map(int, stdin.readline().split(',')))
    (_, program_output_1) = intcode_computer(intcode.copy(), [1])
    print("Part 1: ", program_output_1.pop())
    (_, program_output_2) = intcode_computer(intcode.copy(), [5])
    print("Part 2: ", program_output_2.pop())
