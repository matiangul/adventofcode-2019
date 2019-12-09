from sys import stdin
import day_5


def test_opcode_steps():
    try:
        day_5.get_opcode_steps(day_5.HALT)
        assert True == False
    except:
        assert True == True
    assert day_5.get_opcode_steps(day_5.ADD) == 4
    assert day_5.get_opcode_steps(day_5.MULTIPLY) == 4
    assert day_5.get_opcode_steps(day_5.SAVE_INPUT) == 2
    assert day_5.get_opcode_steps(day_5.OUTPUT) == 2


def test_input_output():
    intcode = [3, 2, 0, 1, 4, 6, 99]
    (_, program_output) = day_5.intcode_computer(intcode, [4])
    assert program_output == [2, 99]


def test_intcode_computer():
    intcode = [1101, 100, -1, 4, 0]
    (resulting_intcode, _) = day_5.intcode_computer(intcode, [])
    assert resulting_intcode == [1101, 100, -1, 4, 99]
    intcode = [1002, 4, 3, 4, 33]
    (resulting_intcode, _) = day_5.intcode_computer(intcode, [])
    assert resulting_intcode == [1002, 4, 3, 4, 99]


def test_jumps_and_compares_intcode_computer():
    intcode = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
               1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
               999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    (_, output) = day_5.intcode_computer(intcode, [8])
    assert output.pop() == 1000
    intcode_2 = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    (_, output_2) = day_5.intcode_computer(intcode_2, [7])
    assert output_2.pop() == 999
    intcode_3 = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    (_, output_3) = day_5.intcode_computer(intcode_3, [9])
    assert output_3.pop() == 1001


my_input = list(map(int, stdin.readline().split(',')))


def test_with_my_input():
    intcode = my_input.copy()
    (_, output) = day_5.intcode_computer(intcode, [1])
    assert output.pop() == 7566643
