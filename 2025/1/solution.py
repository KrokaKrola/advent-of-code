with open("./input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")


def solution1():
    password = 0
    dial = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        distance = distance % 100

        if direction == "R":
            dial += distance
        elif direction == "L":
            dial -= distance

        dial = dial % 100

        if dial == 0:
            password += 1

        print(f"The dial is rotated {direction}{distance} to point at {dial}")

    print(f"Password is {password}")


def solution2():
    password = 0
    dial = 50

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        password += distance // 100

        remainder = distance % 100

        if remainder > 0:
            if direction == "R":
                # Check if we wrap around 99 -> 0
                if dial + remainder >= 100:
                    password += 1
            elif direction == "L":
                # We only score if we didn't start at 0, and the move is big enough to hit 0
                if dial > 0 and remainder >= dial:
                    password += 1

        if direction == "R":
            dial = (dial + remainder) % 100
        else:
            dial = (dial - remainder) % 100

    print(password)


solution2()
