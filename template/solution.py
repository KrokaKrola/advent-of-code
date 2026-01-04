import sys
from pathlib import Path


def parse_input(file_path: str):
    """
    Reads the input file and returns a list of lines or a processed structure.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} not found.")
        return None

    with open(path, "r") as f:
        # Toggle between .read(), .read().splitlines(), or .readlines()
        return f.read().splitlines()


def solve_part1(data) -> int:
    """
    Logic for Part 1 of the puzzle.
    """
    ans = 0
    # Your code here
    return ans


def solve_part2(data) -> int:
    """
    Logic for Part 2 of the puzzle (often requires optimization).
    """
    ans = 0
    # Your code here
    return ans


if __name__ == "__main__":
    # Use 'sample.txt' for testing logic, 'input.txt' for the final answer
    input_file = "sample.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    data = parse_input(input_file)

    if data:
        print(f"--- Part 1 ({input_file}) ---")
        print(f"Result: {solve_part1(data)}")

        print(f"\n--- Part 2 ({input_file}) ---")
        print(f"Result: {solve_part2(data)}")
