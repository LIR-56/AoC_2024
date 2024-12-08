import sys


def total_calibration_result(test_values, numbers):
    tcr = 0
    i = 0
    while i < len(test_values):
        if test_result(test_values[i], 0, numbers[i]) > 0:
            tcr += test_values[i]
        i += 1
    return tcr


def test_result(number, acc, numbers_to_process):
    if len(numbers_to_process) == 0:
        return number == acc
    else:
        return test_result(number, acc * numbers_to_process[0], numbers_to_process[1:]) or \
            test_result(number, acc + numbers_to_process[0], numbers_to_process[1:])


def total_calibration_result_2(test_values, numbers):
    tcr = 0
    i = 0
    while i < len(test_values):
        if test_result_2(test_values[i], 0, numbers[i]) > 0:
            tcr += test_values[i]
        i += 1
    return tcr


def test_result_2(number, acc, numbers_to_process):
    if len(numbers_to_process) == 0:
        return number == acc
    else:

        return test_result_2(number, acc * numbers_to_process[0], numbers_to_process[1:]) or \
            test_result_2(number, acc + numbers_to_process[0], numbers_to_process[1:]) or \
            test_result_2(number, int(str(acc) + str(numbers_to_process[0])), numbers_to_process[1:])


values_for_test = [190, 3267, 83, 156, 7290, 161011, 192, 21037, 292]
numbers_for_test = [
    [10, 19],
    [81, 40, 27],
    [17, 5],
    [15, 6],
    [6, 8, 6, 15],
    [16, 10, 13],
    [17, 8, 14],
    [9, 7, 18, 13],
    [11, 6, 16, 20],
]
assert total_calibration_result(values_for_test, numbers_for_test) == 3749
assert total_calibration_result_2(values_for_test, numbers_for_test) == 11387

test_values = []
numbers = []
for line in sys.stdin:
    r = line.split(':')
    test_values.append(int(r[0]))
    numbers.append(list(map(int, r[1].strip().split(' '))))

print(total_calibration_result(test_values, numbers))
print(total_calibration_result_2(test_values, numbers))
