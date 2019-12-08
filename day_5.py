from sys import stdin

HALT = 99
ADD = 1
MULTIPLY = 2
SAVE_INPUT = 3
OUTPUT = 4


def steps_to_move(opcode):
    if (opcode == ADD):
        return 4
    if (opcode == MULTIPLY):
        return 4
    if (opcode == SAVE_INPUT):
        return 2
    if (opcode == OUTPUT):
        return 2
    raise RuntimeError("Unknown opcode!", opcode)


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
        program_output.append(integers[parameters[0]])
    else:
        raise RuntimeError("Unknown opcode!", opcode)


def intcode_computer(integers, program_input):
    program_output = []
    iterator = 0
    while (integers[iterator] != HALT):
        opcode = integers[iterator] % 10
        opcode_steps = steps_to_move(opcode)
        parameter_count = opcode_steps - 1
        parameter_modes = [0] * parameter_count
        for m in range(2, parameter_count + 2):
            parameter_modes[m-2] = integers[iterator] // 10**m % 10
        parameters = integers[iterator+1:iterator+opcode_steps]
        run(integers, program_input, program_output,
            parameter_modes, opcode, parameters)
        iterator += opcode_steps
    return (integers, program_output)


if __name__ == "__main__":
    intcode = list(map(int, stdin.readline().split(',')))
    (_, program_output) = intcode_computer(intcode, [1])
    print("Part 1: ", program_output.pop())
