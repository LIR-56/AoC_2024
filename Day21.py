import sys
from functools import cache


def find_sum_of_complexities_25(input):
    routes_for_lines = find_numeric_keypad_sequences(input)
    result_sum = 0
    for i in range(25):
        routes_for_lines = find_directional_keypad_sequences(routes_for_lines)
        filtered_once_again_routes_for_lines = {}
        for line, routes in routes_for_lines.items():
            min_length = min(map(len, routes))
            filtered_once_again_routes_for_lines[line] = list(filter(lambda l : len(l) <= min_length, routes))
            print(i, min_length, len(routes), len(filtered_once_again_routes_for_lines[line]))
        routes_for_lines = filtered_once_again_routes_for_lines
    for line, routes in routes_for_lines.items():
        min_length = min(map(len, routes))
        result_sum = result_sum + (int(line[:3]) * min_length)
    return result_sum

def find_sum_of_complexities(input):
    routes_for_lines = find_directional_keypad_sequences(find_directional_keypad_sequences(find_numeric_keypad_sequences(input)))
    sum = 0
    for line, routes in routes_for_lines.items():
        min_length = min(map(len, routes))
        sum = sum + (int(line[:3]) * min_length)
    return sum

def find_directional_keypad_sequences(input):
    result = {}
    positions = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
    for line, variants in input.items():
        routes_for_line = set()
        for variant in variants:
            position = (0, 2)
            prefixes = [""]
            for p in variant:
                new_prefixes_addings = get_all_routes_directions(position, positions[p])
                position = positions[p]
                new_prefixes = set()
                for i in prefixes:
                    for j in new_prefixes_addings:
                        new_prefixes.add(i + j + 'A')
                prefixes = new_prefixes
            routes_for_line = routes_for_line | prefixes
        result[line] = routes_for_line
    return result


def find_numeric_keypad_sequences(input):
    result = {}
    positions = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0),
                 '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}  # y, x
    for line in input:
        prefixes = {""}
        position = (3, 2)
        for p in line:
            new_prefixes_addings = get_all_routes_numeric(position, positions[p])
            position = positions[p]
            new_prefixes = set()
            for i in prefixes:
                for j in new_prefixes_addings:
                    new_prefixes.add(i + j + 'A')
            prefixes = new_prefixes
        result[line] = prefixes
    return result


@cache
def get_all_routes_directions(pos_start, pos_end):
    routes = []
    h = get_horizontal(pos_start[1], pos_end[1])
    v = get_vertical(pos_start[0], pos_end[0])
    if pos_start[0] == pos_end[0]:
        routes.append(h * abs(pos_end[1] - pos_start[1]))
    elif pos_start[1] == pos_end[1]:
        routes.append(v * abs(pos_end[0] - pos_start[0]))
    elif abs(pos_start[0] - pos_end[0]) == 1 and abs(pos_start[1] - pos_end[1]) == 1:
        routes.append(h + v)
        routes.append(v + h)
    elif abs(pos_start[1] - pos_end[1]) == 2 and abs(pos_start[0] - pos_end[0]) == 1:
        routes.append(h + h + v)
        routes.append(h + v + h)
        routes.append(v + h + h)
    return filter_result(routes, pos_start, (0, 0))


@cache
def get_all_routes_numeric(pos_start, pos_end):
    routes = []
    h = get_horizontal(pos_start[1], pos_end[1])
    v = get_vertical(pos_start[0], pos_end[0])
    if pos_start[0] == pos_end[0]:
        routes.append(h * abs(pos_end[1] - pos_start[1]))
    elif pos_start[1] == pos_end[1]:
        routes.append(v * abs(pos_end[0] - pos_start[0]))
    elif abs(pos_start[1] - pos_end[1]) == 1 and abs(pos_start[0] - pos_end[0]) == 1:
        routes.append(h + v)
        routes.append(v + h)
    elif abs(pos_start[1] - pos_end[1]) == 1 and abs(pos_start[0] - pos_end[0]) == 2:
        routes.append(v + h + v)
        routes.append(h + v + v)
        routes.append(v + v + h)
    elif abs(pos_start[1] - pos_end[1]) == 2 and abs(pos_start[0] - pos_end[0]) == 1:
        routes.append(h + h + v)
        routes.append(h + v + h)
        routes.append(v + h + h)
    elif abs(pos_start[1] - pos_end[1]) == 1 and abs(pos_start[0] - pos_end[0]) == 3:
        routes.append(h + v + v + v)
        routes.append(v + h + v + v)
        routes.append(v + v + h + v)
        routes.append(v + v + v + h)
    elif abs(pos_start[1] - pos_end[1]) == 2 and abs(pos_start[0] - pos_end[0]) == 3:
        routes.append(h + h + v + v + v)
        routes.append(h + v + h + v + v)
        routes.append(h + v + v + h + v)
        routes.append(h + v + v + v + h)
        routes.append(v + h + h + v + v)
        routes.append(v + h + v + h + v)
        routes.append(v + h + v + v + h)
        routes.append(v + v + h + h + v)
        routes.append(v + v + h + v + h)
        routes.append(v + v + v + h + h)
    elif abs(pos_start[1] - pos_end[1]) == 2 and abs(pos_start[0] - pos_end[0]) == 2:
        routes.append(h + h + v + v)
        routes.append(h + v + h + v)
        routes.append(h + v + v + h)
        routes.append(v + h + h + v)
        routes.append(v + h + v + h)
        routes.append(v + v + h + h)
    return filter_result(routes, pos_start, (3, 0))


def filter_result(routes, pos_start, panic_point):
    result = []
    for route in routes:
        y = pos_start[0]
        x = pos_start[1]
        failed = False
        for move in route:
            if y == panic_point[0] and x == panic_point[1]:
                failed = True
            if move == '<':
                x -= 1
            elif move == '>':
                x += 1
            elif move == '^':
                y -= 1
            elif move == 'v':
                y += 1
            elif move != 'A':
                raise Exception("SomethingWrong in this string")
        if not failed:
            result.append(route)
    return result


def get_horizontal(x1, x2):
    return '<' if x1 > x2 else '>'


def get_vertical(y1, y2):
    return '^' if y1 > y2 else 'v'

test_codes = ['029A', '980A', '179A', '456A', '379A']
#assert find_sum_of_complexities(test_codes) == 126384


codes = []
for line in sys.stdin:
    codes.append(line.strip())
#print(find_sum_of_complexities(codes))
print(find_sum_of_complexities_25(codes))
