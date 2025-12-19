import os

script_dir = os.path.dirname(__file__)
file_name = "input.txt"
absolute_file_path = os.path.join(script_dir, file_name)

with open(absolute_file_path) as f:
    data = f.read().strip()

input = data.split(",")


def solution1() -> None:
    invalidIds: list[int] = []

    for inputRange in input:
        frStr, toStr = inputRange.split("-")

        fromNum = int(frStr)
        toNum = int(toStr)

        for num in range(fromNum, toNum + 1):
            numAsStr = str(num)
            size = len(numAsStr)
            # skip non odd numbers
            if size % 2 != 0:
                continue

            middleOfTheNumberIdx = int(size / 2)

            if numAsStr[0:middleOfTheNumberIdx] == numAsStr[middleOfTheNumberIdx:]:
                invalidIds.append(num)

    result = sum(invalidIds)
    print(result)


def isInvalidId(id: int) -> bool:
    idAsStr = str(id)
    strLength = len(idAsStr)

    # We only need to check possible repeating sequences up to half the string length.
    # The length of the repeating unit (period) 'l' must be a divisor of 'n'.
    for unitLength in range(1, strLength // 2 + 1):
        # 1. Check if the string length 'n' is perfectly divisible by the potential unit length
        if strLength % unitLength == 0:
            # 2. Extract the potential repeating unit
            repeating_unit = idAsStr[:unitLength]

            # 3. Check if the entire string can be reconstructed by repeating this unit.
            repetitions = strLength // unitLength

            if repeating_unit * repetitions == idAsStr:
                return True

    return False


def solution2() -> None:
    invalidIds: list[int] = []

    for inputRange in input:
        frStr, toStr = inputRange.split("-")

        fromNum = int(frStr)
        toNum = int(toStr)

        for num in range(fromNum, toNum + 1):
            if isInvalidId(num):
                print(f"invalid num = {num}")
                invalidIds.append(num)

    result = sum(invalidIds)
    print(result)


def solution2_1() -> None:
    max_boundary = 0

    for inputRange in input:
        _, to_str = inputRange.split("-")
        if int(to_str) > max_boundary:
            max_boundary = int(to_str)

    invalid_ids = set()

    max_boundary_len = len(str(max_boundary))

    for num in range(1, max_boundary + 1):
        num_len = len(str(num))

        if int(str(num) * 2) > max_boundary:
            break

        for i in range(2, max_boundary_len // num_len + 1):
            invalid_ids.add(int(str(num) * i))

    ids: list[int] = []

    for inputRange in input:
        frStr, toStr = inputRange.split("-")

        fromNum = int(frStr)
        toNum = int(toStr)

        for i in range(fromNum, toNum + 1):
            if i in invalid_ids:
                ids.append(i)

    print(sum(ids))


# solution1()
# solution2()
solution2_1()
