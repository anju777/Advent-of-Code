from copy import deepcopy
import re
import os
from enum import StrEnum, auto
from pprint import pprint

with open("6.txt", "r") as f:
    q = f.read()

e = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

class Direction(StrEnum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()

    def __repr__(self) -> str:
        match self:
            case Direction.UP: return "'^'"
            case Direction.DOWN: return "'v'"
            case Direction.RIGHT: return "'>'"
            case Direction.LEFT: return "'<'"


def find_guard(m: list[list], replace: bool = True) -> None:
    for row, l in enumerate(m):
        if "^" in l:
            col = l.index("^")
            if replace:
                l[col] = "_"
            return (row, col), Direction.UP


def get_in_area_fn(m):
    map_height = len(m)
    map_width = len(m[0])

    def in_area(curr_loc) -> bool:
        h, w = curr_loc[0], curr_loc[1]
        return 0 <= h < map_height and 0 <= w < map_width

    return in_area


def turn(dir):
    match dir:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP
        case Direction.RIGHT:
            return Direction.DOWN


def step(m, curr_loc, dir, in_area) -> None:
    h, w = curr_loc
    if dir == Direction.UP:
        next_loc = (h - 1, w)
    elif dir == Direction.DOWN:
        next_loc = (h + 1, w)
    elif dir == Direction.RIGHT:
        next_loc = (h, w + 1)
    elif dir == Direction.LEFT:
        next_loc = (h, w - 1)

    if not in_area(next_loc):
        return next_loc, dir
    elif "#" == m[next_loc[0]][next_loc[1]]:
        return curr_loc, turn(dir)
    else:
        m[next_loc[0]][next_loc[1]] = "_"
        return next_loc, dir


def step_loop(m, curr_loc, dir, in_area) -> None:
    h, w = curr_loc
    if dir == Direction.UP:
        next_loc = (h - 1, w)
    elif dir == Direction.DOWN:
        next_loc = (h + 1, w)
    elif dir == Direction.RIGHT:
        next_loc = (h, w + 1)
    elif dir == Direction.LEFT:
        next_loc = (h, w - 1)

    just_placed = False
    if not in_area(next_loc):
        return next_loc, dir, just_placed
    elif "#" == m[next_loc[0]][next_loc[1]]:
        return curr_loc, turn(dir), just_placed
    else:
        if m[next_loc[0]][next_loc[1]] != dir:
            just_placed = True
            m[next_loc[0]][next_loc[1]] = dir
        return next_loc, dir, just_placed


def walk_loop(m: list[list]) -> None:
    curr_loc, dir = find_guard(m)

    in_area = get_in_area_fn(m)

    while in_area(curr_loc):
        curr_loc, dir, just_placed = step_loop(m, curr_loc, dir, in_area)
        # pprint(m)
        # print(curr_loc, dir, just_placed)
        if not just_placed and in_area(curr_loc) and m[curr_loc[0]][curr_loc[1]] == dir:
            return True

    return False


def walk(m: list[list]) -> None:
    curr_loc, dir = find_guard(m)

    in_area = get_in_area_fn(m)

    while in_area(curr_loc):
        curr_loc, dir = step(m, curr_loc, dir, in_area)


def count_step(m: list):
    count = 0
    for line in m:
        count += line.count("_")
    return count


def get_step_loc(m: list[list], security_guard_pos, include_security_guard: bool = False):
    # TESTED
    possible_locs = set()

    for row, line in enumerate(m):
        start = 0
        while "_" in line[start:]:
            col = line[start:].index("_")
            possible_locs.add((row, col + start))
            start += col + 1

    if not include_security_guard:
        possible_locs.remove(security_guard_pos)

    return possible_locs


def f(x: str):
    x = x.strip()
    security_guard_map = list(map(list, x.splitlines()))

    walk(security_guard_map)
    count_steps = count_step(security_guard_map)

    return count_steps

# print(f(e))
# print(f(q))

# Part 1:
# 5242


def creates_loop(m: list[list], obstruction) -> bool:
    m_copy = deepcopy(m)
    m_copy[obstruction[0]][obstruction[1]] = "#"
    looped = walk_loop(m_copy)
    # pprint(m_copy)
    return looped


def f2(x: str) -> int:
    x = x.strip()
    security_guard_map = list(map(list, x.splitlines()))
    orig_security_guard_map = deepcopy(security_guard_map)
    guard_loc, _ = find_guard(security_guard_map, replace=False)

    walk(security_guard_map)
    possible_obstruction_locs = get_step_loc(security_guard_map, guard_loc)

    num_obstructions = 0
    for obstruction in possible_obstruction_locs:
        if creates_loop(orig_security_guard_map, obstruction):
            num_obstructions += 1

    return num_obstructions

print(f2(e))
print(f2(q))

# Part 2
# 1424 (but takes ~1 min to run)
