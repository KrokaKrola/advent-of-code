import sys
from pathlib import Path


def parse_input(file_path: str):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} not found.")
        return None

    with open(path, "r") as f:
        return f.read().splitlines()


def solve_part1(data: list[str]) -> int:
    ans = 0

    for el in data[0]:
        if el == "(":
            ans += 1
        else:
            ans -= 1

    return ans


def solve_part2(data: list[str]) -> int:
    ans = 0
    k = 0

    for el in data[0]:
        if el == "(":
            ans += 1
        else:
            ans -= 1

        k += 1

        if ans == -1:
            break

    return k


if __name__ == "__main__":
    input_file = "sample.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    script_dir = Path(__file__).parent
    input_path = script_dir / input_file

    data = parse_input(input_path)

    if data:
        print(f"--- Part 1 ({input_file}) ---")
        print(f"Result: {solve_part1(data)}")

        print(f"\n--- Part 2 ({input_file}) ---")
        print(f"Result: {solve_part2(data)}")
