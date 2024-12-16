e = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

with open("14.txt", "r") as f:
    q = f.read()

from pprint import pprint
import numpy as np
import copy
import re
import math

def parse_line(x: str) -> tuple[tuple]:
    p, v = x.split(" ")
    p, v = p.split("=")[1], v.split("=")[1]
    p = p.split(",")
    v = v.split(",")
    return (int(p[1]), int(p[0])), (int(v[1]), int(v[0]))


def f(x: str, rows: int, cols: int, seconds: int):
    x = x.strip().splitlines()
    final_locs = []

    for line in x:
        p, v = parse_line(line)
        final_locs.append(((p[0] + v[0] * seconds) % rows, (p[1] + v[1] * seconds) % cols))

    quads = [0] * 4
    half_row = rows // 2
    half_col = cols // 2
    # print(half_row, half_col)
    for pos in final_locs:
        row, col = pos
        if row < half_row and col < half_col:
            quads[0] += 1
        elif row > half_row and col < half_col:
            quads[1] += 1
        elif row < half_row and col > half_col:
            quads[2] += 1
        elif row > half_row and col > half_col:
            quads[3] += 1

    # print(sorted(final_locs))
    # print(quads)
    prod = 1
    for quad in quads:
        prod *= quad

    return prod

# print(f(e, 7, 11, 1))
print(f(e, 7, 11, 100))
print(f(q, 103, 101, 100))

# Part 1