import sys

def part1():
    data = sys.stdin.read().strip().split("\n")
    print(data)


    count = 0


    for i in data:
        front, back = i.split('|')
        front = front.split()
        back = back.split()

        for num in back:

            unique_num = len(num)

            if unique_num == 2 or unique_num == 3 or unique_num == 4 or unique_num == 7:
                count += 1
            

        print(front, back)
    print(count)


part1()