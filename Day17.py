import sys


def find_output(a_register, b_register, c_register, programm):
    a = a_register
    b = b_register
    c = c_register
    programm_codes = programm.copy()
    i = 0
    out = []
    while i < len(programm_codes):
        if programm_codes[i] == 0:  # adb
            a = int(a / (2 ** get_combo_operand(a, b, c, programm_codes, i + 1)))
        elif programm_codes[i] == 1:  # bxl
            b = b ^ programm_codes[i + 1]
        elif programm_codes[i] == 2:  # bst
            b = get_combo_operand(a, b, c, programm_codes, i + 1) % 8
        elif programm_codes[i] == 3:  # jnz
            if a != 0:
                i = programm_codes[i + 1]
                continue
        elif programm_codes[i] == 4:  # bxc
            b = b ^ c
        elif programm_codes[i] == 5:  # out
            out.append(get_combo_operand(a, b, c, programm_codes, i + 1) % 8)
        elif programm_codes[i] == 6:  # bdv
            b = int(a / (2 ** get_combo_operand(a, b, c, programm_codes, i + 1)))
        elif programm_codes[i] == 7:  # cdv
            c = int(a / (2 ** get_combo_operand(a, b, c, programm_codes, i + 1)))
        i += 2
    return out


def get_combo_operand(a_register, b_register, c_register, programm, i):
    if programm[i] <= 3:
        return programm[i]
    elif programm[i] == 4:
        return a_register
    elif programm[i] == 5:
        return b_register
    elif programm[i] == 6:
        return c_register
    else:
        raise Exception("7 operand!")


def find_a_for_input(program):
    good = [[], [0, 1, 2, 4, 5, 6, 7], set(range(64))]
    for i in range(2, len(program) + 1):
        new_good = set()
        for j in range(8):
            for good_one in good[i]:
                a = good_one + (j << i * 3)
                output = find_output_with_output_limit(a, 0, 0, program, i)
                if output[:i - 2] == program[:i - 2]:
                    new_good.add(a)
        if len(new_good) == 0:
            return
        good.append(new_good)
    right = []
    for num in good[len(good) - 1]:
        if find_output(num, 0, 0, program) == program:
            right.append(num)

    return min(right)


def find_output_with_output_limit(a_register, b_register, c_register, program, output_length_limit):
    a = a_register
    b = b_register
    c = c_register
    program_codes = program.copy()
    i = 0
    out = []
    while i < len(program_codes) and len(out) < output_length_limit:
        if program_codes[i] == 0:  # adb
            a = int(a / (2 ** get_combo_operand(a, b, c, program_codes, i + 1)))
        elif program_codes[i] == 1:  # bxl
            b = b ^ program_codes[i + 1]
        elif program_codes[i] == 2:  # bst
            b = get_combo_operand(a, b, c, program_codes, i + 1) % 8
        elif program_codes[i] == 3:  # jnz
            if a != 0:
                i = program_codes[i + 1]
                continue
        elif program_codes[i] == 4:  # bxc
            b = b ^ c
        elif program_codes[i] == 5:  # out
            out.append(get_combo_operand(a, b, c, program_codes, i + 1) % 8)
        elif program_codes[i] == 6:  # bdv
            b = int(a / (2 ** get_combo_operand(a, b, c, program_codes, i + 1)))
        elif program_codes[i] == 7:  # cdv
            c = int(a / (2 ** get_combo_operand(a, b, c, program_codes, i + 1)))
        i += 2
    return out


test_a = 729
test_b = 0
test_c = 0
test_program = [0, 1, 5, 4, 3, 0]
assert find_output(test_a, test_b, test_c, test_program) == [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]

a = 0
b = 0
c = 0
program = []
for line in sys.stdin:
    if line.startswith("Register A:"):
        a = int(line.strip().split(" ")[2])
    elif line.startswith("Register B:"):
        b = int(line.strip().split(" ")[2])
    elif line.startswith("Register C:"):
        c = int(line.strip().split(" ")[2])
    elif line.startswith("Program:"):
        program = list(map(int, (line.strip().split(" ")[1]).split(",")))

print(*find_output(a, b, c, program), sep=',')
print(find_a_for_input(program))
