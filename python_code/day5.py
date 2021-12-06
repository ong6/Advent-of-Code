import sys
import math
import numpy as np

def parse_data(line):
    start, end = line.split("->")
    x1, y1 = start.strip().split(",")
    x2, y2 = end.strip().split(",")
    return (int(x1), int(y1), int(x2), int(y2))

def sort_num(num1, num2):
    return (num1, num2) if num1 < num2 else (num2, num1)


def part1():
    data = sys.stdin.readlines()
    data = [x.strip() for x in data]

    grid = [[0 for _ in range(999)] for _ in range(999)]
    count = 0
    for i in data:
        x1, y1, x2, y2 = parse_data(i)
        if x1 == x2:
            y1, y2 = sort_num(y1, y2)
            for y in range(y1, y2 + 1): 
                grid[y][x1] += 1
                if grid[y][x1] == 2:
                    count += 1
        
        if y1 == y2:
            x1, x2 = sort_num(x1, x2)
            for x in range(x1, x2 + 1):
                grid[y1][x] += 1
                if grid[y1][x] == 2:
                    count += 1
                        

def part2():
    data = sys.stdin.readlines()
    data = [x.strip() for x in data]
    grid = [[0 for _ in range(999)] for _ in range(999)]
    count = 0

    for i in data:
        ox1, oy1, ox2, oy2 = parse_data(i)
        x1, x2 = sort_num(ox1, ox2)
        y1, y2 = sort_num(oy1, oy2)
        grad_check = math.atan2(oy2 - oy1, ox2 - ox1)

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x == x1 and x == x2) or (y == y1 and y == y2) :
                    grid[y][x] += 1
                    if grid[y][x] == 2:
                        count += 1

        diff = abs(ox1 - ox2) + 1
        if (grad_check == -(math.pi/4)):
            for i in range(diff):
                grid[oy1 - i][ox1 + i] += 1
                if grid[oy1 - i][ox1 + i] == 2:
                    count += 1
        if (grad_check == math.pi/4):
            for i in range(diff):
                grid[oy1 + i][ox1 + i] += 1
                if grid[oy1 + i][ox1 + i] == 2:
                    count += 1
        if (grad_check == (3 * math.pi/4)):
            for i in range(diff):
                grid[oy1 + i][ox1 - i] += 1
                if grid[oy1 + i][ox1 - i] == 2:
                    count += 1
        if (grad_check == -(3 * math.pi/4)):
            for i in range(diff):
                grid[oy1 - i][ox1 - i] += 1
                if grid[oy1 - i][ox1 - i] == 2:
                    count += 1
                
    print(count)

part2()