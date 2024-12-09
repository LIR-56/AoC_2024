import sys


def count_antinodes(frequency_map):
    i = 0
    antennas_dict = {}
    while i < len(frequency_map):
        j = 0
        while j < len(frequency_map[i]):
            if frequency_map[i][j] != '.':
                c = frequency_map[i][j]
                if c not in antennas_dict:
                    antennas_dict[c] = []
                antennas_dict[c].append((i, j))
            j += 1
        i += 1

    antinodes = set()
    for (k, v) in antennas_dict.items():
        i = 0
        while i < len(v):
            j = i + 1
            while j < len(v):
                first = v[i]
                second = v[j]
                x_diff = first[0] - second[0]
                y_diff = first[1] - second[1]

                antinodes.add((first[0] + x_diff, first[1] + y_diff))
                antinodes.add((second[0] - x_diff, second[1] - y_diff))

                j += 1
            i += 1
    antinodes_filtered = set()
    for antinode in antinodes:
        if not (antinode[0] < 0 or antinode[0] >= len(frequency_map)) and\
            not (antinode[1] < 0 or antinode[1] >= len(frequency_map[0])):
                antinodes_filtered.add(antinode)

    return len(antinodes_filtered)

def count_antinodes_2(frequency_map):
    i = 0
    antennas_dict = {}
    while i < len(frequency_map):
        j = 0
        while j < len(frequency_map[i]):
            if frequency_map[i][j] != '.':
                c = frequency_map[i][j]
                if c not in antennas_dict:
                    antennas_dict[c] = []
                antennas_dict[c].append((i, j))
            j += 1
        i += 1

    antinodes = set()
    for (k, v) in antennas_dict.items():
        i = 0
        while i < len(v):
            j = i + 1
            while j < len(v):
                first = v[i]
                second = v[j]
                x_diff = first[0] - second[0]
                y_diff = first[1] - second[1]

                new_x = first[0] + x_diff
                new_y = first[1] + y_diff
                while not (new_x < 0 or new_x >= len(frequency_map)) and\
                    not (new_y < 0 or new_y >= len(frequency_map[0])):
                    antinodes.add((new_x, new_y))
                    new_x += x_diff
                    new_y += y_diff

                new_x = second[0] - x_diff
                new_y = second[1] - y_diff
                while not (new_x < 0 or new_x >= len(frequency_map)) and \
                        not (new_y < 0 or new_y >= len(frequency_map[0])):
                    antinodes.add((new_x, new_y))
                    new_x -= x_diff
                    new_y -= y_diff
                antinodes.add(first)
                antinodes.add(second)
                j += 1
            i += 1
    return len(antinodes)



test_frequency_map = [
"............",
"........0...",
".....0......",
".......0....",
"....0.......",
"......A.....",
"............",
"............",
"........A...",
".........A..",
"............",
"............"
]
assert count_antinodes(test_frequency_map) == 14
assert count_antinodes_2(test_frequency_map) == 34

frequency_map = []
for line in sys.stdin:
    frequency_map.append(line.strip())

print(count_antinodes(frequency_map))
print(count_antinodes_2(frequency_map))