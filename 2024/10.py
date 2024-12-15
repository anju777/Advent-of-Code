import re, copy, os, traceback, pdb
from pprint import pprint

e = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

p = """
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
"""

PART2 = True

with open("10.txt", "r") as f:
    q = f.read()

def get_possible_coords(x, row, col):
    rows = len(x)
    cols = len(x[0])
    possibles = [
        (row - 1, col),
        (row + 1, col),
        (row, col + 1),
        (row, col - 1)
    ]
    actual_possible = list()
    for (pos_row, pos_col) in possibles:
        if (0 <= pos_row < rows) and (0 <= pos_col < cols):
            actual_possible.append((pos_row, pos_col))
    # print(actual_possible)
    return actual_possible

def find_routes(x, row, col) -> int:
    curr = x[row][col]

    if curr == "9":
        if PART2:
            return 1
        else:
            return {(row, col)}

    next = str(int(curr) + 1)
    reachables = set()
    num_reachables = 0

    for pos_row, pos_col in get_possible_coords(x, row, col):
        if x[pos_row][pos_col] == next:
            num_reachables += find_routes(x, pos_row, pos_col)
            # print("\t" * int(curr) + f"{curr} ({row}, {col}) -> ")

            # reachables = reachables.union(find_routes(x, pos_row, pos_col))

    return num_reachables

def f(x):
    x = x.strip().splitlines()
    for i in range(len(x)):
        # x[i] = list(map(int, x[i]))
        x[i] = list(x[i])

    trailheads = 0
    num_reachables = set()
    for row in range(len(x)):
        for col in range(len(x[row])):
            if x[row][col] == "0":
                new_reachables = find_routes(x, row, col)
                # print(f"trailhead: ({row}, {col}). reachables: {new_reachables}")
                # num_reachables = num_reachables.union(new_reachables)
                trailheads += new_reachables
    # pprint(x)

    return trailheads

print(f(e))
print(f(p))
print(f(q))