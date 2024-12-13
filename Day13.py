import sys


def find_fewest_tokens(x_A_changes, x_B_changes, y_A_changes, y_B_changes, x_prizes, y_prizes):
    sum_min = 0
    i = 0
    while i < len(x_prizes):
        sum_min += count_min_tokens_for_prize(x_A_changes[i], x_B_changes[i], y_A_changes[i], y_B_changes[i],
                                              x_prizes[i], y_prizes[i])
        i += 1
    return sum_min


def count_min_tokens_for_prize(x_A_change, x_B_change, y_A_change, y_B_change, x_prize, y_prize):
    min_tokens = sys.maxsize
    for i in range(100):
        for j in range(100):
            if i * x_A_change + j * x_B_change == x_prize and i * y_A_change + j * y_B_change == y_prize:
                if 3 * i + j < min_tokens:
                    min_tokens = 3 * i + j
    if min_tokens == sys.maxsize:
        return 0
    return min_tokens


def find_fewest_tokens_2(x_A_changes, x_B_changes, y_A_changes, y_B_changes, x_prizes, y_prizes):
    sum_min = 0
    i = 0
    while i < len(x_prizes):
        sum_min += count_min_tokens_for_prize_2(x_A_changes[i], x_B_changes[i], y_A_changes[i], y_B_changes[i],
                                                x_prizes[i] + 10000000000000, y_prizes[i] + 10000000000000)
        i += 1
    return sum_min


def count_min_tokens_for_prize_2(x_A_change, x_B_change, y_A_change, y_B_change, x_prize, y_prize):
    # (1) i * Ax + j * Bx = X
    # (2) i * Ay + j * By = Y
    # =>
    # (1) + (-Ax / Ay) * (2)
    # j * (Bx) + j * ((By) * (-Ax) / Ay) = X + (Y * (-Ax) / Ay)
    #               => j = (X + Y * (-Ax) / Ay) / (Bx + By * (-Ax) / Ay)
    # (1) and knowing j
    # i * (Ax) + j * (Bx) = X -> i = (X - j * Bx) / Ax

    j = (x_prize + (-1 * y_prize * x_A_change / y_A_change)) / (
            x_B_change + (-1 * (y_B_change * x_A_change) / y_A_change))
    j = round(j, 3)
    if j == int(j):
        i = (x_prize - j * x_B_change) / x_A_change
        i = round(i, 3)
        if i == int(i) and i * x_A_change + j * x_B_change == x_prize and i * y_A_change + j * y_B_change == y_prize:
            return 3 * i + j
    return 0


test_x_A_changes = [94, 26, 17, 69]
test_x_B_changes = [22, 67, 84, 27]
test_y_A_changes = [34, 66, 86, 23]
test_y_B_changes = [67, 21, 37, 71]
test_x_prizes = [8400, 12748, 7870, 18641]
test_y_prizes = [5400, 12176, 6450, 10279]

assert find_fewest_tokens(test_x_A_changes, test_x_B_changes,
                          test_y_A_changes, test_y_B_changes,
                          test_x_prizes, test_y_prizes) == 480

assert (count_min_tokens_for_prize_2(test_x_A_changes[0], test_x_B_changes[0],
                                   test_y_A_changes[0], test_y_B_changes[0],
                                   test_x_prizes[0] + 10000000000000, test_y_prizes[0] + 10000000000000)) == 0

assert (count_min_tokens_for_prize_2(test_x_A_changes[1], test_x_B_changes[1],
                                   test_y_A_changes[1], test_y_B_changes[1],
                                   test_x_prizes[1] + 10000000000000, test_y_prizes[1] + 10000000000000)) != 0

assert (count_min_tokens_for_prize_2(test_x_A_changes[2], test_x_B_changes[2],
                                   test_y_A_changes[2], test_y_B_changes[2],
                                   test_x_prizes[2] + 10000000000000, test_y_prizes[2] + 10000000000000)) == 0

assert (count_min_tokens_for_prize_2(test_x_A_changes[3], test_x_B_changes[3],
                                   test_y_A_changes[3], test_y_B_changes[3],
                                   test_x_prizes[3] + 10000000000000, test_y_prizes[3] + 10000000000000)) != 0


x_A_changes = []
x_B_changes = []
y_A_changes = []
y_B_changes = []
x_prizes = []
y_prizes = []
for line in sys.stdin:
    if line.startswith("Button A"):
        values = line.strip().split(' ')
        x_A_changes.append(int(values[2][2:-1]))
        y_A_changes.append(int(values[3][2:]))
    elif line.startswith("Button B"):
        values = line.strip().split(' ')
        x_B_changes.append(int(values[2][2:-1]))
        y_B_changes.append(int(values[3][2:]))
    elif line.startswith("Prize:"):
        values = line.strip().split(' ')
        x_prizes.append(int(values[1][2:-1]))
        y_prizes.append(int(values[2][2:]))

print(find_fewest_tokens(x_A_changes, x_B_changes, y_A_changes, y_B_changes, x_prizes, y_prizes))
print(find_fewest_tokens_2(x_A_changes, x_B_changes, y_A_changes, y_B_changes, x_prizes, y_prizes))
