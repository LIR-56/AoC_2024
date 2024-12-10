import sys


def sum_of_scores_of_trailheads(topographic_map):
    i = 0
    result = 0
    while i < len(topographic_map):
        j = 0
        while j < len(topographic_map[i]):
            if topographic_map[i][j] == '0':
                result += count_score(topographic_map, (i, j))
            j += 1
        i += 1
    return result


def count_score(topographic_map, trailhead):
    current_positions = set()
    next_positions = set()
    num = 0
    current_positions.add(trailhead)
    while num < 9:
        num += 1
        for pos in current_positions:
            if pos[0] > 0 and int(topographic_map[pos[0] - 1][pos[1]]) == num:
                next_positions.add((pos[0] - 1, pos[1]))
            if pos[0] < len(topographic_map) - 1 and int(topographic_map[pos[0] + 1][pos[1]]) == num:
                next_positions.add((pos[0] + 1, pos[1]))
            if pos[1] > 0 and int(topographic_map[pos[0]][pos[1] - 1]) == num:
                next_positions.add((pos[0], pos[1] - 1))
            if pos[1] < len(topographic_map[pos[0]]) - 1 and int(topographic_map[pos[0]][pos[1] + 1]) == num:
                next_positions.add((pos[0], pos[1] + 1))
        current_positions = next_positions
        next_positions = set()
    return len(current_positions)

def sum_of_scores_of_trailheads_v2(topographic_map):
    i = 0
    result = 0
    while i < len(topographic_map):
        j = 0
        while j < len(topographic_map[i]):
            if topographic_map[i][j] == '0':
                result += count_score_based_on_distinct_hiking_trails(topographic_map, (i, j))
            j += 1
        i += 1
    return result


def count_score_based_on_distinct_hiking_trails(topographic_map, trailhead):
    current_positions = [] #the only difference - use lists instead of set
    next_positions = []
    num = 0
    current_positions.append(trailhead)
    while num < 9:
        num += 1
        for pos in current_positions:
            if pos[0] > 0 and int(topographic_map[pos[0] - 1][pos[1]]) == num:
                next_positions.append((pos[0] - 1, pos[1]))
            if pos[0] < len(topographic_map) - 1 and int(topographic_map[pos[0] + 1][pos[1]]) == num:
                next_positions.append((pos[0] + 1, pos[1]))
            if pos[1] > 0 and int(topographic_map[pos[0]][pos[1] - 1]) == num:
                next_positions.append((pos[0], pos[1] - 1))
            if pos[1] < len(topographic_map[pos[0]]) - 1 and int(topographic_map[pos[0]][pos[1] + 1]) == num:
                next_positions.append((pos[0], pos[1] + 1))
        current_positions = next_positions
        next_positions = []
    return len(current_positions)


test_map = [
    "89010123",
    "78121874",
    "87430965",
    "96549874",
    "45678903",
    "32019012",
    "01329801",
    "10456732"
]
assert sum_of_scores_of_trailheads(test_map) == 36
assert sum_of_scores_of_trailheads_v2(test_map) == 81

topographic_map = []
for line in sys.stdin:
    topographic_map.append(line.strip())
print(sum_of_scores_of_trailheads(topographic_map))
print(sum_of_scores_of_trailheads_v2(topographic_map))
