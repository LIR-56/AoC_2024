import sys


def count_distinct_path_positions(map, start_x, start_y):
    guard_direction = 0
    leave_the_map = False
    pos_x = start_x
    pos_y = start_y
    my_map = []
    for i in map:
        my_map.append(i.copy())  # we are going to change that
    while not leave_the_map:
        if guard_direction == 0:
            if pos_y > 0:
                if my_map[pos_y - 1][pos_x] == '.' or my_map[pos_y - 1][pos_x] == 'X':
                    my_map[pos_y][pos_x] = 'X'
                    pos_y -= 1
                else:
                    guard_direction = 1
            else:
                my_map[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 1:
            if pos_x < len(my_map[pos_y]) - 1:
                if my_map[pos_y][pos_x + 1] == '.' or my_map[pos_y][pos_x + 1] == 'X':
                    my_map[pos_y][pos_x] = 'X'
                    pos_x += 1
                else:
                    guard_direction = 2
            else:
                my_map[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 2:
            if pos_y < len(my_map) - 1:
                if my_map[pos_y + 1][pos_x] == '.' or my_map[pos_y + 1][pos_x] == 'X':
                    my_map[pos_y][pos_x] = 'X'
                    pos_y += 1
                else:
                    guard_direction = 3
            else:
                my_map[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 3:
            if pos_x > 0:
                if my_map[pos_y][pos_x - 1] == '.' or my_map[pos_y][pos_x - 1] == 'X':
                    my_map[pos_y][pos_x] = 'X'
                    pos_x -= 1
                else:
                    guard_direction = 0
            else:
                my_map[pos_y][pos_x] = 'X'
                leave_the_map = True
    result = 0
    for i in my_map:
        result += i.count('X')
    return result


def count_distinct_loop_obstruction_positions(map, start_x, start_y):
    # straightforward bruteforce with O^2 difficulty; takes dozens of second to complete
    number_of_obstructions_for_looping = 0
    i = 0
    while i < len(map):
        j = 0
        while j < len(map[i]):
            if map[i][j] == '.':
                my_map = []
                for k in map:
                    my_map.append(k.copy())  # we are going to change that
                my_map[i][j] = '#'
                if is_loopable(my_map, start_x, start_y):
                    number_of_obstructions_for_looping += 1
            j += 1
        i += 1
    return number_of_obstructions_for_looping


def is_loopable(lab_map_with_obstruction, start_x, start_y):
    steps_for_loop = len(lab_map_with_obstruction) * len(lab_map_with_obstruction) * 4
    guard_direction = 0
    leave_the_map = False
    pos_x = start_x
    pos_y = start_y
    while not (leave_the_map or steps_for_loop == 0):
        steps_for_loop -= 1
        if guard_direction == 0:
            if pos_y > 0:
                if lab_map_with_obstruction[pos_y - 1][pos_x] == '.' or lab_map_with_obstruction[pos_y - 1][
                    pos_x] == 'X':
                    lab_map_with_obstruction[pos_y][pos_x] = 'X'
                    pos_y -= 1
                else:
                    guard_direction = 1
            else:
                lab_map_with_obstruction[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 1:
            if pos_x < len(lab_map_with_obstruction[pos_y]) - 1:
                if lab_map_with_obstruction[pos_y][pos_x + 1] == '.' or lab_map_with_obstruction[pos_y][
                    pos_x + 1] == 'X':
                    lab_map_with_obstruction[pos_y][pos_x] = 'X'
                    pos_x += 1
                else:
                    guard_direction = 2
            else:
                lab_map_with_obstruction[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 2:
            if pos_y < len(lab_map_with_obstruction) - 1:
                if lab_map_with_obstruction[pos_y + 1][pos_x] == '.' or lab_map_with_obstruction[pos_y + 1][
                    pos_x] == 'X':
                    lab_map_with_obstruction[pos_y][pos_x] = 'X'
                    pos_y += 1
                else:
                    guard_direction = 3
            else:
                lab_map_with_obstruction[pos_y][pos_x] = 'X'
                leave_the_map = True
        elif guard_direction == 3:
            if pos_x > 0:
                if lab_map_with_obstruction[pos_y][pos_x - 1] == '.' or lab_map_with_obstruction[pos_y][
                    pos_x - 1] == 'X':
                    lab_map_with_obstruction[pos_y][pos_x] = 'X'
                    pos_x -= 1
                else:
                    guard_direction = 0
            else:
                lab_map_with_obstruction[pos_y][pos_x] = 'X'
                leave_the_map = True
    return steps_for_loop == 0


test_map = [
    list('....#.....'),
    list('.........#'),
    list('..........'),
    list('..#.......'),
    list('.......#..'),
    list('..........'),
    list('.#..^.....'),
    list('........#.'),
    list('#.........'),
    list('......#...')
]
test_start_x = 4
test_start_y = 6

assert count_distinct_path_positions(test_map, 4, 6) == 41
assert count_distinct_loop_obstruction_positions(test_map, 4, 6) == 6

lab_map = []
start_x_pos = 0
start_y_pos = 0
for line in sys.stdin:
    lab_map.append(list(line.strip()))
    if "^" in line:
        start_y_pos = len(lab_map) - 1
        start_x_pos = line.index("^")
print(count_distinct_path_positions(lab_map, start_x_pos, start_y_pos))
print(count_distinct_loop_obstruction_positions(lab_map, start_x_pos, start_y_pos))
