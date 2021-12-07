import sys

def part1(days):
    data = sys.stdin.read().split(",")
    data = [int(x) for x in data]

    for _ in range(days):
        for i in range(len(data)):
            data[i] -= 1
            if data[i] == -1:
                data[i] = 6
                data.append(8)
        

    print(len(data))


def part2(days):
    data = sys.stdin.read().split(",")
    data = [int(x) for x in data]

    fish_dict = {0:0, 1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

    for i in data:
        fish_dict[i] += 1

    for _ in range(days):
        new_fish = fish_dict[0]
        for i in range(1,9):
            fish_dict[i-1] = fish_dict[i]
        fish_dict[8] = 0
        fish_dict[8] += new_fish
        fish_dict[6] += new_fish
        
    count = 0
    for k, v in fish_dict.items():
        count += v
    
    print(count)

part2(256)