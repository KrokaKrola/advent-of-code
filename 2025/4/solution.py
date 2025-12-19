import os
from collections import deque

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
absolute_file_path = os.path.join(script_dir, file_name)

with open(absolute_file_path) as f:
    data = f.read().strip().split("\n")

grid = [list(row) for row in data]

ROLL_OF_PAPER_SYMBOL = "@"

surroundings = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]


def count_neighbors(rowIdx, colIdx) -> int:
    numOfRolls = 0

    for el in surroundings:
        rowOffset, colOffset = el

        rowIdxWithOffset = rowIdx + rowOffset
        colIdxWithOffset = colIdx + colOffset

        if (
            colIdxWithOffset < 0
            or rowIdxWithOffset < 0
            or rowIdxWithOffset > len(grid) - 1
            or colIdxWithOffset > len(grid[rowIdx]) - 1
        ):
            continue

        if grid[rowIdxWithOffset][colIdxWithOffset] == ROLL_OF_PAPER_SYMBOL:
            numOfRolls += 1

    return numOfRolls


def solution1() -> None:
    accesseblePaperRollsCoords: list[list[int]] = []

    for rowIdx in range(0, len(grid)):
        for colIdx in range(0, len(grid[rowIdx])):
            el = grid[rowIdx][colIdx]

            if el != ROLL_OF_PAPER_SYMBOL:
                continue

            numOfRolls = count_neighbors(rowIdx, colIdx)

            if numOfRolls < 4:
                accesseblePaperRollsCoords.append([rowIdx, colIdx])

    print(len(accesseblePaperRollsCoords))


# brute force
def solution2() -> None:
    removableRolls = 0

    while True:
        accesseblePaperRollsCoords: list[list[int]] = []

        for rowIdx in range(0, len(grid)):
            for colIdx in range(0, len(grid[rowIdx])):
                el = grid[rowIdx][colIdx]

                if el != ROLL_OF_PAPER_SYMBOL:
                    continue

                numOfRolls = count_neighbors(rowIdx, colIdx)

                if numOfRolls < 4:
                    accesseblePaperRollsCoords.append([rowIdx, colIdx])

        if len(accesseblePaperRollsCoords) > 0:
            removableRolls += len(accesseblePaperRollsCoords)

            for idx in range(0, len(accesseblePaperRollsCoords)):
                grid[accesseblePaperRollsCoords[idx][0]][
                    accesseblePaperRollsCoords[idx][1]
                ] = "x"
        else:
            break

    print(removableRolls)


def get_neighbors(rowIdx, colIdx) -> list[list[int]]:
    neighbors = []

    for el in surroundings:
        rowOffset, colOffset = el

        rowIdxWithOffset = rowIdx + rowOffset
        colIdxWithOffset = colIdx + colOffset

        if (
            colIdxWithOffset < 0
            or rowIdxWithOffset < 0
            or rowIdxWithOffset > len(grid) - 1
            or colIdxWithOffset > len(grid[rowIdx]) - 1
        ):
            continue

        neighbors.append((rowIdxWithOffset, colIdxWithOffset))

    return neighbors


def solution2_1():
    rows = len(grid)
    cols = len(grid[0])
    to_remove = deque()
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ROLL_OF_PAPER_SYMBOL and count_neighbors(r, c) < 4:
                to_remove.append((r, c))
                visited.add((r, c))

    removed_count = 0

    while len(to_remove) > 0:
        r, c = to_remove.popleft()

        if grid[r][c] == ROLL_OF_PAPER_SYMBOL:
            grid[r][c] = "x"
            removed_count += 1

        neighbors = get_neighbors(r, c)
        for rn, cn in neighbors:
            if grid[rn][cn] == ROLL_OF_PAPER_SYMBOL:
                if count_neighbors(rn, cn) < 4 and (rn, cn) not in visited:
                    to_remove.append((rn, cn))
                    visited.add((rn, cn))

    print(removed_count)


# solution1()
# solution2()
solution2_1()
