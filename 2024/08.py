e = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

with open("08.txt", "r") as f:
    q = f.read()

from pprint import pprint
import copy
import re
import math
import time


def get_legend(x: str):
    legend = dict()
    for row, line in enumerate(x):
        for col, symbol in enumerate(line):
            if symbol != ".":
                if symbol not in legend:
                    legend[symbol] = list()
                legend[symbol].append((row, col))

    return legend


def get_lin(coord1, coord2, in_area):
    row1, col1 = coord1
    row2, col2 = coord2

    row_diff = row2 - row1
    col_diff = col2 - col1

    lins = [coord1, coord2]

    factor = 1
    while in_area((new_coord := (row1 - row_diff * factor, col1 - col_diff * factor))):
        lins.append(new_coord)
        factor += 1

    factor = 1
    while in_area((new_coord := (row2 + row_diff * factor, col2 + col_diff * factor))):
        lins.append(new_coord)
        factor += 1

    return lins


def get_coord_for_individual(coords, in_area):
    ret = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            lins = get_lin(coords[i], coords[j], in_area)
            # print("\t", pos1, pos2)
            for pos in lins:
                if in_area(pos):
                    ret.append(pos)

    return ret


def get_coords(legend: dict, in_area):
    antinodes = set()
    for key, coords in legend.items():
        # print(f"Getting coord for {key}")
        antinodes_particular = get_coord_for_individual(coords, in_area)
        antinodes = antinodes.union(antinodes_particular)
        # print(f"coord: {coords}, antinodes: {antinodes_particular}")

    return antinodes


def f(x: str):
    x = x.strip().splitlines()

    def in_area(coord):
        row, col = coord
        return 0 <= row < len(x) and 0 <= col < len(x[0])

    legend = get_legend(x)
    pprint(legend)
    coords = get_coords(legend, in_area)

    return len(coords)

print(f(e))
start = time.time()
print(f(q))
duration = time.time() - start
print(f"Duration: {duration} s")

# Answer:
# 295