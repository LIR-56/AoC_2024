import sys


def add_all_multiplications(string):
    return add_multiplications(string, True)


def add_multiplications(string, always_enabled=False):
    result = 0
    i = 0
    j = 0
    state = 0  # 0,1,2,3, - mul(; 4, 5 - first number, other numbers; 6 - ','; 7 - second number;
    # 9,10,11,12,13 - don't; 14, 15 -'(' for disabling and enabling;
    disabled = False
    for ch in string:
        if ch == 'm':
            state = 1
            i = 0
            j = 0
        elif ch == 'u':
            if state == 1:
                state = 2
            else:
                state = 0
                i = 0
                j = 0
        elif ch == 'l':
            if state == 2:
                state = 3
            else:
                state = 0
                i = 0
                j = 0
        elif ch == "(":
            if state == 3:
                state = 4
            elif state == 10:
                state = 15
            elif state == 13:
                state = 14
            else:
                state = 0
                i = 0
                j = 0
        elif ch.isnumeric():
            if state == 4:
                i += int(ch)
                state = 5
            elif state == 5:
                i *= 10
                i += int(ch)
            elif state == 6:
                j *= 10
                j += int(ch)
                state = 7
            elif state == 7:
                j *= 10
                j += int(ch)
            else:
                state = 0
                i = 0
                j = 0
        elif ch == ',':
            if state == 5:
                state = 6
            else:
                i = 0
                j = 0
                state = 0
        elif ch == ')':
            if state == 7:
                if not disabled:
                    result += i * j
                state = 0
                i = 0
                j = 0
            elif state == 14:
                if not always_enabled:
                    disabled = True
                state = 0
            elif state == 15:
                disabled = False
                state = 0
            else:
                state = 0
                i = 0
                j = 0
        elif ch == 'd':
            state = 9
            i = 0
            j = 0
        elif ch == 'o':
            if state == 9:
                state = 10
            else:
                i = 0
                j = 0
                state = 0
        elif ch == 'n':
            if state == 10:
                state = 11
                i = 0
                j = 0
            else:
                i = 0
                j = 0
                state = 0
        elif ch == '\'':
            if state == 11:
                state = 12
            else:
                i = 0
                j = 0
                state = 0
        elif ch == "t":
            if state == 12:
                state = 13
            else:
                i = 0
                j = 0
                state = 0
        else:
            state = 0
            i = 0
            j = 0
    return result


assert add_all_multiplications("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))") == 161
assert add_multiplications("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48

s = ""
for line in sys.stdin:
    s += line
print(add_all_multiplications(s))
print(add_multiplications(s))
