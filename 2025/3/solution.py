import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
absolute_file_path = os.path.join(script_dir, file_name)

with open(absolute_file_path) as f:
    data = f.read().strip().split("\n")


def solution1() -> None:
    joltages: list[int] = []

    for bank in data:
        max_lp_idx = 0

        for i in range(0, len(bank) - 1):
            if bank[i] == "9":
                max_lp_idx = i
                break

            if bank[i] > bank[max_lp_idx]:
                max_lp_idx = i

        max_rp_idx = max_lp_idx + 1

        for i in range(max_rp_idx, len(bank)):
            if bank[i] == "9":
                max_rp_idx = i
                break

            if bank[i] > bank[max_rp_idx]:
                max_rp_idx = i

        joltages.append(int(bank[max_lp_idx] + bank[max_rp_idx]))

    print(sum(joltages))


def solution2() -> None:
    joltages: list[int] = []

    for bank in data:
        joltage = ""
        lts_idx = 0

        while len(joltage) < 12:
            max_idx = lts_idx

            remaining_needed = 12 - len(joltage)
            search_limit = len(bank) - remaining_needed + 1

            for i in range(lts_idx, search_limit):
                if bank[i] == "9":
                    max_idx = i
                    break

                if bank[i] > bank[max_idx]:
                    max_idx = i

            joltage += bank[max_idx]
            lts_idx = max_idx + 1

        joltages.append(int(joltage))

    print(sum(joltages))


# solution1()
solution2()
