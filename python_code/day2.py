import sys

def day1():
    data = sys.stdin.read().splitlines()

    x_range = 0
    y_range = 0

    # split data into command and number
    for line in data:
        command, number = line.split()
        number = int(number)

        if command == "forward":
            x_range += number
        if command == "backward":
            x_range -= number
        if command == "up":
            y_range -= number
        if command == "down":
            y_range += number

    print(x_range * y_range)

def day2():
    data = sys.stdin.read().splitlines()

    horizontal = 0
    depth = 0
    aim = 0

    # split data into command and number
    for line in data:
        command, x = line.split()
        x = int(x)

        if command == "forward":
            horizontal += x
            depth += aim * x
        if command == "backward":
            horizontal -= x
        if command == "up":
            aim -= x
        if command == "down":
            aim += x
            
    print(horizontal * depth)

day2()
