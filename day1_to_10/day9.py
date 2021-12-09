import sys
import fileinput


def part1():
    f = open("day9.txt", "r")
    data = f.read().split()
    f.close()
    new_data = []
    for i in data:
        new_data.append([int(x) for x in i])

    data = new_data
    grid_size = len(data)
    low_points = []

    for row in range(grid_size):
        for col in range(grid_size):
            point = data[row][col] 
            try:
                is_low_right = point < data[row][col + 1]
            except IndexError:
                is_low_right = True
            try:
                is_low_left = point < data[row][col - 1]
            except IndexError:
                is_low_left = True
            try:
                is_low_top = point < data[row + 1][col]
            except IndexError:
                is_low_top = True
            try:
                is_low_bot = point < data[row - 1][col]
            except IndexError:
                is_low_bot = True
            
            if is_low_bot and is_low_top and is_low_left and is_low_right:
                low_points.append(point + 1)
            
           
    print(sum(low_points))



def part2():
    f = open("day9.txt", "r")
    data = f.read().split()
    f.close()
    new_data = []
    new_data.append([9 for x in range(len(data[0]) + 2)])
    for i in data:
        temp = [int(x) for x in i]
        new_data.append([9] + temp + [9])
    new_data.append([9 for x in range(len(data[0]) + 2)])

    data = new_data
    row_size = len(data)
    col_size = len(data[0])
    low_points = []

    for row in range(row_size):
        for col in range(col_size):
            point = data[row][col] 
            try:
                is_low_right = point < data[row][col + 1]
            except IndexError:
                is_low_right = True
            try:
                is_low_left = point < data[row][col - 1]
            except IndexError:
                is_low_left = True
            try:
                is_low_top = point < data[row + 1][col]
            except IndexError:
                is_low_top = True
            try:
                is_low_bot = point < data[row - 1][col]
            except IndexError:
                is_low_bot = True
            
            if is_low_bot and is_low_top and is_low_left and is_low_right:
                low_points.append((row, col))

    cords_lst = []

    def neighbor_check(row, col, count):
        curr = data[row][col]
        data[row][col] = 9
        cords_lst.append((row, col))

        if  9 != data[row][col + 1] :
            neighbor_check(row, col + 1, count + 1)
        if  9 != data[row][col - 1]:
            neighbor_check(row, col - 1, count + 1)
        if  9 != data[row + 1][col]:
            neighbor_check(row + 1, col, count + 1)
        if  9 != data[row - 1][col]:
            neighbor_check(row - 1, col, count + 1)

    results = []   
    for row, col in low_points:    
        neighbor_check(row, col, 0)    
        results.append(len(cords_lst))
        cords_lst = []

    results.sort()
    print(results[-1] * results[-2] * results[-3])

    return results[1]

part2()


    # def neighbor_check(row, col, count):
    #     curr = data[row][col]
    #     print(curr, row, col)
    #     cords_lst.append((row, col))

    #     try:
    #         temp_right = data[row][col + 1] 
    #         is_nine_right = 9 == temp_right or (row, col+1) in cords_lst
    #     except IndexError:
    #         is_nine_right = True
    #     try:
    #         temp_left = data[row][101 if (col - 1) < 0 else col - 1]
    #         is_nine_left = 9 == temp_left or (row, 101 if (col - 1) < 0 else col - 1) in cords_lst
    #     except IndexError:
    #         is_nine_left = True
    #     try:
    #         temp_top = data[row + 1][col]
    #         is_nine_top = 9 == temp_top or (row + 1, col) in cords_lst
    #     except IndexError:
    #         is_nine_top = True
    #     try:
    #         temp_bot = data[101 if (row - 1) < 0 else row - 1][col]
    #         is_nine_bot = 9 == temp_bot or (101 if (row - 1) < 0 else row - 1, col) in cords_lst
    #     except IndexError:
    #         is_nine_bot = True

    #     if not is_nine_bot:
    #         return neighbor_check(row - 1, col, count + 1)
    #     if not is_nine_top:
    #         return neighbor_check(row + 1, col, count + 1)
    #     if not is_nine_right: 
    #         return neighbor_check(row, col + 1, count + 1)
    #     if not is_nine_left: 
    #         return neighbor_check(row, col - 1, count + 1)


    # print(neighbor_check(0, 9, 0))


    # print(data)
    # for row, col in low_points:
    #     print(row, col)
    #     num = neighbor_check(row, col, 0)
    #     out.append(num)

    # print(out)

