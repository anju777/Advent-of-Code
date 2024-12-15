e = '''
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''

q = '''
addx 1
noop
noop
noop
addx 5
addx 5
noop
noop
addx 9
addx -5
addx 1
addx 4
noop
noop
noop
addx 6
addx -1
noop
addx 5
addx -2
addx 7
noop
addx 3
addx -2
addx -38
noop
noop
addx 32
addx -22
noop
addx 2
addx 3
noop
addx 2
addx -2
addx 7
addx -2
noop
addx 3
addx 2
addx 5
addx 2
addx -5
addx 10
noop
addx 3
noop
addx -38
addx 1
addx 27
noop
addx -20
noop
addx 2
addx 27
noop
addx -22
noop
noop
noop
noop
addx 3
addx 5
addx 2
addx -11
addx 16
addx -2
addx -17
addx 24
noop
noop
addx 1
addx -38
addx 15
addx 10
addx -15
noop
addx 2
addx 26
noop
addx -21
addx 19
addx -33
addx 19
noop
addx -6
addx 9
addx 3
addx 4
addx -21
addx 4
addx 20
noop
addx 3
addx -38
addx 28
addx -21
addx 9
addx -8
addx 2
addx 5
addx 2
addx -9
addx 14
addx -2
addx -5
addx 12
addx 3
addx -2
addx 2
addx 7
noop
noop
addx -27
addx 28
addx -36
noop
addx 1
addx 5
addx -1
noop
addx 6
addx -1
addx 5
addx 5
noop
noop
addx -2
addx 20
addx -10
addx -3
addx 1
addx 3
addx 2
addx 4
addx 3
noop
addx -30
noop
'''

def check_cycle(n, v):
    if (n in [20, 60, 100, 140, 180, 220]):
        return n * v
    else: return 0

def f(x):
    x = x.strip('\n').splitlines()
    num_cycles = 0
    val = 1
    prod = 0
    for line in x:
        if (line == 'noop'):
            num_cycles += 1
            prod += check_cycle(num_cycles, val)
        else:
            add = int(line.split(' ')[-1])
            for i in range(2):
                num_cycles += 1
                prod += check_cycle(num_cycles, val)
            val += add
    return prod

def update_array(a, n, v):
    n = n - 1
    row = n // 40
    col = n % 40
    n = n % 40
    print(n, v, row, col)
    if (v in range(n-1, n+2)):
        a[row][col] = '#'

def f2(x):
    array = []
    for i in range(6):
        array.append(['.'] * 40)
    
    x = x.strip('\n').splitlines()
    num_cycles = 0
    val = 1
    for line in x:
        if (line == 'noop'):
            num_cycles += 1
            update_array(array, num_cycles, val)
        else:
            add = int(line.split(' ')[-1])
            for i in range(2):
                num_cycles += 1
                update_array(array, num_cycles, val)
            val += add
    for i in range(len(array)):
        print(''.join(array[i]))

print(f2(e))