import os

script_dir = os.path.dirname(__file__)
file_name = "input-test.txt"
absolute_file_path = os.path.join(script_dir, file_name)

with open(absolute_file_path) as f:
    data = [list(row) for row in f.read().strip().split("\n")]


def solution_1():
    beam_enter_idx = data[0].index("S")

    data[1][beam_enter_idx] = "|"
    total_beams = 0

    for idx in range(2, len(data)):
        for col_idx in range(len(data[idx])):
            if data[idx][col_idx] == "^" and data[idx - 1][col_idx] == "|":
                data[idx][col_idx - 1] = "|"
                data[idx][col_idx + 1] = "|"
                total_beams += 1
            if data[idx - 1][col_idx] == "|" and data[idx][col_idx] != "^":
                data[idx][col_idx] = "|"

    for it in data:
        print("".join(it))

    print(total_beams)


def solution_1_1():
    active_columns = {data[0].index("S")}

    total_beams = 0
    height = len(data)
    width = len(data[0])

    for r in range(1, height):
        next_active_columns = set()

        for c in active_columns:
            char = data[r][c]

            if char == "^":
                total_beams += 1

                if c - 1 >= 0:
                    next_active_columns.add(c - 1)

                if c + 1 < width:
                    next_active_columns.add(c + 1)
            else:
                next_active_columns.add(c)

        active_columns = next_active_columns

        if not active_columns:
            break

    print(total_beams)


solution_1_1()
