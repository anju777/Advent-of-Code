e = '''
2333133121414131402
'''

easy = """12344"""

huh = "90909"

with open("08.txt", "r") as f:
    q = f.read()

import copy
import re
import math
import time

def decompress(x: str):
    is_free = False
    id = 0

    res = []
    free_map = []

    for num in x:
        if not is_free:
            for _ in range(int(num)):
                res.append(str(id))
            id += 1
        else:
            free_map.append(int(num))
            for _ in range(int(num)):
                res.append(".")

        is_free = not is_free

    # print(f"Res: {res}")
    return res, free_map

def get_last_num(x: list):
    len_list = len(x)
    for i in range(1, len(x) + 1):
        if x[-i] != ".":
            return len_list - i, x[-i]
    # x_copy = copy.copy(x)
    # x_copy.reverse()
    # nums = range(10)
    # min_index = math.inf
    # min_val = None
    # for num in nums:
    #     if str(num) in x_copy:
    #         num_index = x_copy.index(str(num))
    #         if num_index < min_index:
    #             min_index = num_index
    #             min_val = str(num)

    # return len(x_copy) - 1 - min_index, min_val


# def try_move(x: list, block: list, end_block: list) -> bool:
#     needed_space = len(block)
#     cake = x
#     total_index = 0
#     while "." in cake:
#         start_space = cake.index(".")
#         start_start_space = start_space
#         while start_space < len(cake) and cake[start_space] == ".":
#             start_space += 1
#         # print(f"Start space: {start_space}, moving {block}")
#         if start_space > needed_space:
#             x[total_index + start_start_space:total_index + start_space] = block
#             x = x + end_block
#             # print(f"Moved: {x}")
#             return x, True
#         cake = cake[start_space:]
#         total_index += start_space
#     return None, False


def try_move(x: list, curr_num: int) -> bool:
    num_occurrence = x.count(str(curr_num))
    if num_occurrence > 0:
        # Move it
        start_index = x.index(str(curr_num))

        search_start_index = 0
        while "." in x[search_start_index:start_index]:
            # print(f"Prev search start: {search_start_index}")
            search_start_index = x.index(".", search_start_index, start_index + 1)
            curr_index = search_start_index
            while curr_index < len(x) and x[curr_index] == ".":
                curr_index += 1
            # print(f"# {curr_num}: search start: {search_start_index}, curr_index: {curr_index}")
            if curr_index - search_start_index >= num_occurrence:
                # print(f"Search start index: {search_start_index}, curr_num: {curr_num}")
                for i in range(num_occurrence):
                    x[i + search_start_index] = str(curr_num)
                for i in range(num_occurrence):
                    x[start_index + i] = "."
                return x
            search_start_index = curr_index + 1
    return x
    # cake = x
    # total_index = 0
    # while "." in cake:
    #     start_space = cake.index(".")
    #     start_start_space = start_space
    #     while start_space < len(cake) and cake[start_space] == ".":
    #         start_space += 1
    #     # print(f"Start space: {start_space}, moving {block}")
    #     if start_space > needed_space:
    #         x[total_index + start_start_space:total_index + start_space] = block
    #         x = x + end_block
    #         # print(f"Moved: {x}")
    #         return x, True
    #     cake = cake[start_space:]
    #     total_index += start_space
    # return None, False


def move(x: str, free_map: list) -> str:
    res = list(x)

    last_num_index, last_num = get_last_num(res)
    curr_num = int(last_num)
    while int(curr_num) > 0:
        # print(res)
        res = try_move(res, curr_num)
        # print(res)
        curr_num -= 1
    return res

def calc_checksum(x: str):
    checksum = 0

    for i, num in enumerate(x):
        if num == ".":
            pass

        else:
            checksum += i * int(num)

    return checksum

def f(x: str):
    x = x.strip()
    decompressed, free_map = decompress(x)
    moved = move(decompressed, free_map)
    checksum = calc_checksum(moved)

    return checksum

print(f(easy))
print(f(e))
start = time.time()
print(f(q))
duration = time.time() - start
print(f"Duration: {duration} s")

# Answer:
# 11805286780775  (17s)
# 6221662795602 (200s)