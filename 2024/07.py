import re, os, time
from enum import Enum, StrEnum
from copy import copy


PART2 = True


with open("07.txt", "r") as f:
    q = f.read()


e = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def parse_line(line: str) -> tuple[int, list[int]]:
    sum, num_str = line.split(":")
    nums = num_str.strip().split(" ")
    return int(sum), list(map(int, nums))


def can_be_equation(sum: int, nums: list[int], with_opt: bool) -> bool:
    if len(nums) == 1:
        return sum == nums[0]
    if with_opt and nums[0] > sum:
        return False

    else:
        copied_nums_mult = copy(nums)
        copied_nums_add = copy(nums)
        copied_nums_add = [nums[0] + nums[1]] + nums[2:]
        copied_nums_mult = [nums[0] * nums[1]] + nums[2:]

        ########## PART 2 ADDITION -- START ##########
        if PART2:
            copied_nums_cat = copy(nums)
            copied_nums_cat = [int(str(nums[0]) + str(nums[1]))] + nums[2:]
            base = can_be_equation(sum, copied_nums_cat, with_opt)
        else:
            base = False
        ########### PART 2 ADDITION -- END ###########

        return (
            can_be_equation(sum, copied_nums_add, with_opt) or
            can_be_equation(sum, copied_nums_mult, with_opt) or
            base
        )


def f(x: str, with_opt: bool = False) -> int:
    x = x.strip()

    sum = 0
    for line in x.splitlines():
        expected_sum, nums = parse_line(line)
        if can_be_equation(expected_sum, nums, with_opt):
            sum += expected_sum

    return sum

print(f(e))

start = time.time()
print(f(q))
print(f"Duration: {time.time() - start} s")  # 11.2s

start = time.time()
print(f(q, with_opt=True))
print(f"Duration (with optimization): {time.time() - start} s")  # 6.2s

# Part 1: 4555081946288
# Part 2: 227921760109726