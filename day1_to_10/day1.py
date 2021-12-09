import sys


def part1():
    data = sys.stdin.read().splitlines()
    int_list = list(map(int, data))

    count = 0
    prev_num = int_list[0]

    for i in int_list[1:]:
        if (i > prev_num):
            count += 1;
        prev_num = i
        

    print(len(int_list))
    print(count)


def part2():
    data = sys.stdin.read().splitlines()
    int_list = list(map(int, data))

    count = 0
    window_1 = 0
    window_2 = 0


    for i, x in enumerate(int_list[:-3]):
        window_1 = int_list[i] + int_list[i + 1] + int_list[i + 2]
        window_2 = int_list[i + 1] + int_list[i + 2] + int_list[i + 3]

        if (window_1 < window_2):
            count += 1;
        

    print(len(int_list))
    print(count)


part2()

