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



def part2():
    data = sys.stdin.read().strip().split("\n")
    count = 0

    for i in data:
        front, back = i.split('|')
        front = front.split()
        back = back.split()

        mapping_dic = {}


        for num in front:
            unique_num = len(num)
            if unique_num == 2:
                mapping_dic["1"] = num
            elif unique_num == 3:
                mapping_dic["7"] = num
            elif unique_num == 4:
                mapping_dic["4"] = num
            elif unique_num == 7:
                mapping_dic["8"] = num

        for num in front:   
            unique_num = len(num)

            if unique_num == 5:
                partial_five = set(mapping_dic["4"]) - set(mapping_dic["7"])
                if set(mapping_dic["1"]).issubset(set(num)):
                    mapping_dic["3"] = num
                elif partial_five.issubset(set(num)):
                    mapping_dic["5"] = num
                else:
                    mapping_dic["2"] = num

            elif unique_num == 6:
                partial_zero = (set(mapping_dic["8"]) - set(mapping_dic["4"])) | set(mapping_dic["1"])
                if set(mapping_dic["4"]).issubset(set(num)):
                    mapping_dic["9"] = num
                elif partial_zero.issubset(set(num)):
                    mapping_dic["0"] = num
                else:
                    mapping_dic["6"] = num
            
        print(mapping_dic)

        for key, value in mapping_dic.items():
            for a, b in list(enumerate(back)):
                if set(value) ==  set(b):
                    back[a] = key

        output = "".join([str(i) for i in back])
        count += int(output)
        print(count)



part2()