import sys


def find_length_of_shortest_path(falling_list, field_size):
    fallings_set = set(falling_list)
    visited = set()
    visited.add((0, 0))
    current = {(0, 0)}
    i = 0
    while len(current) > 0:
        next = set()
        for step in current:
            x = step[0] - 1
            y = step[1]
            if x >= 0:
                if (x, y) not in fallings_set and (x, y) not in visited:
                    next.add((x, y))
                    visited.add((x, y))
            x = step[0] + 1
            y = step[1]
            if x < field_size:
                if (x, y) not in fallings_set and (x, y) not in visited:
                    next.add((x, y))
                    visited.add((x, y))
            if x == field_size - 1 and y == field_size - 1:
                return i + 1
            x = step[0]
            y = step[1] - 1
            if y >= 0:
                if (x, y) not in fallings_set and (x, y) not in visited:
                    next.add((x, y))
                    visited.add((x, y))
            x = step[0]
            y = step[1] + 1
            if y < field_size:
                if (x, y) not in fallings_set and (x, y) not in visited:
                    next.add((x, y))
                    visited.add((x, y))
            if x == field_size - 1 and y == field_size - 1:
                return i + 1
        i += 1
        current = next
    return 0

test_fallings = [
    (5,4),
    (4,2),
    (4,5),
    (3,0),
    (2,1),
    (6,3),
    (2,4),
    (1,5),
    (0,6),
    (3,3),
    (2,6),
    (5,1),
    (1,2),
    (5,5),
    (2,5),
    (6,5),
    (1,4),
    (0,4),
    (6,4),
    (1,1),
    (6,1),
    (1,0),
    (0,5),
    (1,6),
    (2,0)
]

assert find_length_of_shortest_path(test_fallings[:12], 7) == 22

fallings = []
for line in sys.stdin:
    tmp = line.strip().split(",")
    fallings.append((int(tmp[0]), int(tmp[1])))

print(find_length_of_shortest_path(fallings[:1024], 71))
for i in range(1024, len(fallings)):
    if find_length_of_shortest_path(fallings[:i], 71) == 0:
        print(fallings[i-1])
        break
