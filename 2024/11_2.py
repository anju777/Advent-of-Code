e = "0 1 10 99 999"

easy = "125 17"

q = "2701 64945 0 9959979 93 781524 620 1"

import time

def blink(x: list[int]) -> list[int]:
    new_stones = []
    for elem in x:
        if elem == 0:
            new_stones.append(1)
        elif len(str(elem)) % 2 == 0:
            half = len(str(elem)) // 2
            new_stones.append(int(str(elem)[:half]))
            new_stones.append(int(str(elem)[half:]))
        else:
            new_stones.append(2024 * elem)
    return new_stones

def f(x: str, num_blinks):
    x = x.strip().split(" ")
    x = [int(elem) for elem in x]
    x = [0]
    cache = {}

    num_split = 10
    total = 0

    for i in range(num_blinks):
        start = time.time()
        x = blink(x)
        print(f"{i} (duration: {time.time() - start} s)")
        print(x)

    return len(x)

# print(f(e, 1))
# print(f(easy, 6))
# print(f(q, 25))

# Part 1: 198075


# f speed
# 20 (duration: 0.00874638557434082 s)
# 21 (duration: 0.011331796646118164 s)
# 22 (duration: 0.03109884262084961 s)
# 23 (duration: 0.03379654884338379 s)
# 24 (duration: 0.04456758499145508 s)
# 25 (duration: 0.08118939399719238 s)
# 26 (duration: 0.09778237342834473 s)
# 27 (duration: 0.17654919624328613 s)
# 28 (duration: 0.2529280185699463 s)
# 29 (duration: 0.37378549575805664 s)
# 30 (duration: 0.5850882530212402 s)
# 31 (duration: 0.8848154544830322 s)
# 32 (duration: 1.3170809745788574 s)
# 33 (duration: 1.9774935245513916 s)
# 34 (duration: 3.042738914489746 s)
# 35 (duration: 4.499819040298462 s)
# 36 (duration: 6.928499221801758 s)
# 37 (duration: 10.291455507278442 s)
# 38 (duration: 16.017988681793213 s)
# 39 (duration: 23.83603048324585 s)
# 40 (duration: 37.83135151863098 s)
# 41 (duration: 63.31744146347046 s)


print(f(q, 75))
# Part 2: