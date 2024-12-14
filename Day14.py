import math
import sys


def find_safety_factor(start_positions, velocities, seconds_number, width, height):
    first_quadrant = 0
    second_quadrant = 0
    third_quadrant = 0
    forth_quadrant = 0
    assert len(start_positions) == len(velocities)
    i = 0
    while i < len(start_positions):
        res_x = (start_positions[i][0] + velocities[i][0] * seconds_number) % width
        res_y = (start_positions[i][1] + velocities[i][1] * seconds_number) % height
        if res_x < width / 2 - 1 and res_y < height / 2 - 1:
            first_quadrant += 1
        elif res_x > width / 2 and res_y < height / 2 - 1:
            second_quadrant += 1
        elif res_x < width / 2 - 1 and res_y > height / 2:
            third_quadrant += 1
        elif res_x > width / 2 and res_y > height / 2:
            forth_quadrant += 1
        i += 1
    return first_quadrant * second_quadrant * third_quadrant * forth_quadrant


def actually_drawing_robots(start_positions, velocities, seconds_number, width, height):
    for second in range(seconds_number):
        field = []
        for i in range(height):
            field.append([' '] * width)

        for i in range(len(start_positions)):
            res_x = (start_positions[i][0] + velocities[i][0] * second) % width
            res_y = (start_positions[i][1] + velocities[i][1] * second) % height
            field[res_y][res_x] = 'X'
        for i in field:
            for j in i:
                print(j, end="")
            print()

def actually_drawing_robots_2(start_positions, velocities, seconds_number, width, height):
    coeff = 0.05
    printed = 0
    for second in range(seconds_number):
        field = []
        for i in range(height):
            field.append([' '] * width)

        first_quadrant = 0
        second_quadrant = 0
        third_quadrant = 0
        forth_quadrant = 0

        for i in range(len(start_positions)):
            res_x = (start_positions[i][0] + velocities[i][0] * second) % width
            res_y = (start_positions[i][1] + velocities[i][1] * second) % height
            field[res_y][res_x] = 'X'

            if res_x < width / 2 - 1 and res_y < height / 2 - 1:
                first_quadrant += 1
            elif res_x > width / 2 and res_y < height / 2 - 1:
                second_quadrant += 1
            elif res_x < width / 2 - 1 and res_y > height / 2:
                third_quadrant += 1
            elif res_x > width / 2 and res_y > height / 2:
                forth_quadrant += 1
            i += 1

        quarter = len(start_positions) / 4
        if quarter + quarter * coeff > first_quadrant > quarter - quarter * coeff and \
                quarter + quarter * coeff > second_quadrant > quarter - quarter * coeff and \
                quarter + quarter * coeff > third_quadrant > quarter - quarter * coeff and \
                quarter + quarter * coeff > forth_quadrant > quarter - quarter * coeff:
                print("Second ", second)
                for i in field:
                        for j in i:
                            print(j, end="")
                        print()
                printed += 1
    print("Printed ",printed)


def trying_to_count_module(start_positions, velocities, width, height):
    i = 0
    lcm_x = 1
    lcm_y = 1
    for i in range(len(velocities)):
        lcm_x = math.lcm(lcm_x, velocities[i][0])
        lcm_y = math.lcm(lcm_y, velocities[i][1])

    print("LCM x: ", lcm_x)

    field = []
    for i in range(height):
        field.append([' '] * width)
    for i in range(len(start_positions)):
        res_x = (start_positions[i][0] + velocities[i][0] * lcm_x) % width
        res_y = (start_positions[i][1] + velocities[i][1] * lcm_x) % height
        field[res_y][res_x] = 'X'
    for i in field:
        for j in i:
            print(j, end="")
        print()

    print("LCM y: ", lcm_y)

    field = []
    for i in range(height):
        field.append([' '] * width)
    for i in range(len(start_positions)):
        res_x = (start_positions[i][0] + velocities[i][0] * lcm_y) % width
        res_y = (start_positions[i][1] + velocities[i][1] * lcm_y) % height
        field[res_y][res_x] = 'X'
    for i in field:
        for j in i:
            print(j, end="")
        print()
    total_lcm = math.lcm(lcm_x, lcm_y)

    print("Total lcm: ", total_lcm)

    field = []
    for i in range(height):
        field.append([' '] * width)
    for i in range(len(start_positions)):
        res_x = (start_positions[i][0] + velocities[i][0] * total_lcm) % width
        res_y = (start_positions[i][1] + velocities[i][1] * total_lcm) % height
        field[res_y][res_x] = 'X'
    for i in field:
        for j in i:
            print(j, end="")
        print()

    pass

def actually_drawing_robots_3_with_some_another_euristics(start_positions, velocities, seconds_number, width, height):
    printed = 0
    for second in range(seconds_number):
        robots_pos = set()
        failed = False
        field = []
        for i in range(height):
            field.append([' '] * width)

        for i in range(len(start_positions)):
            res_x = (start_positions[i][0] + velocities[i][0] * second) % width
            res_y = (start_positions[i][1] + velocities[i][1] * second) % height
            if (res_x, res_y) in robots_pos:
                failed = True
                break
            robots_pos.add((res_x, res_y))
            field[res_y][res_x] = 'X'

        if not failed:
            print("Second ", second)
            for i in field:
                    for j in i:
                        print(j, end="")
                    print()
            printed += 1
    print("Printed ",printed)


test_start_positions = [(0, 4), (6, 3), (10, 3), (2, 0), (0, 0), (3, 0), (7, 6), (3, 0), (9, 3), (7, 3), (2, 4), (9, 5)]
test_velocities = [(3, -3), (-1, -3), (-1, 2), (2, -1), (1, 3), (-2, -2), (-1, -3), (-1, -2), (2, 3), (-1, 2), (2, -3),
                   (-3, -3)]

assert find_safety_factor(test_start_positions, test_velocities, 100, 11, 7)

robots_start_positions = []
robots_velocities = []
for line in sys.stdin:
    spl1 = line.strip().split(' ')
    spl2 = spl1[0][2:].split(',')
    robots_start_positions.append((int(spl2[0]), int(spl2[1])))
    spl3 = spl1[1][2:].split(',')
    robots_velocities.append((int(spl3[0]), int(spl3[1])))

print(find_safety_factor(robots_start_positions, robots_velocities, 100, 101, 103))
#actually_drawing_robots(robots_start_positions, robots_velocities, 101*103, 101, 103)
#actually_drawing_robots_2(robots_start_positions, robots_velocities, 101*103, 101, 103)
#trying_to_count_module(robots_start_positions, robots_velocities, 101, 103)
actually_drawing_robots_3_with_some_another_euristics(robots_start_positions, robots_velocities, 101*103, 101, 103) #this one actually works!
