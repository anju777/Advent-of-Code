import math
with open("5.txt", "r") as f:
    q = f.read()

e = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def get_middle_number(l: list):
    mid = len(l) // 2
    return l[mid]

def is_valid(numbers: list, rules_list: list):
    valid = True
    for i in range(len(numbers)):
        later_pages = numbers[i:]

        for later_page in later_pages:
            if (later_page, numbers[i]) in rules_list:
                valid = False
    return valid

def f(x: str):
    x = x.strip()
    orders, pages = x.split("\n\n")

    orders_list = []
    for order in orders.splitlines():
        int1, int2 = order.split("|")
        orders_list.append((int(int1), int(int2)))

    good_list = []
    bad_list = []
    for page in pages.splitlines():
        valid = True
        numbers = page.split(",")
        numbers = list(map(int, numbers))
        valid = is_valid(numbers)

        if valid:
            good_list.append(numbers, orders_list)
        else:
            bad_list.append(numbers)

    # Get middle numbers
    print(good_list)
    sum = 0
    for nums in good_list:
        sum += get_middle_number(nums)
    return sum

# print(f(e))
# print(f(q))

# Part 1:
# 4569

class Tree:
    def __init__(self, lower: int, upper: int | None = None, level: int = 0):
        self.head = lower
        self.children: list[Tree] = []
        self.level=level
        if upper:
            if isinstance(upper, Tree):
                self.children.append(upper)
            else:
                self.children.append(Tree(upper, level=level + 1))

    def has(self, item: int):
        for child in self.children:
            if child.has(item):
                return True
        return False

    def get_child(self, item: int):
        if self.head == item:
            return self

        for child in self.children:
            return child.get_child(item)

        assert False

    def pop_child(self, item: int):
        if self.head == item:
            return self

        for child in self.children:
            found = child.get_child(item)

        if found:
            self.children.remove(found)
            return found

        assert False

    def set_level(self, level: int):
        self.level = level

        for child in self.children:
            child.set_level(level + 1)

    def add(self, lower, upper):
        if self.has(upper):
            upper_tree = self.pop_child(upper)
        else:
            upper_tree = Tree(upper)

        if self.has(lower):
            for child in self.children:
                if child.head == lower and not child.has(upper):
                    if upper_tree:
                        upper_tree.set_level(child.level + 1)
                        child.children.append(upper_tree)
                    else:
                        child.children.append(Tree(lower=upper, level=child.level + 1))
                elif child.has(lower):
                    child.add(lower)

        else:
            upper_tree.set_level(self.level + 2)
            self.children.append(Tree(lower, upper_tree, self.level + 1))

    def __repr__(self) -> str:
        if not hasattr(self, "head"):
            for child in self.children:
                child.__repr__()
        ret = ""
        ret += "\t"*self.level + f"--> {self.head}\n"
        for child in self.children:
            ret += ("\t"*self.level + " | \n")
            ret += child.__repr__()
        return ret

    def __str__(self) -> str:
        if not hasattr(self, "head"):
            ret = ""
            for child in self.children:
                ret += child.__str__()
            return ret

        ret = ""
        ret += "\t"*self.level + f"--> {self.head}\n"
        for child in self.children:
            ret += ("\t"*self.level + " | \n")
            ret += child.__str__()
        return ret


class Base(Tree):
    def __init__(self):
        self.children = []
        self.level = 0

def sort_rules(rules: list):
    rules = list(map(list, rules))

    added = set()

    base = Base()

    for rule in rules:
        print(f"adding rule {rule}")
        base.add(rule[0], rule[1])
        print(base)
        print("---------------")

    print(base)
    import pdb; pdb.set_trace()

    # return sorted_list


def fix_bad_list(l: list, rules: list):
    # print(f"l: {l}, rules: {rules}")
    l_copy = l.copy()
    added = set()
    rules_set = set(rules)
    while not is_valid(l_copy, rules):
        for first, last in rules_set.difference(added):
            if first in l_copy and last in l_copy:
                first_i = l_copy.index(first)
                last_i = l_copy.index(last)
                if first_i > last_i:
                    l_copy.pop(first_i)
                    if last_i != 0:
                        l_copy.insert(last_i - 1, first)
                    else:
                        l_copy = [first] + l_copy
    return l_copy


def f2(x: str):
    x = x.strip()
    orders, pages = x.split("\n\n")

    rules = []
    for order in orders.splitlines():
        int1, int2 = order.split("|")
        rules.append((int(int1), int(int2)))

    good_list = []
    bad_list = []
    for page in pages.splitlines():
        valid = True
        numbers = page.split(",")
        numbers = list(map(int, numbers))

        for i in range(len(numbers)):
            later_pages = numbers[i:]

            for later_page in later_pages:
                if (later_page, numbers[i]) in rules:
                    valid = False

        if valid:
            good_list.append(numbers)
        else:
            bad_list.append(numbers)

    ordered_bad_lists = []
    for nums in bad_list:
        ordered_bad_lists.append(fix_bad_list(nums, rules))
    print(f"ORDERED: {ordered_bad_lists}\n")

    sum = 0
    # Get middle numbers
    for nums in ordered_bad_lists:
        sum += get_middle_number(nums)
    return sum

print(f2(e))
print(f2(q))


# 6456