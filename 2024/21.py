"""
Object Closest
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

Controller Controller x 3
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

e = """
029A
980A
179A
456A
379A
"""

def get_code(seq: str) -> str:
    front_line_code = solve_front_line

with open("21.txt", "r") as f:
    q = f.read()

def f(x: str):
    sum = 0

    x = x.strip().splitlines()

    for sequence in x:
        number = int(sequence[:-1])
        code = get_code(sequence)
        print(f"Number: {number}, code: {code} (len {len(code)})")
        sum += number * len(code)

    return sum