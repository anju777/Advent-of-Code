e = '''
Time:      7  15   30
Distance:  9  40  200
'''

q = """
Time:        59     79     65     75
Distance:   597   1234   1032   1328
"""

import re
import math

def parse_line(x: str):
    x = x.split(":")[1].strip().split(" ")
    # x = [int(i) for i in x if i != ""]
    x = "".join(x)
    return [int(x)]

def parse_input(x: str):
    x = x.strip("\n").splitlines()
    print(x)
    return parse_line(x[0]), parse_line(x[1])

def f(x):
    waystowin = []
    times, distances = parse_input(x)
    for time, distance in zip(times, distances):
        best_time = time/2
        win_time_high = (time + math.sqrt(time**2 - (4*(distance + 1e-9)))) / 2
        win_time_low = (time - math.sqrt(time**2 - (4*(distance + 1e-9)))) / 2
        # num_ways = round(abs(math.ceil(win_time) - best_time) * 2)
        num_ways = math.floor(win_time_high) - math.ceil(win_time_low) + 1
        print(win_time_high, win_time_low, num_ways)
        waystowin.append(num_ways)
    product = 1
    for ways in waystowin:
        product *= ways
    return product
        


def f2(x):
    total_points = 0
    x_array = x.strip('\n').splitlines()
    scratch_cards = []
    for line, content in enumerate(x_array):
        matches = 0
        _, rest = content.split(":")
        win_num_str, hand_num_str = rest.split("|")
        win_nums = win_num_str.split(" ")
        hand_nums = hand_num_str.split(" ")
        # print(win_nums, hand_nums)
        for hand_num in hand_nums:
            if hand_num == "":
                continue
            if hand_num in win_nums:
                matches += 1
        
        num_instance = scratch_cards.count(line + 1) + 1
        # print("line", line, f"matches: {matches}, copy: {num_instance}")
        for j in range(1, matches + 1):
            card_num = line + 1 + j
            # print(card_num, num_instance)
            scratch_cards.extend([card_num] * num_instance)
    # print(scratch_cards)
    return len(scratch_cards) + len(x_array)

print(f(e))
print(f(q))