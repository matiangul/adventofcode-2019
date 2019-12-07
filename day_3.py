# find the intersection point closest to the central port
from sys import stdin

RIGHT = 'R'
UP = 'U'
LEFT = 'L'
DOWN = 'D'


def closest_intersection(first_wire, second_wire):
    return closest_distance(all_intersections(first_wire, second_wire))


def closest_distance(intersections):
    return min({taxicab_distance((0, 0), x) for x in intersections})


def taxicab_distance(start, stop):
    return abs(start[0] - stop[0]) + abs(start[1] - stop[1])


def fewest_steps_intersection(first_wire, second_wire):
    return fewest_steps(all_intersections(first_wire, second_wire))


def fewest_steps(intersections):
    return min({x[2] for x in intersections})


def all_intersections(first_wire, second_wire):
    intersections = set()
    moves = list()
    # (x (from, to), y (from, to))
    move = ((0, 0), (0, 0), 0)

    for cmd in first_wire:
        direction = cmd[0]
        distance = int(cmd[1:])

        diff_x = -1 * distance if direction == LEFT else distance if direction == RIGHT else 0
        diff_y = -1 * distance if direction == DOWN else distance if direction == UP else 0

        init_x = move[0][1]
        init_y = move[1][1]
        init_steps = move[2]

        move = ((init_x, init_x + diff_x), (init_y, init_y + diff_y),
                init_steps + abs(diff_x) + abs(diff_y))
        moves.append(move)

    move = ((0, 0), (0, 0), 0)

    for cmd in second_wire:
        direction = cmd[0]
        distance = int(cmd[1:])

        diff_x = -1 * distance if direction == LEFT else distance if direction == RIGHT else 0
        diff_y = -1 * distance if direction == DOWN else distance if direction == UP else 0

        init_x = move[0][1]
        init_y = move[1][1]
        init_steps = move[2]

        move = ((init_x, init_x + diff_x), (init_y, init_y + diff_y),
                init_steps + abs(diff_x) + abs(diff_y))

        for m in moves:
            i = intersection(m, move)
            if (i is None or (i[0] == 0 and i[1] == 0)):
                continue
            else:
                intersections.add(i)

    return intersections


def intersection(m1, m2):
    # m1 vertical
    # m2 horizontal
    if (m1[0][0] == m1[0][1] and m2[1][0] == m2[1][1] and min(m1[1]) <= m2[1][0] and m2[1][0] <= max(m1[1]) and min(m2[0]) <= m1[0][0] and m1[0][0] <= max(m2[0])):
        return (m1[0][0], m2[1][0], m1[2] + m2[2] - abs(m1[1][1] - m2[1][0]) - abs(m2[0][1] - m1[0][0]))
    # other way
    if (m2[0][0] == m2[0][1] and m1[1][0] == m1[1][1] and min(m2[1]) <= m1[1][0] and m1[1][0] <= max(m2[1]) and min(m1[0]) <= m2[0][0] and m2[0][0] <= max(m1[0])):
        return (m2[0][0], m1[1][0], m2[2] + m1[2] - abs(m2[1][1] - m1[1][0]) - abs(m1[0][1] - m2[0][0]))
    return None


if __name__ == "__main__":
    lines = stdin.readlines()
    first_wire = lines[0].split(',')
    second_wire = lines[1].split(',')
    print("Closest: ", closest_intersection(first_wire, second_wire))
    print("Fewest steps: ", fewest_steps_intersection(first_wire, second_wire))
