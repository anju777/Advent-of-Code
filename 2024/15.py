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

# ex = """
# ########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<
# """
ex = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
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

def check_for_wall(m, move, fish_pos):
    # True if a wall is found. False otherwise

    if m[fish_pos[0]][fish_pos[1]] == "#":
        return True

    match move:
        case ">":
            next_pos = (fish_pos[0], fish_pos[1] + 1)
            if m[next_pos[0]][next_pos[1]] in "[]":
                return check_for_wall(m, move, next_pos)
            elif m[next_pos[0]][next_pos[1]] == "#":
                return True
            elif m[next_pos[0]][next_pos[1]] == ".":
                return False
            else:
                raise RuntimeError("huh")
        case "<":
            next_pos = (fish_pos[0], fish_pos[1] - 1)
            if m[next_pos[0]][next_pos[1]] in "[]":
                return check_for_wall(m, move, next_pos)
            elif m[next_pos[0]][next_pos[1]] == "#":
                return True
            elif m[next_pos[0]][next_pos[1]] == ".":
                return False
            else:
                raise RuntimeError("huh")
        case "v":
            # print(fish_pos)
            next_pos = (fish_pos[0] + 1, fish_pos[1])
            match m[next_pos[0]][next_pos[1]]:
                case "[":
                    return check_for_wall(m, move, next_pos) or check_for_wall(m, move, (next_pos[0], next_pos[1] + 1))
                case "]":
                    return check_for_wall(m, move, next_pos) or check_for_wall(m, move, (next_pos[0], next_pos[1] - 1))
                case "#":
                    return True
                case ".":
                    return False
        case "^":
            next_pos = (fish_pos[0] - 1, fish_pos[1])
            match m[next_pos[0]][next_pos[1]]:
                case "[":
                    return check_for_wall(m, move, next_pos) or check_for_wall(m, move, (next_pos[0], next_pos[1] + 1))
                case "]":
                    return check_for_wall(m, move, next_pos) or check_for_wall(m, move, (next_pos[0], next_pos[1] - 1))
                case "#":
                    return True
                case ".":
                    return False

    return check_for_wall(m, move, next_checks)

def move_objs(m, move, curr_pos, prev_obj):
    match move:
        case ">":
            next_pos = (curr_pos[0], curr_pos[1] + 1)
            next_pos_obj = m[next_pos[0]][next_pos[1]]
            m[next_pos[0]][next_pos[1]] = prev_obj
            if next_pos_obj in "[]":
                move_objs(m, move, next_pos, next_pos_obj)
        case "<":
            next_pos = (curr_pos[0], curr_pos[1] - 1)
            next_pos_obj = m[next_pos[0]][next_pos[1]]
            m[next_pos[0]][next_pos[1]] = prev_obj
            if next_pos_obj in "[]":
                move_objs(m, move, next_pos, next_pos_obj)

        case "v":
            next_pos = (curr_pos[0] + 1, curr_pos[1])
            next_pos_obj = m[next_pos[0]][next_pos[1]]
            init_next_pos_obj = next_pos_obj
            m[next_pos[0]][next_pos[1]] = prev_obj
            if init_next_pos_obj == "[":
                move_objs(m, move, next_pos, next_pos_obj)

                # Move the other thing
                next_pos = (curr_pos[0] + 1, curr_pos[1] + 1)
                next_pos_obj = m[next_pos[0]][next_pos[1]]
                move_objs(m, move, next_pos, next_pos_obj)
                m[next_pos[0]][next_pos[1]] = "."

            elif init_next_pos_obj == "]":
                move_objs(m, move, next_pos, next_pos_obj)

                # Move the other thing
                next_pos = (curr_pos[0] + 1, curr_pos[1] - 1)
                next_pos_obj = m[next_pos[0]][next_pos[1]]
                move_objs(m, move, next_pos, next_pos_obj)
                m[next_pos[0]][next_pos[1]] = "."
        case "^":
            next_pos = (curr_pos[0] - 1, curr_pos[1])
            next_pos_obj = m[next_pos[0]][next_pos[1]]
            init_next_pos_obj = next_pos_obj
            m[next_pos[0]][next_pos[1]] = prev_obj
            if init_next_pos_obj == "[":
                move_objs(m, move, next_pos, next_pos_obj)

                # Move the other thing
                next_pos = (curr_pos[0] - 1, curr_pos[1] + 1)
                next_pos_obj = m[next_pos[0]][next_pos[1]]
                move_objs(m, move, next_pos, next_pos_obj)
                m[next_pos[0]][next_pos[1]] = "."

            elif init_next_pos_obj == "]":
                move_objs(m, move, next_pos, next_pos_obj)

                # Move the other thing
                next_pos = (curr_pos[0] - 1, curr_pos[1] - 1)
                next_pos_obj = m[next_pos[0]][next_pos[1]]
                move_objs(m, move, next_pos, next_pos_obj)
                m[next_pos[0]][next_pos[1]] = "."


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
        case "[" | "]":
            # Do a bunch of things...
            init_next_pos = next_pos
            init_next_pos_obj = next_pos_obj

            wall = check_for_wall(m, move, fish_pos)
            if wall:
                # print("Hit a wall!", move, fish_pos)
                return fish_pos

            else:
                # print(f"\nBefore ({fish_pos} {move}):")
                # for line in m:
                #     print("".join(line))

                # print()
                fish_pos = move_objs(m, move, fish_pos, ".")
                # print("After:")
                # for line in m:
                #     print("".join(line))

                return init_next_pos

def f(x: str):
    init_map, moves = x.strip().split("\n\n")
    init_map = init_map.splitlines()
    for i in range(len(init_map)):
        init_map[i] = init_map[i].replace("#", "##")
        init_map[i] = init_map[i].replace("O", "[]")
        init_map[i] = init_map[i].replace(".", "..")
        init_map[i] = init_map[i].replace("@", "@.")
        init_map[i] = list(init_map[i])
    # for line in init_map: print(line)

    moves = moves.replace("\n", "")
    fish_pos = find_symbol(init_map, "@", find_all=False)

    curr_map = copy.deepcopy(init_map)
    curr_map[fish_pos[0]][fish_pos[1]] = "."
    for move in moves:
        fish_pos = make_move(curr_map, fish_pos, move)

    rock_positions = find_symbol(curr_map, "[", find_all=True)
    # for line in curr_map: print(line)
    sum = 0
    for rock in rock_positions:
        sum += 100 * rock[0] + rock[1]

    return sum

print(f(e))
print(f(ex))
print(f(q))

# Part 1: 1559280

# Part 2: 1576353
