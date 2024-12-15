q = '''
Monkey 0:
  Starting items: 93, 98
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 1:
  Starting items: 95, 72, 98, 82, 86
  Operation: new = old + 5
  Test: divisible by 13
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 2:
  Starting items: 85, 62, 82, 86, 70, 65, 83, 76
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 3:
  Starting items: 86, 70, 71, 56
  Operation: new = old + 1
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 5

Monkey 4:
  Starting items: 77, 71, 86, 52, 81, 67
  Operation: new = old + 4
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 5:
  Starting items: 89, 87, 60, 78, 54, 77, 98
  Operation: new = old * 7
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 4

Monkey 6:
  Starting items: 69, 65, 63
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 7:
  Starting items: 89
  Operation: new = old * old
  Test: divisible by 11
    If true: throw to monkey 0
    If false: throw to monkey 2
'''

e = '''
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
'''

# post_insection: round(worry / 3)
# Round: per monkey

def retrieve_op(line):
    assert 'Operation' in line

    op = line.split('new = ')[-1]
    ops = op.split(' ')
    op1 = ops[0]
    operator = ops[1]
    op2 = ops[2]

    def op_f(x):
        if op1 == 'old': x1 = int(x)
        else: x1 = int(op1)

        if op2 == 'old': x2 = int(x)
        else: x2 = int(op2)
        if operator == '*':
            return x1 * x2
        elif operator == '+':
            return x1 + x2
        elif operator == '-':
            return x1 - x2

    return op_f

def get_items(x):
    assert 'items:' in x
    x = x.split(': ')[-1]
    items = x.split(', ')
    items = list(map(int, items))
    return items

def perform_round(ms, m_stat, inspection, mod_val):
    for i, m in enumerate(ms):
        operation = retrieve_op(m[2])
        div = int(m[3].split('divisible by ')[-1])
        true_m = int(m[4].split(' ')[-1])
        false_m = int(m[5].split(' ')[-1])

        for j in range(len(m_stat[i])):
            item = m_stat[i].pop()
            worry = item
            new_worry = operation(worry)
            # new_worry //= 3
            new_worry %= mod_val
            if (new_worry % div == 0):
                m_stat[true_m].append(new_worry)
            else:
                m_stat[false_m].append(new_worry)
            inspection[i] += 1

def f(x):
    x = x.strip('\n')
    ms = x.split('\n\n')
    ms = list(map(lambda m: m.splitlines(), ms))
    m_stat = []
    inspection = []
    mod = []
    for m in ms:
        items = get_items(m[1])
        m_stat.append(items)
        inspection.append(0)
        mod.append(int(m[3].split(' ')[-1]))
    mod_val = 1
    for i in mod:
        mod_val *= i

    for i in range(10000):
        perform_round(ms, m_stat, inspection, mod_val)

    print(inspection)
    inspection.sort()
    m1, m2 = inspection[-2:]
        
    return m1 * m2

print(f(e))