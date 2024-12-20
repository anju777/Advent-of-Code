e = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

q = """
Game 1: 1 red, 10 blue, 5 green; 11 blue, 6 green; 6 green; 1 green, 1 red, 12 blue; 3 blue; 3 blue, 4 green, 1 red
Game 2: 3 red, 5 green; 5 green, 7 red; 1 blue, 7 red, 3 green; 3 red, 2 blue; 5 green, 4 red
Game 3: 4 blue, 4 green; 2 green, 2 blue; 8 green, 2 red, 3 blue
Game 4: 3 blue, 15 green; 16 green; 2 red, 7 green; 2 blue, 14 green
Game 5: 8 green, 6 red, 16 blue; 8 red, 12 green; 1 red, 9 green, 16 blue; 8 red, 3 green; 2 blue, 5 red, 10 green; 15 red, 4 blue, 8 green
Game 6: 5 blue, 2 green; 6 red, 3 green; 4 green, 4 blue, 2 red; 14 blue, 2 red
Game 7: 2 green, 6 blue, 1 red; 2 blue, 1 red; 8 blue; 5 blue, 1 green; 6 blue, 1 red; 2 blue
Game 8: 1 red, 10 blue, 1 green; 6 blue, 1 red; 3 blue, 2 green; 1 red, 1 blue, 3 green; 13 blue; 10 blue, 3 green, 3 red
Game 9: 2 blue; 8 green, 3 blue; 4 green; 14 green, 1 red, 2 blue; 3 blue, 1 red, 12 green
Game 10: 1 blue, 7 green; 1 red, 3 green, 5 blue; 1 blue, 5 green, 1 red; 13 green, 5 blue, 2 red
Game 11: 1 green, 10 red, 6 blue; 15 red, 12 blue; 18 red, 1 green, 1 blue
Game 12: 16 red, 8 blue, 1 green; 15 red, 3 blue, 1 green; 5 red
Game 13: 6 red, 7 blue, 7 green; 3 blue, 4 red, 13 green; 1 blue, 6 red, 11 green; 2 red, 1 blue, 14 green; 8 green, 5 blue, 2 red; 4 blue, 18 green, 4 red
Game 14: 16 red, 3 blue, 1 green; 7 green, 3 red; 16 red, 15 green, 3 blue; 3 blue, 13 red, 10 green
Game 15: 1 blue, 1 red; 3 blue, 2 green; 1 red; 2 red, 2 green, 3 blue; 3 blue, 1 red, 3 green
Game 16: 9 red, 3 blue; 13 red, 9 blue; 9 blue, 10 red; 5 red, 10 blue, 1 green; 2 red, 6 green, 8 blue; 6 green, 13 red, 5 blue
Game 17: 15 red, 17 green, 8 blue; 18 red, 16 blue, 15 green; 8 blue, 17 green, 10 red; 5 green, 3 red, 12 blue
Game 18: 2 blue, 11 red, 2 green; 1 green, 11 red, 11 blue; 1 red, 4 blue; 10 blue, 9 red; 1 blue, 7 red
Game 19: 2 blue, 3 green, 5 red; 8 blue, 16 green; 12 red, 7 blue, 8 green; 9 green, 1 blue; 3 red, 16 green, 10 blue
Game 20: 3 blue, 5 green, 6 red; 2 red, 8 blue, 7 green; 7 green, 3 blue; 2 red, 11 blue; 1 green, 6 red, 3 blue
Game 21: 16 red, 3 blue, 8 green; 10 red, 15 blue, 3 green; 6 green, 13 red, 15 blue; 11 green, 13 blue, 10 red
Game 22: 8 green, 1 blue; 2 blue, 9 green, 3 red; 2 red, 2 blue; 1 red, 3 blue, 8 green; 2 blue, 1 green; 1 green, 2 blue
Game 23: 2 blue, 8 red, 5 green; 9 green, 2 blue; 10 red, 2 green; 12 red, 1 blue; 11 green, 2 blue, 13 red; 7 green
Game 24: 6 red; 13 green, 7 red, 10 blue; 7 green, 9 red, 1 blue; 3 blue, 2 green, 2 red
Game 25: 7 green, 1 red, 2 blue; 8 green, 2 blue, 5 red; 5 blue, 8 green, 4 red; 5 blue, 2 green, 1 red; 5 green, 3 red, 7 blue; 3 blue, 6 green, 1 red
Game 26: 6 green, 3 red; 1 blue, 2 green, 2 red; 2 green, 2 red, 3 blue; 4 blue, 8 red, 2 green; 1 red, 1 green, 1 blue; 6 red, 5 blue
Game 27: 4 green, 13 blue, 2 red; 2 red, 7 green, 10 blue; 14 blue, 11 green, 1 red; 10 blue, 15 green
Game 28: 4 green, 13 red, 7 blue; 2 red, 5 blue; 5 blue, 4 green
Game 29: 6 green, 15 red; 1 blue, 6 red, 8 green; 6 green, 1 blue; 12 red; 1 green, 7 red, 1 blue
Game 30: 4 blue, 4 green, 2 red; 6 blue, 9 red, 20 green; 9 blue, 4 red, 2 green; 8 red, 8 blue, 1 green; 6 green, 12 blue, 2 red; 8 green, 8 red
Game 31: 9 blue; 1 red, 2 blue, 5 green; 2 blue, 2 red, 9 green; 2 blue, 1 red, 8 green; 11 green, 2 red, 3 blue; 7 green, 5 blue
Game 32: 15 red, 5 green; 4 green, 2 blue, 3 red; 1 blue, 9 red; 1 blue, 15 red; 4 blue, 2 red, 8 green; 3 green, 3 blue
Game 33: 13 blue, 1 red, 1 green; 8 blue, 6 red; 4 blue, 2 red
Game 34: 5 blue, 9 red, 7 green; 8 red, 6 green, 5 blue; 2 blue, 7 green, 12 red
Game 35: 4 blue, 15 red; 1 green, 10 blue, 7 red; 9 red, 3 green, 1 blue; 13 red, 9 blue; 3 blue, 2 red
Game 36: 4 blue, 18 green, 2 red; 5 green, 6 blue, 11 red; 6 red, 12 blue, 14 green; 19 green, 10 blue, 7 red; 7 red, 8 green, 9 blue
Game 37: 16 blue, 5 green, 18 red; 3 blue, 14 green, 1 red; 4 blue, 3 green, 14 red; 12 green, 7 red, 15 blue; 15 green, 11 blue, 2 red; 8 blue, 13 green, 6 red
Game 38: 6 red, 4 blue, 12 green; 3 red, 11 blue; 16 green, 2 blue, 8 red; 4 blue, 11 red, 4 green; 17 green, 7 red, 10 blue; 9 blue, 15 green, 1 red
Game 39: 1 green, 1 red, 10 blue; 1 red, 5 blue, 2 green; 4 red, 7 blue; 9 red, 6 green, 5 blue; 1 green, 2 blue, 9 red
Game 40: 13 blue, 11 red, 12 green; 8 green, 11 red, 4 blue; 2 blue, 2 green, 12 red; 2 green, 3 red, 13 blue; 13 blue, 6 red, 2 green; 4 green, 6 red, 8 blue
Game 41: 12 red, 4 green, 13 blue; 4 red, 7 blue, 10 green; 17 green, 17 red, 11 blue
Game 42: 1 red, 1 green; 1 red, 4 green; 1 blue, 4 red, 4 green; 3 red; 1 blue, 3 green, 1 red
Game 43: 7 blue, 10 green; 5 blue, 2 green; 2 blue, 1 green, 4 red; 14 red, 6 green, 7 blue; 4 green, 14 red, 8 blue; 4 green, 6 red
Game 44: 9 green, 4 red; 4 red, 6 green; 5 red, 2 blue, 7 green; 9 blue, 1 green, 14 red
Game 45: 20 blue, 4 red, 6 green; 3 blue, 1 green, 6 red; 8 blue, 8 green, 11 red
Game 46: 1 green, 6 red; 6 red, 3 blue, 3 green; 6 red, 3 blue, 4 green; 1 blue, 5 red; 1 green, 4 red, 1 blue; 2 green, 4 red
Game 47: 12 green, 8 red, 4 blue; 7 green, 6 red, 11 blue; 4 red, 11 blue, 12 green
Game 48: 1 green, 3 blue; 13 green, 3 red, 11 blue; 7 blue, 1 green, 2 red; 7 red, 15 green, 4 blue; 4 red, 8 blue, 10 green; 15 green, 8 blue, 6 red
Game 49: 2 red; 2 red, 9 blue; 4 blue, 1 green
Game 50: 10 blue, 1 green, 18 red; 13 red, 1 green, 7 blue; 4 red, 2 green, 9 blue; 2 green, 4 red, 10 blue; 7 blue, 3 red; 19 red, 9 blue
Game 51: 2 green, 2 red, 5 blue; 9 red, 5 blue; 3 red, 10 blue; 9 blue, 6 red, 7 green; 2 red, 5 blue
Game 52: 6 blue, 3 green; 5 green, 3 blue, 5 red; 1 blue, 2 green, 2 red
Game 53: 2 blue, 9 green, 15 red; 18 red, 1 blue; 13 red, 12 green; 7 green, 2 blue, 9 red
Game 54: 18 green; 2 red, 6 green; 6 red, 9 green, 1 blue; 1 blue, 4 green, 5 red; 3 red; 3 green, 4 red
Game 55: 5 red, 2 blue, 5 green; 10 blue, 4 green, 8 red; 15 green, 9 blue, 9 red; 1 green, 9 blue
Game 56: 8 green, 11 blue, 1 red; 1 blue, 1 red, 4 green; 8 blue
Game 57: 5 green, 4 blue; 1 blue, 4 green; 1 red, 1 green, 3 blue; 1 red, 2 blue, 6 green
Game 58: 8 green, 10 red, 10 blue; 8 blue, 6 green, 12 red; 9 green, 11 blue, 1 red; 12 red, 5 green, 11 blue; 7 red, 2 green, 8 blue
Game 59: 10 red, 1 green, 3 blue; 16 red, 1 green, 4 blue; 9 red, 2 blue; 1 red
Game 60: 11 blue, 13 green, 10 red; 15 red, 12 blue; 3 blue, 9 green, 6 red; 12 blue, 5 green
Game 61: 2 blue, 7 red; 3 green, 14 blue, 11 red; 7 red, 10 blue; 6 blue, 3 green, 4 red; 10 blue
Game 62: 1 blue, 7 green; 6 red, 12 green, 1 blue; 8 red
Game 63: 1 blue, 3 green, 1 red; 8 green, 10 red, 1 blue; 8 green, 11 red; 1 blue, 11 green, 5 red; 8 green, 11 red, 2 blue; 2 blue, 10 red, 6 green
Game 64: 17 green, 2 blue; 12 blue, 8 green; 11 green, 3 red, 4 blue; 5 red, 9 green, 14 blue
Game 65: 7 blue, 12 green, 5 red; 13 green, 5 blue, 4 red; 4 blue, 8 green, 1 red; 5 red, 10 green, 10 blue; 5 red, 5 blue, 15 green; 4 red, 9 green, 10 blue
Game 66: 8 green, 2 red; 8 red, 4 green; 5 red, 2 blue, 7 green
Game 67: 10 green, 7 blue, 2 red; 15 blue, 1 green, 9 red; 2 red, 7 green, 18 blue; 3 green, 5 blue, 8 red; 10 green, 11 blue, 1 red; 10 green, 4 red, 17 blue
Game 68: 13 green, 10 blue, 7 red; 1 red, 15 green, 7 blue; 17 green, 14 red, 3 blue; 6 green, 8 blue, 6 red; 4 red, 3 blue, 5 green
Game 69: 1 red, 6 green, 3 blue; 3 red, 4 blue, 6 green; 2 blue, 2 red, 1 green; 6 blue, 9 green, 2 red; 5 green, 6 blue
Game 70: 1 green, 1 red, 3 blue; 2 green, 4 blue, 8 red; 5 red, 2 green, 3 blue; 3 green, 1 red, 3 blue; 3 green, 4 blue
Game 71: 11 blue, 13 green; 1 red, 11 green, 3 blue; 6 blue, 14 green, 1 red; 5 blue, 17 green
Game 72: 3 blue, 10 green, 4 red; 2 green, 6 red, 13 blue; 1 green, 1 blue, 6 red; 5 red, 1 blue, 1 green; 2 green, 5 red, 5 blue; 9 blue, 10 green, 6 red
Game 73: 6 red, 4 green, 1 blue; 1 blue, 5 red, 3 green; 2 red, 11 green, 3 blue
Game 74: 13 green, 2 red, 2 blue; 5 blue, 6 green; 12 green, 3 red, 4 blue; 2 green
Game 75: 9 red, 10 blue, 6 green; 12 blue, 9 red; 11 red, 6 green; 12 blue, 2 red, 1 green
Game 76: 1 green, 2 blue, 5 red; 2 blue, 1 green; 1 blue, 2 green, 1 red; 2 blue, 1 red; 3 green, 3 red
Game 77: 5 green, 12 blue, 3 red; 11 blue, 9 green, 13 red; 8 blue, 13 green, 13 red
Game 78: 2 red, 3 blue, 1 green; 1 green, 19 blue, 1 red; 7 blue, 2 green, 2 red
Game 79: 5 red, 1 blue, 4 green; 1 blue, 9 green, 10 red; 13 red, 1 green; 1 blue, 1 red, 5 green
Game 80: 13 green, 2 blue; 1 red, 4 blue, 13 green; 5 red, 7 green, 4 blue
Game 81: 3 red, 4 blue, 12 green; 16 green, 5 red, 1 blue; 4 blue, 2 red, 2 green; 4 blue, 5 red, 13 green; 8 red, 4 blue, 13 green; 16 green, 3 red
Game 82: 6 red, 3 green, 2 blue; 1 green, 6 red, 2 blue; 3 blue, 8 green, 9 red
Game 83: 3 green, 3 red, 1 blue; 3 blue, 4 green, 3 red; 3 blue, 4 green, 1 red; 2 red, 8 green, 2 blue
Game 84: 5 red, 6 blue, 3 green; 1 blue, 2 green; 3 green, 2 blue, 2 red; 1 red, 3 green, 6 blue; 12 red, 2 green; 4 blue, 2 green, 4 red
Game 85: 11 green, 4 blue, 9 red; 13 red, 1 blue, 11 green; 7 green, 8 blue, 7 red; 1 red, 4 blue
Game 86: 3 blue, 19 green, 7 red; 19 green, 1 red, 1 blue; 9 green, 2 red; 7 red, 6 green, 1 blue
Game 87: 1 blue, 1 green, 4 red; 1 green, 6 red; 6 red, 2 blue; 8 red, 3 blue
Game 88: 9 red, 6 blue; 4 red, 1 blue, 2 green; 1 green, 10 blue, 6 red; 2 blue, 1 green, 10 red; 7 red, 9 blue
Game 89: 3 blue, 15 green, 1 red; 1 red, 13 green, 3 blue; 4 blue, 14 green, 4 red; 10 green, 1 blue
Game 90: 1 red, 13 green; 3 green, 1 red, 5 blue; 5 blue, 6 green; 14 green, 4 blue; 3 blue, 10 green; 13 green, 1 red
Game 91: 13 green, 11 red, 4 blue; 14 red, 1 green, 10 blue; 4 red, 2 green, 3 blue
Game 92: 2 red, 3 blue, 6 green; 2 red, 2 blue, 8 green; 14 blue, 1 red, 1 green
Game 93: 15 blue, 2 red, 13 green; 8 green, 2 red, 8 blue; 6 blue, 1 red, 2 green
Game 94: 5 red, 4 green, 9 blue; 1 red, 5 green, 4 blue; 11 blue, 4 green, 2 red
Game 95: 9 blue, 3 green; 2 green, 12 blue; 10 green, 3 blue; 1 green, 1 red, 10 blue
Game 96: 4 blue, 2 red; 3 green, 10 blue, 7 red; 2 blue, 7 green, 1 red; 13 blue, 9 green; 10 blue, 4 green, 1 red
Game 97: 6 red, 4 green; 1 blue, 13 red; 3 green, 13 red
Game 98: 1 red, 13 blue, 1 green; 7 green, 5 blue, 3 red; 15 blue, 6 green; 4 blue, 5 green; 13 blue, 2 green, 1 red; 4 blue, 3 red, 2 green
Game 99: 1 red, 2 green; 2 red, 2 blue, 1 green; 3 green, 1 blue, 6 red; 3 red, 4 green; 5 red, 1 blue, 4 green; 1 blue, 2 red, 1 green
Game 100: 9 green, 2 blue, 12 red; 2 blue, 14 red, 2 green; 14 red, 12 green
"""
import re

