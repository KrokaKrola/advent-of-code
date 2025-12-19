import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
absolute_file_path = os.path.join(script_dir, file_name)

ranges: list[list[int]] = []
ids: list[int] = []

with open(absolute_file_path) as f:
    data = f.read().strip().split("\n")
    isRanges = True
    for row in data:
        if row == "":
            isRanges = False
            continue

        if isRanges:
            fromR, toR = row.split("-")
            ranges.append([int(fromR), int(toR)])
        else:
            ids.append(int(row))


def solution1():
    fresh_ids = []
    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                fresh_ids.append(id)
                break
    print(len(fresh_ids))


def solution2():
    ranges.sort(key=lambda x: x[0])

    new_ranges = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        _, last_end = new_ranges[-1]

        if current_start <= last_end:
            new_ranges[-1][1] = max(last_end, current_end)
        else:
            new_ranges.append([current_start, current_end])

    total = 0
    for r in new_ranges:
        total += r[1] - r[0] + 1

    print(total)


# solution1()
solution2()
