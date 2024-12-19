import sys


def count_possible(towels, designs):
    result = 0
    for design in designs:
        if is_design_possible(towels, design):
            result += 1
    return result


def is_design_possible(towels, design):
    current_parts = {design}
    while len(current_parts) > 0:
        next_parts = set()
        for design_part in current_parts:
            for towel in towels:
                if design_part.startswith(towel):
                    next_parts.add(design_part[len(towel):])
                    if len(design_part) == len(towel):
                        return True
        current_parts = next_parts
    return False


def count_all_possible_ways_to_make_designs(towels, designs):
    result = 0
    cache = {}
    for design in designs:
        result += count_all_ways_to_make_design(towels, design, cache)
    return result


def count_all_ways_to_make_design(towels, design, cache_for_towel_search):
    if len(design) == 0:
        return 1
    result = 0
    if design in cache_for_towel_search:
        return cache_for_towel_search[design]
    else:
        for towel in towels:
            if design.startswith(towel):
                result += count_all_ways_to_make_design(towels, design[len(towel):], cache_for_towel_search)
    cache_for_towel_search[design] = result
    return result


test_towels = ['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br']
test_designs = [
    'brwrr',
    'bggr',
    'gbbr',
    'rrbgbr',
    'ubwu',
    'bwurrg',
    'brgr',
    'bbrgwb'
]

assert count_possible(test_towels, test_designs) == 6
assert count_all_possible_ways_to_make_designs(test_towels, test_designs) == 16

towels = input().strip().split(", ")
designs = []
input()
for line in sys.stdin:
    designs.append(line.strip())

print(count_possible(towels, designs))
print(count_all_possible_ways_to_make_designs(towels, designs))
