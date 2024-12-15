e = '''
AAAA
BBCD
BBCC
EEEC
'''



import pprint
import copy
import re
import math

def parse_line(x: str):
    x = x.split(":")[1].strip().split(" ")
    x = "".join(x)
    return [int(x)]

def parse_input(x: str):
    x = x.strip("\n").splitlines()
    print(x)
    return parse_line(x[0]), parse_line(x[1])

pattern = re.compile(r"#+")
patternh = re.compile(r"([.]+|^)#+([.]+|$)")
patternc = re.compile(r"[#\?]+")
patternq = re.compile(r"\?+")

def f(x):
    x = x.strip("\n").splitlines()
    sum = 0
    def try_this(inputstr, combo):
        if "?" not in inputstr:
            hashes = pattern.findall(inputstr)
            for i in range(len(hashes)):
                hashes[i] = len(hashes[i])
            # print("Try_this", hashes, combo)
            # if hashes == combo:
            #     print(inputstr, combo)
            return int(hashes == combo)

        return try_this(inputstr.replace("?", "#", 1), combo) + try_this(inputstr.replace("?", ".", 1), combo)

    for line in x:
        layout, combo = line.split(" ")
        combo = list(map(int, combo.split(",")))
        hashes = patternh.findall(layout)
        clusters = patternc.findall(layout)
        questions = patternq.findall(layout)

        print("before", layout, hashes, combo)
        for hash in hashes:
            if hash.count("#") in combo:
                combo.remove(hash.count("#"))
                start, end = patternh.search(layout).span()

                layout = layout[:start] + "." + layout[end:]
        print(layout, combo)

        hashes = pattern.findall(layout)
        clusters = patternc.findall(layout)
        questions = patternq.findall(layout)

        curr = try_this(layout.replace("?", "#", 1), combo) + try_this(layout.replace("?", ".", 1), combo)
        sum += curr
        # print(line, "->", curr)

    return sum

    # return product



# def f2(x):""
#     x = x.strip("\n").splitlines()
#     return len(scratch_cards) + len(x_array)

print(f(e))
#print(f(q))