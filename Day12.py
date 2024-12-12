import sys


class Region:
    def __init__(self, mark, square):
        self.mark = mark
        self.square = square
        self.coordinates = set()
        self.perimeter = 0
        self.sides = 0

    def unite(self, other):
        if self.mark != other.mark:
            raise Exception("Expected " + self.mark + " but found " + other.mark + " mark")
        self.square += other.square
        self.coordinates = self.coordinates.union(other.coordinates)
        self.perimeter += other.perimeter
        self.sides += other.sides
        return self


def count_total_fence_price(field):
    coordinate_to_region = {}
    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            this_region = Region(field[i][j], 1)
            this_region.coordinates.add((i, j))
            if j > 0:
                if field[i][j - 1] == field[i][j]:
                    region = coordinate_to_region[(i, j - 1)]
                    this_region = region.unite(this_region)
                else:
                    this_region.perimeter += 1
            else:
                this_region.perimeter += 1
            if i > 0:
                if field[i - 1][j] == field[i][j]:
                    region = coordinate_to_region[(i - 1, j)]
                    if this_region != region:
                        this_region = region.unite(this_region)
                        for (x, y) in region.coordinates:
                            if (x, y) in coordinate_to_region:
                                coordinate_to_region[(x, y)] = this_region
                else:
                    this_region.perimeter += 1
            else:
                this_region.perimeter += 1
            if j < len(field[i]) - 1:
                if field[i][j + 1] != field[i][j]:
                    this_region.perimeter += 1
            else:
                this_region.perimeter += 1

            if i < len(field) - 1:
                if field[i + 1][j] != field[i][j]:
                    this_region.perimeter += 1
            else:
                this_region.perimeter += 1
            coordinate_to_region[(i, j)] = this_region
            j += 1
        i += 1
    result_sum = 0
    for region in set(coordinate_to_region.values()):
        result_sum += region.perimeter * region.square
    return result_sum


def count_total_fence_price_2(field):
    coordinate_to_region = {}
    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            this_region = Region(field[i][j], 1)
            this_region.coordinates.add((i, j))

            # uniting with top or left regions (which should already be at least partially processed)
            if j > 0:
                if field[i][j - 1] == field[i][j]:
                    region = coordinate_to_region[(i, j - 1)]
                    this_region = region.unite(this_region)
            if i > 0:
                if field[i - 1][j] == field[i][j]:
                    region = coordinate_to_region[(i - 1, j)]
                    if this_region != region:
                        this_region = region.unite(this_region)
                        for (x, y) in region.coordinates:
                            if (x, y) in coordinate_to_region:
                                coordinate_to_region[(x, y)] = this_region

            # updating sides changes with this particular
            # top side
            if i == 0 or field[i - 1][j] != field[i][j]:
                if j == 0 or field[i][j - 1] != field[i][j]:
                    this_region.sides += 1
                elif j > 0 and i > 0 and field[i - 1][j - 1] == field[i][j]:
                    this_region.sides += 1
            # left side
            if j == 0 or field[i][j - 1] != field[i][j]:
                if i == 0 or field[i - 1][j] != field[i][j]:
                    this_region.sides += 1
                elif i > 0 and j > 0 and field[i - 1][j - 1] == field[i][j]:
                    this_region.sides += 1
            # bottom side
            if i == len(field) - 1 or field[i + 1][j] != field[i][j]:
                if j == 0 or field[i][j - 1] != field[i][j]:
                    this_region.sides += 1
                elif j > 0 and i < len(field) - 1 and field[i + 1][j - 1] == field[i][j]:
                    this_region.sides += 1
            # right side
            if j == len(field[i]) - 1 or field[i][j + 1] != field[i][j]:
                if i == 0 or field[i - 1][j] != field[i][j]:
                    this_region.sides += 1
                elif i > 0 and j < len(field[i]) - 1 and field[i - 1][j + 1] == field[i][j]:
                    this_region.sides += 1

            coordinate_to_region[(i, j)] = this_region
            j += 1
        i += 1
    result_sum = 0
    for region in set(coordinate_to_region.values()):
        result_sum += region.sides * region.square
    return result_sum


test_map_1 = [
    "AAAA",
    "BBCD",
    "BBCC",
    "EEEC"
]

test_map_2 = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE"
]

assert count_total_fence_price(test_map_1) == 140
assert count_total_fence_price(test_map_2) == 1930

assert count_total_fence_price_2(test_map_1) == 80
assert count_total_fence_price_2(test_map_2) == 1206

field_map = []
for line in sys.stdin:
    field_map.append(line.strip())

print(count_total_fence_price(field_map))
print(count_total_fence_price_2(field_map))
