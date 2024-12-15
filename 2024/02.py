e = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

import re

import numpy as np

def f(x: str):
    x = x.strip()
    success = 0
    for line in x.splitlines():
        num_a = list(map(int, line.split(" ")))

        diff = np.diff(num_a)
        factor = 1 if (np.count_nonzero(diff > 0) > len(diff) // 2) else -1

        prev = None
        skipped = False
        new_numa = []
        for num in num_a:
            if prev is None:
                if not (1 <= (num_a[1] - num) * factor <= 3) and not skipped:
                    skipped = True
                else:
                    prev = num
                    new_numa.append(num)
            else:
                curr_diff = (num - prev) * factor
                if not (1 <= curr_diff <= 3) and not skipped:
                    skipped = True
                else:
                    new_numa.append(num)
                    prev = num
        diff = np.diff(new_numa) * factor

        curr_success = True
        
        if np.count_nonzero(np.array(diff) <= 0) != 0:
            curr_success = False
        else:
            for d in diff:
                if not (1 <= d <= 3):
                    curr_success = False
                    break
        if skipped:
            print(f"\tdiff: {diff}, curr_success: {curr_success}")
        
        if curr_success:
            success += 1

    return success

def get_increment(l: list[int]) -> bool:
    diff = np.diff(l)
    increment = np.count_nonzero(diff > 0)
    decrement = np.count_nonzero(diff < 0)
    if increment > decrement:
        return True
    return False

def remove_first_oddity(l: list[int], incrementing: bool) -> list:
    # Remove any element that stagnates or goes up/down by more than 1 to 3
    l = list(l)
    new_list = []
    skipped = False
    factor = 1 if incrementing else -1

    assert(len(l) >= 3)
    diff1 = (l[1] - l[0]) * factor
    diff2 = (l[2] - l[1]) * factor
    if 1 <= diff1 <= 3 and 1 <= diff2 <= 3:
        new_list.append(l[0])
        new_list.append(l[1])
        new_list.append(l[2])
    elif not(1 <= diff1 <= 3) and not (1 <= diff2 <= 3):
        new_list.append(l[0])
        new_list.append(l[2])
        skipped = True
    elif not (1 <= diff1 <= 3) and (1 <= diff2 <= 3):
        new_list.append(l[1])
        new_list.append(l[2])
        skipped = True
    elif (1 <= diff1 <= 3) and not (1 <= diff2 <= 3):
        new_list.append(l[0])
        new_list.append(l[2])
        skipped = True
    else:
        assert False, "should not be happening!!"

    prev = l[2]
    for num in l[3:]:
        diff = num - prev
        if not incrementing:
            diff *= -1
        
        if not 1 <= diff <= 3 and not skipped:
            skipped = True
        else:
            new_list.append(num)
        prev = num

    if skipped:
        print(l, "->", new_list)
    return new_list


def check_safe(input_list: list[int]) -> bool:
    incrementing = get_increment(input_list)
    adjusted_list = remove_first_oddity(input_list, incrementing)
    diffs = np.diff(adjusted_list)
    if not incrementing:
        diffs = diffs * -1

    safe = True
    for diff in diffs:
        if not (1 <= diff <= 3):
            safe = False
    num_good = np.count_nonzero(diffs > 0)
    if num_good != len(list(diffs)):
        safe = False
    return safe
        

def attempt(x: str):
    success = 0
    for line in x.strip().splitlines():
        line = line.split(" ")
        line = list(map(int, line))
        if (safe := check_safe(line)):
            success += 1
    
    return success


q = """
82 84 85 87 90 92 93 91
7 10 12 14 17 19 22 22
66 68 69 72 74 78
10 11 13 14 17 18 25
34 36 39 41 43 42 44
35 37 40 37 39 38
12 13 10 11 11
57 58 55 58 60 62 66
59 62 59 62 63 66 67 74
46 48 51 53 54 56 56 59
5 6 7 7 6
86 87 89 89 92 92
77 80 81 84 85 86 86 90
70 73 76 77 77 78 85
37 40 44 46 49 50
61 63 67 69 72 70
47 48 49 50 54 57 57
72 75 79 80 82 86
29 31 32 36 43
83 84 91 92 94 97
17 19 20 21 23 24 29 27
25 27 32 35 35
28 29 30 35 38 41 45
58 59 60 62 63 68 70 77
71 69 70 71 72 75
62 60 62 65 66 63
15 12 15 16 19 19
18 17 20 21 23 25 29
9 8 10 13 16 19 25
70 69 66 69 71
62 60 63 62 65 68 67
36 35 38 40 38 40 42 42
26 23 26 24 27 31
9 7 8 6 9 12 18
78 76 78 79 82 82 85
24 22 22 23 21
47 46 49 49 49
40 39 40 42 42 45 49
26 23 23 24 27 30 36
77 74 76 80 81 84 86
85 84 88 91 89
53 52 54 57 61 64 67 67
59 57 61 62 65 69
57 55 59 61 64 70
71 70 71 78 79 81 84
83 81 87 89 92 95 94
62 61 68 70 72 75 77 77
20 19 22 24 30 32 35 39
45 43 50 53 56 58 59 64
30 30 31 32 35 38 41
49 49 51 53 56 54
10 10 11 14 14
63 63 66 69 71 75
25 25 26 29 30 32 38
60 60 62 60 63 65
76 76 74 75 74
63 63 60 61 63 64 66 66
81 81 83 86 84 87 91
17 17 18 17 18 20 27
40 40 42 45 47 47 48
24 24 27 29 29 30 31 28
20 20 23 24 24 24
90 90 90 91 95
47 47 48 49 52 52 53 59
64 64 65 67 68 70 74 77
5 5 6 8 11 15 14
79 79 82 86 87 89 89
33 33 34 36 37 41 45
32 32 34 38 40 42 43 48
16 16 19 25 27
90 90 91 96 98 99 96
8 8 14 17 19 19
1 1 4 6 8 13 17
83 83 86 92 99
51 55 57 59 60
47 51 54 57 59 62 61
15 19 22 23 26 29 30 30
45 49 51 54 57 61
15 19 22 23 24 25 30
27 31 29 32 33 36 39 40
8 12 10 11 10
22 26 28 26 27 27
20 24 27 24 25 27 31
8 12 13 10 11 12 18
34 38 40 42 42 44 46 49
6 10 11 14 14 15 12
29 33 33 36 39 39
45 49 50 53 54 54 56 60
66 70 70 73 79
65 69 71 75 76 77
21 25 29 30 33 36 34
29 33 34 35 36 40 40
6 10 11 15 19
10 14 17 20 23 27 29 36
27 31 37 39 40 41 44
80 84 87 88 90 97 94
12 16 21 22 22
21 25 26 29 34 37 38 42
9 13 15 20 23 25 26 31
68 73 74 75 77 78
28 35 37 40 42 44 41
41 47 50 51 54 55 56 56
7 14 17 19 21 25
51 56 57 60 65
39 45 44 47 49 52 55
71 77 78 77 78 80 83 82
45 51 53 55 56 53 53
35 40 42 45 47 49 47 51
65 72 69 71 73 79
40 46 47 49 49 51
56 63 65 65 64
39 46 49 49 49
81 87 88 88 92
11 17 17 20 22 23 28
40 46 47 51 53 54 56 57
34 40 42 46 43
31 36 40 43 46 48 49 49
13 19 20 24 25 27 30 34
17 24 27 29 33 36 43
79 85 92 95 97
48 55 56 62 65 67 66
65 72 75 77 84 84
44 50 55 57 61
36 41 44 45 48 55 58 63
76 75 73 72 69 72
45 42 41 39 38 38
82 81 79 76 74 70
49 47 44 41 38 35 34 29
51 48 45 42 43 40 39 36
22 19 20 19 18 17 19
49 48 46 43 44 44
63 61 63 61 59 55
52 49 46 48 46 41
36 35 34 34 32
88 87 85 85 83 85
77 74 74 72 72
32 29 29 27 23
94 93 90 87 87 82
54 53 49 47 46 44 41 40
33 32 29 25 22 24
95 93 91 88 84 82 81 81
43 40 36 34 31 28 24
18 16 14 10 4
34 31 29 24 22 19 18
54 51 46 44 41 44
72 71 64 63 60 59 57 57
69 66 61 59 56 53 49
92 91 88 85 79 78 75 70
47 49 47 44 42 41 40
94 95 93 90 93
60 61 60 57 56 56
41 43 42 40 36
63 64 62 60 57 54 51 44
73 76 73 76 74
59 61 60 63 61 59 60
60 63 62 61 62 62
9 11 9 7 6 3 5 1
27 29 27 26 24 27 25 18
50 51 48 48 45 44 42
65 67 67 65 66
85 87 84 83 83 83
6 8 8 6 2
71 72 71 69 68 68 61
57 59 56 53 51 48 44 41
75 77 74 72 68 69
90 92 89 88 84 81 81
59 62 60 58 57 53 49
87 89 86 82 77
20 21 14 11 9 7 5 2
18 21 20 17 10 7 9
70 73 72 67 65 65
67 69 67 66 60 56
73 75 68 67 65 64 61 56
25 25 22 21 18 16 13
82 82 79 76 73 74
3 3 2 1 1
57 57 56 54 50
20 20 19 17 15 14 7
50 50 53 50 49 46
73 73 70 71 74
56 56 58 55 55
62 62 59 62 58
76 76 74 71 72 71 66
99 99 97 96 96 95 93 90
63 63 63 61 58 55 58
39 39 37 35 32 31 31 31
30 30 28 28 25 23 19
77 77 74 72 69 68 68 61
61 61 59 58 54 51 48
43 43 41 39 35 33 34
15 15 13 9 6 5 5
20 20 19 15 13 11 7
30 30 29 25 18
61 61 60 57 56 50 48 47
70 70 63 60 57 58
97 97 91 89 89
65 65 59 56 55 51
52 52 45 44 37
58 54 51 48 47
69 65 62 59 58 61
57 53 50 49 47 45 45
37 33 32 30 29 28 24
17 13 10 8 1
37 33 30 32 30 29 28
51 47 50 48 47 45 44 47
99 95 96 93 93
53 49 52 49 45
62 58 57 55 57 55 49
32 28 25 23 23 22 20
13 9 7 7 5 2 4
41 37 36 36 36
51 47 45 42 40 39 39 35
33 29 26 23 20 20 15
60 56 54 53 49 48
61 57 54 51 47 46 44 45
85 81 77 74 74
74 70 69 65 63 59
49 45 44 40 34
27 23 21 20 13 12 11
71 67 60 59 58 61
48 44 42 35 34 31 28 28
84 80 77 75 74 73 67 63
64 60 57 55 53 48 42
94 89 88 85 83 81 80 77
88 83 80 78 76 75 72 75
73 67 65 63 61 58 58
21 14 13 10 7 3
19 13 12 11 4
27 21 22 19 16 15 12
98 93 91 89 92 94
13 7 8 6 6
26 21 19 22 19 17 15 11
44 38 41 39 33
67 61 60 57 57 55
44 38 38 37 34 35
36 31 31 30 29 28 25 25
80 75 72 72 71 70 66
45 38 35 32 29 28 28 22
78 72 70 66 65 63
25 19 15 12 11 9 11
43 36 33 29 28 26 26
80 74 73 71 69 65 61
85 80 77 73 70 67 64 59
99 94 93 90 87 81 80
54 47 46 43 38 37 36 38
71 66 63 60 53 51 51
97 92 89 86 85 79 76 72
70 64 62 60 55 49
18 17 18 20 22 25 25 23
17 18 19 21 22 23 27
28 26 25 26 27 24
20 20 22 29 32
67 67 68 69 70
20 22 20 18 16 11 13
34 38 39 41 40
18 12 13 10 8 8
79 79 77 76 75
75 69 68 67 67 65 63 62
98 93 91 89 88 88 83
60 55 57 56 53 51 50 47
10 14 15 16 17 18 22 26
65 65 62 59 57 56 55 49
83 81 80 77 75 74 76 72
62 62 60 57 54 48 46 41
48 41 36 34 36
90 83 78 75 73 73
43 50 52 55 56 53 55 55
42 38 36 37 34 31 30 26
16 17 12 11 9 9
54 54 47 45 44 43 40 36
52 55 56 60 64
74 74 70 68 65 62 59 54
42 37 31 29 22
74 70 68 68 70
93 96 95 94 96 93
49 52 55 59 60 67
19 19 22 24 27 30 29 29
37 41 44 46 46 48 51 52
15 11 12 9 7 4 1
85 81 75 72 71 71
85 86 86 85 81
63 63 66 71 75
33 40 43 43 43
68 72 74 74 75 77 79 79
59 53 52 50 47 46 43
36 36 33 31 30 30 23
78 79 78 76 76 74 71 72
49 48 50 53 59 65
18 22 24 24 25 31
14 12 8 6 3 3
64 64 64 66 71
19 23 25 28 31 32 33 37
13 12 9 6 6 2
23 23 24 31 36
40 40 38 35 37 33
63 70 70 72 76
36 33 32 34 31 31
20 24 26 28 30 33 34 40
8 8 5 4 5 3
63 63 62 60 59 61 58 61
98 91 87 85 82 78
48 48 51 53 56 62
38 35 38 41 45
25 19 17 15 15 15
20 19 19 16 13 13
31 28 29 30 34 36 37 39
33 30 31 32 34 33 36 42
74 76 71 68 65 62 60 53
66 72 75 72 79
65 64 62 55 54 50
22 20 15 14 12 7
54 54 51 53 54 55
41 41 42 44 49 51 51
60 59 58 57 56 49 49
9 12 18 19 22 21
30 34 37 38 44 41
31 27 23 20 18 11
18 21 19 16 15 8
76 76 75 73 73 70 68
50 55 58 60 60 65
27 23 21 20 19 17 20 20
53 54 57 59 56 57 61
55 48 48 46 45 43 39
12 16 18 25 26 27 31
62 59 61 64 66 66
66 60 59 58 51 48 45 42
72 76 79 80 83 85 87 90
45 42 46 49 53
70 75 77 78 78 75
39 39 37 34 31 27 29
45 47 50 52 54
17 16 14 11 8 6 3
63 64 66 68 70 73 75
72 70 69 66 65 62 61 58
86 84 81 80 77 76 74 72
84 87 90 92 95
97 96 93 92 91 89
34 31 28 26 25 24 22
11 10 9 7 4
44 42 40 39 37 35 33 31
88 87 85 84 83 82 80 79
2 4 6 9 10 12
84 81 80 79 76 73 71
21 18 17 16 13 10
59 60 61 64 66
28 26 23 21 20 17
93 90 87 85 83 80
34 33 32 30 28 26 24 22
7 9 11 14 17 19 21
95 92 89 87 86 84 81
67 69 71 72 73 76 78 79
10 11 14 17 18 19
61 64 67 69 70 71 74 75
72 70 69 66 64 63 61 60
67 68 69 72 73 75 78
86 83 82 80 78 77
79 81 82 84 86 88 91
27 30 32 33 34
6 8 10 13 15
28 29 30 31 33 35 37
59 61 63 65 67
20 18 17 15 14
87 88 89 92 95 96
13 10 8 7 6 5
8 10 12 14 17 18 21
72 71 69 66 65
76 74 73 70 69 67 64 63
87 86 84 81 78 76 74 71
40 43 45 48 50 51 54 56
23 21 20 18 16 14 12 11
46 45 44 41 39 36
32 33 36 37 39 41 43
83 84 87 90 92 94 96 97
47 49 50 52 55 58 61
3 4 7 9 12 13 16
25 26 27 28 31
18 19 20 21 23 25
78 81 82 85 87 90
93 95 97 98 99
56 53 51 50 48 45 43 42
98 96 94 92 89
68 69 72 74 75
55 58 61 62 64 66 68
83 86 89 90 92 93 94
6 7 10 12 13 15 18 19
14 12 10 8 5 4 2
28 31 33 35 38 39 42
22 21 18 16 14
61 64 65 68 69 72 74
34 33 32 29 28 25
10 11 12 13 15
72 70 68 66 64 61
77 80 82 84 86 89 91 92
51 52 55 58 59 61
77 74 71 70 68
47 44 41 39 36 33 32
28 31 33 35 38 39
31 32 34 36 38 39 42
72 73 75 77 78 81 82
11 8 7 6 3
85 84 82 80 77 74 71 70
73 74 76 79 80
77 75 73 71 68 66
11 13 16 18 20 21 24 25
84 87 88 91 94 97
84 87 88 90 91 93
89 88 86 83 81
73 76 79 81 82
23 26 28 31 32
67 68 70 72 74 75 76
30 32 35 38 39 41 44 46
36 35 34 31 30 28 25 23
22 25 27 28 30 33
24 22 20 19 18
98 97 95 93 91 88 85
14 17 20 22 25 26
39 40 42 45 48 49 52 53
40 38 37 35 33
9 10 12 14 16 19
25 23 21 20 17 15 13
55 54 51 48 45 43 41
46 48 50 52 53
42 43 44 47 50 52 55 58
34 31 29 28 26
31 28 26 24 22 19 18 16
13 11 9 7 6
75 76 78 81 83 85 86 87
6 7 8 11 14 15 16
18 21 22 24 25 28
89 87 85 84 81 80
85 84 83 82 80
60 59 56 54 51 49 46
67 70 71 74 77
58 55 52 50 49 48
7 10 12 14 15
11 9 7 6 4
31 34 36 37 39 40 42 43
47 48 49 50 51
49 50 52 53 56
32 34 35 38 40
12 13 15 18 19 20 22
24 21 18 16 15 12
86 83 80 77 74 71 68 66
82 84 86 89 92 94
61 58 57 54 53 50 47 45
19 22 24 26 27 30 31 34
19 21 24 26 27 28
9 11 12 15 18
36 33 30 28 25 22
24 25 28 29 31 32 35
26 29 32 34 36 38 41 44
38 40 41 43 45 48 49
81 82 83 86 89 90 93 96
93 94 95 96 98 99
57 56 54 53 52
42 39 38 35 34 31
19 16 13 12 11
96 94 92 90 87 86 83 80
37 40 42 43 44
81 78 76 74 72
83 82 81 79 78
70 72 74 77 79 81 82
68 70 73 76 79 82
97 94 93 92 89 87
42 43 44 47 49 51 52 53
32 35 37 38 39 42 45 46
58 60 63 65 68 71 73 75
63 65 68 70 73 75 78
67 70 72 75 77 80
82 80 79 77 76 73 70
28 25 24 22 19 17 14 13
22 25 27 30 33
44 41 39 36 35 34 32
78 76 75 73 71 70 68
12 11 8 7 4 3
71 72 74 76 77
64 62 61 60 59 57
84 83 82 80 77
95 94 91 88 87
23 21 20 19 18 17 15
76 74 73 71 68 67
52 54 56 58 59 62 63 66
38 39 42 45 48 49 52
68 69 70 73 74
92 90 87 86 84
49 48 46 43 42
58 55 53 52 50 49
42 45 46 49 51 54 56 58
46 44 41 39 38 35
43 45 47 49 50
62 61 58 55 54 52 50
73 74 77 80 81
38 37 35 33 31
34 33 30 27 25 23
17 16 13 12 9
88 86 85 84 83 80 79 76
15 17 18 21 22 25 28
25 22 20 19 16 14 11
74 77 80 82 85 87
91 89 88 87 84 81 80
88 86 85 83 80 79 76
63 60 58 57 55 54
75 77 78 80 83 85 87 90
60 57 55 52 50 47 46
88 85 83 80 78 77 75 72
49 52 55 58 60 61 63
13 12 11 10 9 7 5 3
82 80 79 78 75 73 72 69
41 38 35 33 31 30 29
75 74 71 68 65 63
55 58 60 63 66 68 71
88 86 85 82 80 77 76 73
75 74 72 70 68 66 63 62
43 42 41 40 39 37 35 34
33 34 35 38 39
88 86 83 80 77 75 72
31 28 25 22 19 16
45 46 49 50 51 54 57
14 11 10 8 6
44 43 42 41 39
19 17 15 14 11 10 9 7
45 48 50 52 54 56 58
52 55 56 57 58 61
7 9 12 14 17 18
25 27 28 31 34
53 51 48 47 44
15 17 19 21 23 26 29
50 49 48 46 45 43 42
73 76 77 79 80 81 84
71 69 66 64 62 59
73 70 69 67 64 63 61 58
85 87 89 91 93
71 74 77 78 80 82 84 86
4 5 7 9 11 12 14
72 71 69 66 65 63
35 36 39 42 43 44 46
6 7 9 10 13 16 17
16 15 13 12 9 6 5
29 30 33 35 37 38
29 26 23 22 19
60 63 66 67 69 70 72
53 52 50 49 47 46 45
1 3 4 7 8 10
51 49 47 45 43 40 37
24 25 28 29 30
80 78 77 76 74 72
82 84 85 87 89
58 55 52 50 48 45 43 41
71 72 73 74 77
48 46 43 42 41 39
63 61 60 58 56 53
27 29 32 33 35 37
72 69 68 67 65 62 61 58
38 41 44 47 50 51
35 38 40 41 44
16 19 22 24 25 26 28
56 53 52 49 47 44 41
86 84 81 79 76
70 73 75 77 79
58 57 54 51 49 47 45 42
42 45 46 47 49
68 66 64 62 59
33 30 29 26 23 20
50 47 46 43 42 39 38 37
82 80 77 75 74
25 23 22 19 16 15 13
62 64 66 68 70
19 21 24 26 27 30 32 33
58 57 56 53 52 51 49
78 75 73 71 68 67 65 62
60 57 56 55 52 50 49 47
47 45 44 43 40 38 35
34 32 31 28 25 23 21 20
82 79 76 74 72 70
71 73 74 76 79 80
6 8 11 13 14 16 19
11 12 13 15 17
79 78 76 75 74 71
64 62 59 56 55 53 50
64 63 62 61 58
12 14 15 16 17 20 23
76 78 80 81 82 85 88
41 43 46 48 50 53 55 58
71 72 74 75 78 79 81 84
71 74 76 79 80
58 61 62 64 67 70 72
49 47 45 42 39 36
18 20 21 24 26 29
8 9 12 13 16 17 18 19
58 59 61 63 64 65 67 70
57 60 63 66 69 72 73
86 85 84 83 82 79 76 74
64 65 67 69 71 74 75
29 30 31 34 37 38 40 42
10 12 13 14 17 18 21
67 69 71 73 74 76 79
12 9 7 6 5
35 37 39 42 45 46
52 50 49 47 45 43
96 95 94 92 89 86 85
28 25 24 22 20
64 66 69 70 73 75 78
54 53 51 48 45 42 41
42 43 45 46 48 50 53
35 38 40 41 44 46 48
27 25 23 20 19 17 15
36 39 41 44 45 46 48 51
33 30 28 27 25 24 22 20
42 43 44 45 46 49 52
14 15 18 21 24 26 27
48 45 42 39 36 34 31 28
72 71 70 69 67 66
82 84 85 87 89 91 94 97
35 36 37 40 42 43
60 63 65 66 67 68 71 73
77 80 83 84 85 86 87
20 18 15 14 11 8
78 81 83 86 89 91 93 95
53 55 56 59 61
78 81 83 86 89
55 58 60 62 65 68 69
68 66 64 63 61 60 59 57
53 55 57 58 60 62
35 34 32 29 27 24 23 21
47 45 42 41 38
81 82 83 86 89 91 94
34 31 30 27 25 23 20 19
80 77 74 71 70
14 13 11 10 7
63 60 59 57 55 52 51
58 55 53 51 49 47 46 45
63 66 68 69 71
42 45 48 51 53 54 56 59
19 20 21 24 25
14 16 17 20 21 23 26
64 61 58 57 54 52 51
78 80 83 86 88
58 55 54 51 50 47 46
29 26 24 21 19
23 21 19 18 17 16
71 74 77 80 81 84 85
76 78 80 81 82 84 86 89
79 80 81 84 85 87 89
37 38 41 43 46
45 47 50 53 55 56 57
34 33 32 30 28 25
41 44 46 47 50 52 55 56
78 75 72 71 69 67 64 63
87 90 93 96 99
83 84 86 88 89 91 94
74 77 79 82 83
79 81 83 85 86 89
7 10 11 14 16
86 88 89 92 94 96
52 51 48 46 43 40
85 82 79 77 75 74
32 34 35 36 39 42 44 47
81 84 85 87 88
16 14 13 12 11 9 7
93 91 88 85 84 81 78
49 47 45 42 41 39
60 61 62 65 66 67 69 72
22 23 25 28 29 32
40 37 36 34 31 30
62 65 67 70 72
68 71 72 75 78 79 82
16 19 22 23 26 28 31
66 63 61 59 57 56 55 52
2 4 6 7 10
36 33 32 31 28 25 23
12 10 7 5 3
24 23 22 21 18
24 22 19 18 17 16 15 13
14 13 12 11 10
29 32 35 37 40 41 43 45
58 61 62 64 66 69 70
81 83 86 88 91 93
11 12 14 17 20 22 25
83 85 87 88 91 92 95
79 80 83 85 88 89
53 50 49 47 46 43
73 76 78 80 83 84
61 59 58 57 56
24 25 28 30 31 34 37
79 76 75 73 72 71
45 46 48 51 52
28 30 31 33 36 38 39
16 17 20 22 24 25 26
74 72 70 68 65
67 66 64 63 60 57 54 53
37 38 40 42 44 47
50 48 46 43 40 38 37 35
83 81 80 78 77 76
39 38 35 32 30 28
40 41 44 47 49 51 52
59 61 64 67 68
36 33 32 31 29
1 3 4 6 7 10 12
87 88 89 91 94 97
54 55 58 61 63 65 68 71
72 73 76 78 81 82
64 61 60 57 56 54
42 44 47 49 51 54
65 67 68 70 73 75 77 80
12 11 8 7 6
18 16 13 11 9 6
50 53 56 59 60 62 65 67
42 39 37 35 33 32 30 28
31 28 25 24 22 21
6 8 11 14 16
60 62 64 65 66 69
58 56 53 51 49 48 46 43
22 19 18 17 14 13 10
37 35 33 30 27
21 20 17 16 15 13 11 9
60 59 57 54 53
36 38 39 41 44 47 48 50
79 81 83 84 86 89 92 95
66 69 72 75 78 81 82 85
1 4 5 6 8 9 10
2 3 5 6 8 11
55 53 50 49 47 46
66 68 70 71 73 76 78 79
55 57 58 61 62 65
12 10 8 6 3 1
16 18 21 23 26
52 55 56 57 60 62 64
6 7 9 12 15
92 89 86 85 84 82 81 80
69 72 75 77 79 82 83
90 93 94 95 98
57 60 63 65 67 69 70 72
97 95 94 92 89 88 85 84
99 98 97 94 93 91 89
13 15 18 19 22 23 24
68 66 65 64 62 61 58
54 57 59 61 62 63 64 66
88 87 85 84 83 81 78
17 16 14 12 11 10 7
21 22 23 25 26
15 13 12 11 10
80 77 75 74 71 70 67 64
15 12 10 8 7 4 1
1 4 7 10 12 13
66 69 70 71 74
45 44 42 41 40 37
84 86 89 90 91 94 96
56 58 61 62 63 66 68 69
99 96 93 92 90 89
25 24 23 22 20 18 15
12 10 9 7 4
12 13 16 18 19 20 21 22
90 89 87 86 85 83 81
80 79 76 73 71 69 66 64
73 75 77 79 81 82 83
88 87 86 83 80
73 74 77 80 81 82 84
70 71 72 74 75 76
61 60 57 56 53 52
84 86 88 91 93 96 97 99
92 91 90 89 86 83 81
5 8 9 12 14 15 18
60 61 64 67 68 71 73
37 34 32 30 28 25
58 56 55 52 51 49
34 31 28 25 23 22 20 19
46 44 42 39 37 34 33 31
42 39 37 35 34 32 31 30
1 4 5 8 10 11 12 15
81 82 84 87 90 92 93
27 25 22 21 20 19
95 92 90 89 88 85
58 56 54 51 48 47 46 44
37 38 40 41 44 46
25 22 21 18 16 15 14
61 62 63 64 67 68
68 71 73 76 78 80
21 19 17 16 13
41 40 37 36 34
31 34 37 40 42 43 46 49
43 42 41 38 37
89 87 84 83 82 79 77
38 36 33 31 30 28 26
13 16 17 20 23
90 93 94 96 97 98
68 66 65 63 62 60 57
87 84 81 80 77 76 73 71
76 77 79 81 82 85 86 88
77 79 80 81 83 86
64 61 60 57 56
37 35 32 31 28 26 23 21
7 6 3 2 1
69 68 67 66 63 62
40 41 42 44 47 49 52 54
25 27 29 32 33 35 37
76 79 81 84 86 87 89 90
68 71 74 75 77 79
29 31 32 34 35 38 39 41
45 48 49 51 52 55
37 35 33 30 28 27 26
46 48 49 51 53
68 67 64 62 60
37 34 32 31 28
68 71 72 75 78 79 81
76 78 79 80 82
37 38 41 44 45
19 16 13 11 8 6
60 63 66 68 70
37 34 33 31 28 26 23 20
60 61 64 65 68 71 72
79 80 82 85 88 90 93
94 93 91 90 87 84 82 80
45 48 50 51 54 56
63 66 67 70 72
74 77 79 81 83 85
43 41 40 39 37 36 33
44 41 40 38 37
84 82 79 78 75 74 71 69
15 16 18 21 24 27
59 58 56 54 52
30 32 34 35 36
7 9 12 13 15 18 20 22
29 30 31 33 34 35 36 37
53 56 58 60 62 64 65
30 33 35 36 39 42 43
73 72 71 69 68 66
44 47 49 52 54
9 10 13 16 17 20 23
41 42 43 45 46 47 48
59 57 55 52 49 46 44 41
77 78 80 81 84 87 89
5 7 10 11 14 16 17 18
55 58 60 63 65 67 68
65 64 63 61 59 57
53 56 58 60 63 64 65
25 22 20 18 17
62 64 67 69 70 71 72 75
76 75 74 72 69 66 65 62
7 9 10 12 13 14
37 34 31 28 26
4 6 7 10 11
32 35 36 37 39 40
30 31 32 34 36 38
87 89 91 92 94
52 53 54 55 58
36 34 33 31 30 29 27 25
54 56 59 62 64
56 57 59 62 64 66 67
61 63 66 69 71 74 76 78
28 30 32 33 35 38 41
50 47 45 43 40 38
79 82 84 86 89 92 94
38 41 43 45 48 51
22 24 25 28 31 33
40 39 38 37 35
73 75 77 78 79
10 12 14 16 17 20
75 73 71 68 67 65 64 62
28 26 24 23 21 20 17 16
44 41 38 36 34
2 3 5 8 9 11 12
29 30 33 34 37 39 42
68 66 63 62 60
20 18 17 16 15 13 12 10
26 24 21 20 19 17 15
51 49 46 44 41 40 37 35
19 18 15 12 9 7 6 3
23 20 17 15 12 10 8
77 78 79 82 83 84
77 75 72 69 66 65 62
46 45 42 40 39 36
42 45 47 48 50
16 13 11 8 6 5 2
66 64 63 62 60 58
52 50 49 46 45 44 41 38
81 78 77 76 73 72 70 69
24 27 28 31 33 35 36
55 57 59 60 61
80 81 84 87 88
53 55 56 57 59 60 62
55 54 51 49 47 45 44 42
54 55 57 60 62 65 68 70
83 85 88 91 94 97
62 65 68 70 71 72 73
84 81 80 77 75 74 73
61 63 65 68 71 74 77
84 87 89 92 95 97 99
70 71 72 73 74
24 22 20 17 14 12 9 8
64 63 61 58 55 52
17 20 22 25 28
44 46 48 49 50 52 55
85 83 82 81 78 76
41 40 38 36 34 33
25 23 20 18 16 13
21 19 16 15 12
14 15 17 20 22 23 26 27
83 82 79 77 74 72 71 70
22 21 20 17 15 13
31 30 27 24 21
39 40 41 42 43
7 10 11 14 16 19 22
11 13 14 17 18 20 22
18 21 24 25 28
25 26 29 32 33 36
86 85 83 80 77 74 72 69
61 62 65 66 67
86 89 92 95 96 97 99
86 83 82 80 79 77
63 60 59 58 57 56 53
59 57 54 51 48 47 46
68 66 65 63 62 59
35 36 39 41 44 45 46 48
68 66 65 64 61 58 57
46 43 42 41 39 37 34 33
96 94 91 89 87
73 74 76 77 80 81
5 6 7 10 12 14 15
15 18 21 24 25 27 30 31
36 39 41 44 47 48 50 51
88 87 84 82 79 78
52 53 54 56 59 60
22 23 26 29 32
56 58 61 62 63
92 89 87 84 82 79 78
4 5 8 10 13 16
9 6 5 3 1
94 92 90 88 87 86
40 39 37 36 33 30
28 26 24 22 20 19
28 27 26 24 23
22 23 26 29 30 33 34
26 23 21 20 19 18 17 16
34 32 31 29 28 26 24 22
78 81 83 86 89 91
55 53 50 49 47 46 44 42
8 9 12 15 16 18
16 15 13 10 8 7
65 67 69 72 75 78
41 40 38 36 33 31 30
31 29 26 23 21 19 18
29 31 34 35 38 39 41
93 90 87 84 81 78
66 65 62 60 59 56 55 52
46 48 49 51 52 53
73 76 79 82 84
38 40 43 45 48 51 53
97 95 93 92 90
84 87 89 91 92 94
50 48 47 45 42
14 13 12 9 8
46 48 50 51 52 53 56
58 56 55 53 50 47
50 47 45 42 39
41 42 44 46 49 52
33 31 30 29 28
65 63 61 60 58 55 52
74 73 72 70 67 66
85 83 81 79 78 77 76 73
1 4 7 9 12 14 17 20
63 62 59 56 55
44 47 49 50 52 55
12 11 9 8 5 4 3 1
13 16 17 20 21 24 25 28
87 85 84 81 78 76 74 73
26 23 20 18 17 16
61 64 67 70 72 73
86 88 91 94 95
61 58 56 55 54 51 50 48
4 6 8 11 13 15 18
29 30 33 34 35
74 72 71 70 67 64 61 59
77 79 81 83 85 87
94 93 90 89 86 85
78 75 72 71 69
87 89 92 93 95
28 25 24 23 20 17
95 93 90 89 87 84
28 27 25 24 23 20 18 15
30 27 26 23 22 20 18 15
26 29 32 35 38
37 39 42 43 45 47 48
70 68 66 63 62 59
41 43 46 47 48 51 52
6 8 11 14 17 18 20
31 28 25 22 21 18 17 14
94 92 91 90 87 85
71 73 75 78 79
27 29 30 32 34 36 38 40
68 70 72 73 75 77 79
93 92 91 90 87 85 83
58 57 55 52 51 50 48
65 64 62 59 58 56 54 51
46 43 40 37 34 31
9 10 13 16 17 19 22 25
26 23 21 20 17 16
43 40 39 36 34 33
23 21 19 16 15 12 10 8
38 39 41 42 45 48
26 25 24 22 21 19
"""

# print(f(e))
# print(f(q))
print(attempt(e))
print(attempt(q))