import sys


def count_xmas(input):
    number_of_xmas = 0
    i = 0
    while i < len(input):
        j = 0
        while j < len(input[0]):
            if input[i][j] == 'X':
                top_available = i - 3 >= 0
                right_available = j + 3 < len(input[0])
                bottom_available = i + 3 < len(input)
                left_available = j - 3 >= 0
                if top_available:
                    if left_available:
                        if input[i - 1][j - 1] == 'M' and input[i - 2][j - 2] == 'A' and input[i - 3][j - 3] == 'S':
                            number_of_xmas += 1
                    if right_available:
                        if input[i - 1][j + 1] == 'M' and input[i - 2][j + 2] == 'A' and input[i - 3][j + 3] == 'S':
                            number_of_xmas += 1
                    if input[i - 1][j] == 'M' and input[i - 2][j] == 'A' and input[i - 3][j] == 'S':
                        number_of_xmas += 1
                if right_available:
                    if input[i][j + 1] == 'M' and input[i][j + 2] == 'A' and input[i][j + 3] == 'S':
                        number_of_xmas += 1
                if bottom_available:
                    if left_available:
                        if input[i + 1][j - 1] == 'M' and input[i + 2][j - 2] == 'A' and input[i + 3][j - 3] == 'S':
                            number_of_xmas += 1
                    if right_available:
                        if input[i + 1][j + 1] == 'M' and input[i + 2][j + 2] == 'A' and input[i + 3][j + 3] == 'S':
                            number_of_xmas += 1
                    if input[i + 1][j] == 'M' and input[i + 2][j] == 'A' and input[i + 3][j] == 'S':
                        number_of_xmas += 1
                if left_available:
                    if input[i][j - 1] == 'M' and input[i][j - 2] == 'A' and input[i][j - 3] == 'S':
                        number_of_xmas += 1
            j += 1
        i += 1
    return number_of_xmas


def count_x_mas(input):
    number_of_x_mas = 0
    i = 1
    while i < len(input) - 1:
        j = 1
        while j < len(input[0]) - 1:
            if input[i][j] == 'A':
                if ((input[i - 1][j - 1] == 'M' and input[i + 1][j + 1] == 'S') or
                        (input[i - 1][j - 1] == 'S' and input[i + 1][j + 1] == 'M')):
                    if ((input[i - 1][j + 1] == 'M' and input[i + 1][j - 1] == 'S') or
                        (input[i - 1][j + 1] == 'S' and input[i + 1][j - 1] == 'M')):
                        number_of_x_mas += 1
            j += 1
        i += 1
    return number_of_x_mas


assert count_xmas(
    ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA",
     "MAMMMXMMMM", "MXMXAXMASX"]) == 18
assert count_x_mas(
    ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM", "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA",
     "MAMMMXMMMM", "MXMXAXMASX"]) == 9

s = []
for line in sys.stdin:
    s.append(line)
print(count_xmas(s))
print(count_x_mas(s))
