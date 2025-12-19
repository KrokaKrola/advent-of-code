import math
import os

script_dir = os.path.dirname(__file__)
file_name = "input-test.txt"
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
    total = 0

    for col in data:
        operator = col[-1]

        print(col[:-1])


# solution_1()
solution_2()
