e = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

ex = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

with open("15.txt", "r") as f:
    q = f.read()


import pprint
import numpy as np
import copy
import re
import math

def find_symbol(m: list[list], symbol, find_all: bool = False) -> tuple[int, int]:
    positions = []
    for i, line in enumerate(m):
        if symbol in line:
            pos = (i, line.index(symbol))
            if not find_all:
                return pos
            positions.append(pos)

            abb_line = line[pos[1] + 1:]
            while symbol in abb_line:
                pos = (i, abb_line.index(symbol) + pos[1] + 1)
                positions.append(pos)
                # print(line, abb_line, pos, positions)
                abb_line = line[pos[1] + 1:]

    return positions

def get_next_pos(move, fish_pos, step: int = 1) -> tuple[int, int]:
    match move:
        case ">":
            next_pos = (fish_pos[0], fish_pos[1] + step)
        case "<":
            next_pos = (fish_pos[0], fish_pos[1] - step)
        case "v":
            next_pos = (fish_pos[0] + step, fish_pos[1])
        case "^":
            next_pos = (fish_pos[0] - step, fish_pos[1])

    return next_pos


def make_move(m: list[list[str]], fish_pos: tuple[int, int], move: str) -> None:
    """In-place modification of map"""
    next_pos = get_next_pos(move, fish_pos, step=1)
    i = 1
    next_pos_obj = m[next_pos[0]][next_pos[1]]
    # print("move", move, "next position object", next_pos_obj, "fish pos", fish_pos)

    match next_pos_obj:
        case "#":
            return fish_pos
        case ".":
            return next_pos
        case "O":
            # Do a bunch of things...
            init_next_pos = next_pos

            while next_pos_obj == "O":
                i += 1
                next_pos = get_next_pos(move, fish_pos, i)
                next_pos_obj = m[next_pos[0]][next_pos[1]]
                # print(next_pos, next_pos_obj)

            if next_pos_obj == ".":
                # Move fish by one
                m[init_next_pos[0]][init_next_pos[1]] = "."
                m[next_pos[0]][next_pos[1]] = "O"
                return init_next_pos

            elif next_pos_obj == "#":
                return fish_pos
            else:
                raise RuntimeError(f"next_pos_obj: {next_pos_obj} {next_pos}")

def f(x: str):
    init_map, moves = x.strip().split("\n\n")
    init_map = init_map.splitlines()
    init_map = [list(line) for line in init_map]

    moves = moves.replace("\n", "")
    fish_pos = find_symbol(init_map, "@", find_all=False)

    curr_map = copy.deepcopy(init_map)
    curr_map[fish_pos[0]][fish_pos[1]] = "."
    for move in moves:
        fish_pos = make_move(curr_map, fish_pos, move)

    rock_positions = find_symbol(curr_map, "O", find_all=True)
    sum = 0
    for rock in rock_positions:
        sum += 100 * rock[0] + rock[1]

    return sum

print(f(e))
print(f(ex))
print(f(q))