num_red = 12
num_green = 13
num_blue = 14
# pattern = re.compile(r"Game (?P<x1>[0-9]+): (?P<y1>[0-9]+),(?P<x2>[0-9]+)-(?P<y2>[0-9]+)", re.IGNORECASE)
pattern = re.compile(r"Game (?P<x1>[0-9]+): (?P<text>)$", re.IGNORECASE)

def get_int_match(match, name):
    return int(match.group(name))

def parse_line(l):
    match = pattern.match(l)
    x1 = get_int_match(match, "x1")
    text = match.group("text")
    print(text)
    return x1, text

def get_green(l):
    try:
        return int(re.compile(r"(?P<color>[0-9]+) green").search(l).group("color"))
    except:
        return 0

def get_blue(l):
    try:
        return int(re.compile(r"(?P<color>[0-9]+) blue").search(l).group("color"))
    except:
        return 0

def get_red(l):
    try:
        return int(re.compile(r"(?P<color>[0-9]+) red").search(l).group("color"))
    except:
        return 0

def f2(x):
    count = 0
    x = x.strip('\n')
    for line_num, line in enumerate(x.splitlines()):
        text = line.split(":")[1]
        games = text.split(";")
        # print(games)
        rule_followed = True


        for game in games:
            game_blue = get_blue(game)
            game_red = get_red(game)
            game_green = get_green(game)
            # print(game_blue, game_red, game_green)
            if not (game_blue <= num_blue and game_red <= num_red and game_green <= num_green):
                rule_followed = False

        if rule_followed:
            count += (line_num + 1)

    return count

def f3(x):
    power = 0
    x = x.strip('\n')
    for line_num, line in enumerate(x.splitlines()):
        text = line.split(":")[1]
        games = text.split(";")
        # print(games)
        rule_followed = True

        game_red, game_green, game_blue = [], [], []
        for game in games:
            game_blue.append(get_blue(game))
            game_red.append(get_red(game))
            game_green.append(get_green(game))
        power_game = max(game_blue) * max(game_red) * max(game_green)

        power += power_game

    return power

print(f3(e))
print(f3(q))