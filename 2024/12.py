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
    perimeters: dict[str, list[int]]
) -> set[tuple[int, int]]


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
                seen = get_perimeter(x, row, col, num_row, num_col, seen, perimeters)

    return perimeters


def f(x: str):
    areas = get_uniques(x)
    perimeters = get_perimeters(x, areas)
    price = 0

    for area, perimeter_list in zip(areas, perimeters):
        for perimeter in perimeter_list:
            price += area * p

    return price

print(f(e))
print(f(e2))
print(f(e3))
