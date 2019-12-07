from sys import stdin


def digit(number, index):
    return number // 10**index % 10


def different_passwords(range_start, range_end):
    sum = 0
    for password in range(range_start, range_end + 1):
        digits = [digit(password, 0), digit(password, 1), digit(password, 2), digit(
            password, 3), digit(password, 4), digit(password, 5)]
        never_decrease = digits[0] >= digits[1] >= digits[2] >= digits[3] >= digits[4] >= digits[5]
        adjacent_digits_same = digits[0] == digits[1] or digits[1] == digits[
            2] or digits[2] == digits[3] or digits[3] == digits[4] or digits[4] == digits[5]
        if (never_decrease and adjacent_digits_same):
            sum += 1
    return sum


def different_passwords_2(range_start, range_end):
    sum = 0
    for password in range(range_start, range_end + 1):
        digits = [digit(password, 0), digit(password, 1), digit(password, 2), digit(
            password, 3), digit(password, 4), digit(password, 5)]
        never_decrease = digits[0] >= digits[1] >= digits[2] >= digits[3] >= digits[4] >= digits[5]
        two_adjacent_digits_same = (digits[0] == digits[1] and digits[0] != digits[2]) \
            or (digits[1] == digits[2] and digits[1] != digits[0] and digits[1] != digits[3]) \
            or (digits[2] == digits[3] and digits[2] != digits[1] and digits[2] != digits[4]) \
            or (digits[3] == digits[4] and digits[3] != digits[2] and digits[3] != digits[5]) \
            or (digits[4] == digits[5] and digits[4] != digits[3])
        if (never_decrease and two_adjacent_digits_same):
            sum += 1
    return sum


if __name__ == "__main__":
    password_range = stdin.readlines()[0].split('-')
    print("Part 1: ", different_passwords(
        int(password_range[0]), int(password_range[1])))
    print("Part 2: ", different_passwords_2(
        int(password_range[0]), int(password_range[1])))
