e = '''
AAAA
BBCD
BBCC
EEEC
'''
# 140

e2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""
# 772

e3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
# 1930

with open("12.txt", "r") as f:
    q = f.read()

import numpy as np

def split_zones(x: str):
    x = 0

def get_uniques(x: str) -> set:
    ret_dict = dict()
    for line in x.strip().splitlines():
        listed = list(line)
        uniques, counts = np.unique(np.array(listed), return_counts=True)
        for unique, count in zip(uniques, counts):
            if unique not in ret_dict:
                ret_dict[unique] = int(count)
            else:
                ret_dict[unique] += int(count)

    return ret_dict


def get_perimeter(
    x: list[list],
    row: int,
    col: int,
    num_row: int,
    num_col: int,
    seen: set,
) -> int:
    perimeter = 0
    area = 1

    if (row, col) in seen:
        return 0, 0

    seen.add((row, col))
    curr_cell = x[row][col]

    for adj_row, adj_col in (
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ):
        if (0 <= adj_row < num_row) and (0 <= adj_col < num_col):
            if (x[adj_row][adj_col] == curr_cell):
                p, a = get_perimeter(
                    x, adj_row, adj_col, num_row, num_col, seen
                )
                perimeter += p
                area += a
            else:
                perimeter += 1
        else:
            perimeter += 1

    return perimeter, area


def get_perimeters(x: str, areas: dict[str, int]):
    seen = set()
    x = x.strip().splitlines()
    x = [list(line) for line in x]

    perimeters = {key: [] for key in areas.keys()}

    num_row = len(x)
    num_col = len(x[0])
    for row in range(num_row):
        for col in range(num_col):
            if (row, col) not in seen:
                perimeter, area = get_perimeter(x, row, col, num_row, num_col, seen)
                curr_cell = x[row][col]
                perimeters[curr_cell].append((perimeter, area))

    return perimeters


def f(x: str):
    uniques = get_uniques(x)
    perimeters = get_perimeters(x, uniques)
    price = 0

    print(perimeters)
    for perimeter_list in perimeters.values():
        for perimeter, area in perimeter_list:
            price += area * perimeter

    return price

print(f(e))
print(f(e2))
print(f(e3))
