from day_4 import different_passwords, different_passwords_2


def test_different_passwords():
    # double 11, never decreases
    assert different_passwords(111111, 111111) == 1
    # decreasing pair of digits 50
    assert different_passwords(223450, 223450) == 0
    # no double
    assert different_passwords(123789, 123789) == 0


def test_different_passwords_2():
    # the digits never decrease and all repeated digits are exactly two digits long
    assert different_passwords_2(112233, 112233) == 1
    # the repeated 44 is part of a larger group of 444
    assert different_passwords_2(123444, 123444) == 0
    # even though 1 is repeated more than twice, it still contains a double 22
    assert different_passwords_2(111122, 111122) == 1
