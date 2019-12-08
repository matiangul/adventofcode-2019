from sys import stdin
import day_5

def test_steps_to_move():
    try:
        day_5.steps_to_move(day_5.HALT)
        assert True == False
    except:
        assert True == True
    assert day_5.steps_to_move(day_5.ADD) == 4
    assert day_5.steps_to_move(day_5.MULTIPLY) == 4
    assert day_5.steps_to_move(day_5.SAVE_INPUT) == 2
    assert day_5.steps_to_move(day_5.OUTPUT) == 2

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

my_input = list(map(int, stdin.readline().split(',')))

def test_with_my_input():
    intcode = my_input.copy()
    (_, output) = day_5.intcode_computer(intcode, [1])
    assert output.pop() == 7566643
