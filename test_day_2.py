from day_2 import intcode_computer, find_noun_and_verb
from sys import stdin

# How to run this test: pytest -s test_day_2.py < input/day_2.txt
my_input = list(map(int, stdin.readline().split(',')))


def test_intcode_computer():
    assert intcode_computer([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert intcode_computer([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert intcode_computer([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert intcode_computer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [
        3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert intcode_computer([1, 0, 0, 4, 99, 5, 6, 0, 99]) == [
        30, 0, 0, 4, 2, 5, 6, 0, 99]


def test_find_noun_and_verb():
    assert find_noun_and_verb([1, 0, 0, 0, 99], 2) == (0, 0)
    assert find_noun_and_verb([2, 3, 0, 3, 99], 2) == (0, 0)
    assert find_noun_and_verb(
        [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500) == (9, 10)
    assert find_noun_and_verb([1, 1, 1, 4, 99, 5, 6, 0, 99], 30) == (0, 0)


def test_incode_computer_with_my_input():
    program_input = my_input.copy()
    program_input[1] = 12
    program_input[2] = 2
    intcode = intcode_computer(program_input)
    assert intcode[0] == 4484226


def test_find_noun_and_verb_with_my_input():
    program_input = my_input.copy()
    assert find_noun_and_verb(program_input, 19690720) == (56, 96)
