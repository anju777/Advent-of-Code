e = '''
13-86,85-88
58-76,53-56
7-95,30-96
96-96,28-78
24-55,23-54
30-84,30-83
'''

q = '''
13-86,85-88
58-76,53-56
7-95,30-96
96-96,28-78
24-55,23-54
30-84,30-83
21-82,7-81
9-35,36-90
3-17,1-2
1-1,2-37
4-99,4-99
38-65,37-45
94-95,31-78
58-95,94-97
30-95,29-95
70-81,76-98
15-76,21-65
6-59,5-59
8-28,7-21
43-61,62-63
10-30,10-30
10-85,10-85
21-40,22-40
24-60,29-61
51-86,13-52
6-96,5-96
6-18,17-55
24-24,24-24
81-95,96-99
'''

import re

pattern = re.compile(r"(?P<x1>[0-9]+)-(?P<y1>[0-9]+),(?P<x2>[0-9]+)-(?P<y2>[0-9]+)", re.IGNORECASE)

def get_int_match(match, name):
    return int(match.group(name))

def parse_line(l):
    match = pattern.match(l)
    x1 = get_int_match(match, "x1")
    y1 = get_int_match(match, "y1")
    x2 = get_int_match(match, "x2")
    y2 = get_int_match(match, "y2")
    return x1, y1, x2, y2


def f(x):
    count = 0
    x = x.strip('\n')
    for line in x.splitlines():
        x1, y1, x2, y2 = parse_line(line)
        if x1 < x2:
            xmin, ymin = x1, y1
            xmax, ymax = x2, y2
        else:
            xmin, ymin = x2, y2
            xmax, ymax = x1, y1

        if (x1 == y1):
            print(x1, y1, x2, y2)
        
        if (xmin <= xmax and ymin >= ymax):
            # print(xmin, ymin, ",", xmax, ymax)
            count += 1
        elif (xmax <= xmin and ymax >= ymin):
            count += 1
    return count

def check_in(x, beg, end):
    return x >= beg and x <= end

def f2(x):
    count = 0
    x = x.strip('\n')
    for line in x.splitlines():
        x1, y1, x2, y2 = parse_line(line)
        
        if (check_in(x1, x2, y2) or check_in(y1, x2, y2)):
            count += 1
        elif (check_in(x2, x1, y1) or check_in(y2, x1, y1)):
            count += 1

    return count

print(f2(e))