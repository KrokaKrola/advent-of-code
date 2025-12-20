import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
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


solution_1()
