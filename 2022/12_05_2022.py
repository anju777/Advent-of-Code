import re

q = '''
        [J]         [B]     [T]    
        [M] [L]     [Q] [L] [R]    
        [G] [Q]     [W] [S] [B] [L]
[D]     [D] [T]     [M] [G] [V] [P]
[T]     [N] [N] [N] [D] [J] [G] [N]
[W] [H] [H] [S] [C] [N] [R] [W] [D]
[N] [P] [P] [W] [H] [H] [B] [N] [G]
[L] [C] [W] [C] [P] [T] [M] [Z] [W]
 1   2   3   4   5   6   7   8   9 

move 6 from 6 to 5
move 2 from 5 to 9
move 8 from 9 to 1
move 3 from 5 to 4
move 9 from 1 to 8
move 2 from 1 to 5
move 1 from 1 to 8
move 14 from 8 to 2
move 1 from 1 to 2
move 2 from 6 to 8
move 2 from 5 to 7
move 6 from 8 to 6
move 4 from 4 to 2
move 2 from 4 to 9
move 5 from 7 to 4
move 2 from 7 to 5
move 6 from 2 to 4
move 2 from 4 to 7
move 4 from 5 to 8
move 1 from 5 to 2
move 3 from 3 to 5
move 3 from 8 to 3
move 4 from 3 to 7
move 2 from 9 to 8
move 1 from 3 to 7
move 1 from 6 to 8
move 5 from 7 to 1
move 3 from 7 to 2
move 1 from 6 to 3
move 2 from 5 to 9
move 5 from 4 to 2
move 3 from 5 to 9
move 5 from 9 to 6
move 2 from 1 to 3
move 4 from 4 to 1
move 2 from 8 to 1
move 18 from 2 to 5
move 3 from 4 to 1
move 1 from 1 to 2
move 1 from 6 to 8
move 1 from 7 to 1
move 10 from 1 to 5
move 1 from 1 to 5
move 3 from 8 to 1
move 2 from 1 to 5
move 3 from 6 to 5
move 8 from 2 to 9
move 2 from 9 to 7
move 3 from 3 to 8
move 1 from 4 to 8
move 3 from 5 to 3
move 15 from 5 to 8
move 4 from 6 to 1
move 2 from 7 to 4
move 9 from 5 to 7
move 1 from 6 to 8
move 5 from 3 to 5
move 5 from 7 to 5
move 3 from 1 to 5
move 2 from 4 to 8
move 3 from 1 to 6
move 20 from 5 to 4
move 1 from 7 to 6
move 21 from 8 to 2
move 1 from 3 to 7
move 2 from 4 to 2
move 1 from 7 to 1
move 18 from 2 to 8
move 3 from 9 to 2
move 1 from 6 to 4
move 1 from 1 to 9
move 8 from 8 to 6
move 4 from 8 to 2
move 1 from 2 to 6
move 7 from 8 to 5
move 2 from 5 to 3
move 1 from 9 to 5
move 5 from 2 to 4
move 1 from 3 to 7
move 2 from 5 to 7
move 4 from 4 to 9
move 2 from 5 to 9
move 6 from 2 to 8
move 3 from 7 to 3
move 2 from 5 to 4
move 4 from 8 to 2
move 2 from 7 to 4
move 7 from 6 to 4
move 1 from 8 to 4
move 3 from 6 to 7
move 2 from 7 to 2
move 7 from 9 to 7
move 1 from 9 to 2
move 3 from 3 to 6
move 3 from 7 to 4
move 2 from 7 to 9
move 6 from 4 to 1
move 3 from 7 to 9
move 1 from 8 to 5
move 1 from 3 to 6
move 3 from 9 to 4
move 2 from 6 to 4
move 3 from 9 to 1
move 4 from 2 to 8
move 1 from 8 to 5
move 9 from 1 to 2
move 1 from 6 to 5
move 1 from 7 to 2
move 1 from 8 to 1
move 2 from 8 to 9
move 1 from 9 to 8
move 1 from 5 to 7
move 1 from 7 to 6
move 1 from 9 to 8
move 1 from 6 to 3
move 26 from 4 to 3
move 1 from 5 to 8
move 3 from 6 to 3
move 7 from 4 to 3
move 1 from 1 to 3
move 1 from 4 to 8
move 13 from 3 to 1
move 1 from 3 to 4
move 12 from 2 to 5
move 20 from 3 to 2
move 1 from 4 to 1
move 4 from 5 to 7
move 1 from 7 to 8
move 9 from 5 to 2
move 5 from 1 to 5
move 21 from 2 to 8
move 5 from 8 to 4
move 4 from 5 to 2
move 6 from 1 to 7
move 1 from 5 to 4
move 4 from 3 to 1
move 6 from 1 to 3
move 1 from 1 to 9
move 6 from 8 to 7
move 4 from 8 to 2
move 4 from 2 to 7
move 5 from 4 to 1
move 8 from 8 to 4
move 1 from 9 to 6
move 18 from 7 to 6
move 15 from 6 to 5
move 2 from 6 to 8
move 2 from 6 to 3
move 8 from 3 to 7
move 15 from 5 to 7
move 3 from 4 to 9
move 12 from 2 to 3
move 3 from 9 to 4
move 6 from 7 to 9
move 9 from 4 to 5
move 10 from 3 to 5
move 9 from 5 to 2
move 14 from 7 to 8
move 14 from 8 to 5
move 4 from 2 to 4
move 1 from 4 to 6
move 2 from 8 to 4
move 3 from 8 to 9
move 18 from 5 to 1
move 1 from 5 to 9
move 1 from 7 to 4
move 5 from 5 to 9
move 3 from 2 to 4
move 13 from 9 to 2
move 13 from 2 to 6
move 1 from 7 to 3
move 3 from 3 to 1
move 9 from 6 to 5
move 1 from 7 to 8
move 20 from 1 to 8
move 2 from 2 to 8
move 5 from 6 to 9
move 15 from 8 to 7
move 3 from 5 to 3
move 5 from 1 to 3
move 2 from 3 to 4
move 3 from 9 to 5
move 4 from 5 to 2
move 4 from 5 to 7
move 3 from 4 to 9
move 10 from 7 to 8
move 2 from 9 to 4
move 1 from 5 to 6
move 8 from 7 to 9
move 1 from 6 to 7
move 6 from 3 to 4
move 12 from 9 to 8
move 1 from 1 to 5
move 2 from 7 to 8
move 1 from 7 to 5
move 1 from 9 to 5
move 2 from 2 to 9
move 11 from 8 to 1
move 7 from 1 to 5
move 3 from 1 to 6
move 5 from 8 to 9
move 8 from 4 to 3
move 4 from 4 to 6
move 5 from 9 to 3
move 4 from 4 to 5
move 2 from 6 to 7
move 1 from 9 to 5
move 2 from 7 to 4
move 12 from 5 to 2
move 8 from 8 to 9
move 8 from 8 to 6
move 9 from 6 to 2
move 4 from 9 to 2
move 1 from 5 to 1
move 5 from 2 to 1
move 2 from 5 to 4
move 5 from 2 to 5
move 5 from 5 to 6
move 3 from 4 to 7
move 11 from 2 to 7
move 2 from 2 to 1
move 4 from 3 to 7
move 2 from 2 to 4
move 6 from 1 to 4
move 1 from 2 to 8
move 2 from 9 to 5
move 4 from 4 to 3
move 5 from 4 to 1
move 2 from 2 to 1
move 1 from 8 to 5
move 14 from 7 to 6
move 3 from 9 to 2
move 15 from 6 to 8
move 4 from 1 to 3
move 2 from 2 to 3
move 1 from 1 to 7
move 2 from 3 to 5
move 4 from 5 to 4
move 1 from 3 to 5
move 5 from 1 to 6
move 12 from 6 to 7
move 7 from 8 to 4
move 12 from 7 to 9
move 4 from 7 to 9
move 1 from 2 to 8
move 12 from 9 to 4
move 23 from 4 to 3
move 1 from 6 to 5
move 3 from 9 to 3
move 1 from 7 to 9
move 1 from 9 to 1
move 1 from 9 to 7
move 42 from 3 to 1
move 3 from 5 to 4
move 5 from 1 to 3
move 3 from 4 to 7
move 1 from 1 to 9
move 4 from 3 to 8
move 1 from 3 to 7
move 1 from 9 to 1
move 2 from 7 to 8
move 8 from 1 to 6
move 2 from 7 to 5
move 9 from 1 to 2
move 5 from 2 to 3
move 3 from 2 to 4
move 20 from 1 to 2
move 1 from 1 to 5
move 1 from 6 to 7
move 3 from 4 to 7
move 2 from 3 to 6
move 3 from 6 to 1
move 1 from 6 to 4
move 2 from 1 to 6
move 3 from 5 to 9
move 1 from 4 to 3
move 2 from 7 to 4
move 6 from 8 to 4
move 1 from 1 to 9
move 1 from 2 to 9
move 2 from 8 to 7
move 3 from 6 to 2
move 5 from 7 to 5
move 4 from 2 to 5
move 4 from 4 to 6
move 3 from 9 to 6
move 4 from 3 to 1
move 1 from 9 to 2
move 7 from 8 to 9
move 4 from 2 to 4
move 2 from 1 to 7
move 3 from 4 to 5
move 4 from 2 to 4
move 1 from 7 to 4
move 4 from 2 to 9
move 7 from 4 to 3
move 1 from 7 to 3
move 6 from 2 to 3
move 2 from 1 to 5
move 10 from 3 to 6
move 2 from 6 to 1
move 2 from 2 to 7
move 2 from 3 to 1
move 1 from 7 to 8
move 11 from 5 to 3
move 2 from 3 to 1
move 4 from 6 to 1
move 1 from 4 to 6
move 8 from 3 to 4
move 2 from 5 to 6
move 3 from 3 to 5
move 1 from 8 to 4
move 1 from 4 to 9
move 2 from 6 to 1
move 1 from 5 to 1
move 9 from 4 to 3
move 5 from 6 to 9
move 5 from 6 to 7
move 13 from 9 to 3
move 5 from 1 to 8
move 4 from 8 to 4
move 10 from 3 to 2
move 3 from 6 to 1
move 2 from 7 to 9
move 1 from 8 to 3
move 1 from 7 to 3
move 1 from 9 to 5
move 1 from 6 to 3
move 7 from 2 to 4
move 3 from 5 to 2
move 8 from 3 to 5
move 7 from 4 to 3
move 5 from 9 to 7
move 1 from 7 to 1
move 9 from 1 to 8
move 9 from 5 to 8
move 2 from 7 to 8
move 3 from 8 to 1
move 10 from 3 to 6
move 1 from 1 to 6
move 5 from 1 to 7
move 3 from 2 to 8
move 7 from 8 to 6
move 7 from 8 to 6
move 1 from 3 to 5
move 5 from 7 to 9
move 4 from 8 to 4
move 3 from 2 to 8
move 1 from 7 to 8
move 3 from 3 to 9
move 3 from 7 to 4
move 1 from 7 to 2
move 9 from 9 to 1
move 5 from 1 to 9
move 4 from 8 to 6
move 1 from 2 to 7
move 1 from 5 to 3
move 1 from 3 to 7
move 1 from 1 to 9
move 1 from 1 to 7
move 5 from 9 to 6
move 2 from 7 to 6
move 10 from 4 to 8
move 1 from 4 to 2
move 1 from 4 to 1
move 1 from 9 to 2
move 3 from 1 to 2
move 1 from 7 to 3
move 1 from 2 to 1
move 16 from 6 to 3
move 9 from 6 to 1
move 6 from 6 to 1
move 5 from 6 to 1
move 3 from 8 to 1
move 11 from 3 to 4
move 1 from 6 to 2
move 3 from 8 to 2
move 4 from 1 to 6
move 5 from 3 to 2
move 1 from 2 to 5
move 1 from 8 to 5
move 5 from 8 to 3
move 4 from 6 to 9
move 2 from 9 to 6
move 3 from 3 to 9
move 1 from 5 to 7
move 5 from 1 to 6
move 3 from 6 to 4
move 2 from 2 to 9
move 8 from 4 to 2
move 9 from 1 to 7
move 3 from 3 to 5
move 3 from 5 to 7
move 12 from 7 to 1
move 5 from 4 to 6
move 1 from 4 to 5
move 7 from 1 to 8
move 5 from 9 to 3
move 1 from 7 to 4
move 10 from 1 to 8
move 1 from 4 to 8
move 4 from 6 to 8
move 1 from 6 to 9
move 2 from 5 to 1
move 4 from 3 to 4
move 1 from 1 to 8
move 4 from 4 to 7
move 2 from 1 to 8
move 4 from 6 to 1
move 3 from 9 to 5
move 1 from 6 to 5
move 1 from 3 to 7
move 24 from 8 to 6
move 3 from 6 to 5
move 4 from 6 to 7
move 1 from 1 to 7
move 7 from 7 to 6
move 7 from 5 to 3
move 13 from 6 to 8
move 3 from 1 to 2
move 7 from 6 to 3
move 12 from 2 to 4
move 4 from 6 to 9
move 6 from 3 to 1
move 1 from 2 to 4
move 2 from 8 to 7
move 2 from 2 to 9
move 6 from 3 to 4
move 12 from 8 to 2
move 18 from 2 to 5
move 10 from 4 to 3
move 4 from 7 to 3
move 5 from 4 to 7
move 3 from 5 to 2
move 4 from 7 to 9
move 1 from 5 to 4
move 3 from 2 to 1
move 4 from 3 to 6
move 7 from 5 to 6
move 2 from 5 to 7
move 5 from 1 to 7
move 9 from 7 to 6
move 8 from 9 to 8
move 1 from 1 to 3
move 1 from 3 to 1
move 10 from 3 to 9
move 8 from 8 to 4
move 1 from 3 to 8
move 1 from 1 to 3
move 6 from 9 to 1
move 5 from 5 to 3
move 5 from 3 to 6
move 1 from 8 to 9
move 19 from 6 to 2
move 13 from 4 to 1
move 4 from 1 to 5
move 6 from 2 to 1
move 2 from 9 to 4
move 1 from 3 to 1
move 9 from 2 to 3
move 4 from 5 to 1
move 5 from 9 to 6
move 4 from 3 to 4
move 3 from 2 to 7
move 2 from 4 to 8
move 6 from 1 to 9
move 1 from 8 to 6
move 4 from 1 to 5
move 3 from 4 to 5
move 1 from 7 to 2
move 11 from 1 to 6
move 1 from 2 to 7
move 5 from 3 to 7
move 1 from 3 to 4
move 1 from 4 to 8
move 3 from 5 to 6
move 8 from 1 to 7
move 1 from 8 to 9
move 1 from 6 to 9
move 1 from 8 to 5
move 11 from 6 to 5
move 12 from 5 to 2
move 1 from 5 to 2
move 8 from 7 to 3
move 1 from 5 to 6
move 2 from 5 to 6
move 3 from 7 to 1
move 6 from 2 to 6
move 1 from 3 to 1
move 1 from 4 to 1
move 4 from 6 to 2
move 5 from 1 to 5
move 10 from 2 to 3
move 2 from 9 to 4
move 4 from 5 to 8
move 2 from 2 to 7
move 12 from 6 to 7
move 1 from 8 to 2
move 10 from 3 to 4
move 2 from 3 to 5
move 1 from 3 to 1
'''

x = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

def f(x):
    x = x.strip('\n')
    new = x.split('\n\n')
    init = new[0]
    instr = new[1].strip('\n')

    rows = init.splitlines()

    # VERIFIED
    cols = int(rows.pop().strip().split('  ')[-1])
    print(len(rows))
    crates = [None] * cols

    def add_crates(crates, row):
        for col in range(cols):
            box = row[1 + (col * 4)]
            if (box.isalpha()):
                if (not crates[col]):
                    crates[col] = []
                crates[col].append(box)
        return crates

    for row in range(len(rows)):
        crates = add_crates(crates, rows[-1 - row])

    pattern = re.compile(r"move (?P<num_crates>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)", re.IGNORECASE)
    def parse_instr(input_text):
        match = pattern.match(input_text)
        return int(match.group("num_crates")), int(match.group("from")), int(match.group("to"))

    for i in instr.splitlines():
        num_crates, from_c, to_c = parse_instr(i)
        for crate in range(num_crates):
            crates[to_c - 1].append(crates[from_c - 1].pop())

    ans = ''
    for col in range(cols):
        ans += crates[col][-1]
    return ans

def f2(x):
    x = x.strip('\n')
    new = x.split('\n\n')
    init = new[0]
    instr = new[1].strip('\n')

    rows = init.splitlines()

    # VERIFIED
    cols = int(rows.pop().strip().split('  ')[-1])
    print(len(rows))
    crates = [None] * cols

    def add_crates(crates, row):
        for col in range(cols):
            box = row[1 + (col * 4)]
            if (box.isalpha()):
                if (not crates[col]):
                    crates[col] = []
                crates[col].append(box)
        return crates

    for row in range(len(rows)):
        crates = add_crates(crates, rows[-1 - row])

    pattern = re.compile(r"move (?P<num_crates>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)", re.IGNORECASE)
    def parse_instr(input_text):
        match = pattern.match(input_text)
        return int(match.group("num_crates")), int(match.group("from")), int(match.group("to"))

    for i in instr.splitlines():
        num_crates, from_c, to_c = parse_instr(i)
        # -1 to account for index starting at 1
        crates[to_c - 1].extend(crates[from_c - 1][-num_crates:])
        crates[from_c - 1] = crates[from_c - 1][:-num_crates]

    ans = ''
    for col in range(cols):
        ans += crates[col][-1]
    return ans
