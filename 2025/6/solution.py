import math
import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
absolute_file_path = os.path.join(script_dir, file_name)

with open(absolute_file_path) as f:
    lines = f.read().strip().split("\n")

    temp_data = [line.split() for line in lines]

    data = list(zip(*temp_data))


def solution_1():
    total = 0

    for col in data:
        operator = col[-1]

        numbers = [int(n) for n in col[:-1]]

        if operator == "+":
            total += sum(numbers)
        elif operator == "*":
            total += math.prod(numbers)

    print(total)


def solution_2():
    with open(absolute_file_path) as f:
        lines = f.read().splitlines()

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]

    raw_columns = list(zip(*padded_lines))

    total = 0
    sub_total = 0
    operator = "+"

    for col in raw_columns:
        if all(c == " " for c in col):
            total += sub_total
            sub_total = 0
            continue

        if col[-1] == "*":
            operator = "*"
            sub_total = 1
        elif col[-1] == "+":
            operator = "+"
            sub_total = 0

        number = int("".join(list(col[:-1])))

        if operator == "+":
            sub_total += number
        elif operator == "*":
            sub_total *= number

    total += sub_total

    print(total)


# solution_1()
solution_2()
