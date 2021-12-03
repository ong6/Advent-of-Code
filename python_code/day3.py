import sys
import copy

def part1():
    data = sys.stdin.read().splitlines()
    binary_count = [0 for i in data[0]]

    for j in range(len(data[0])):
        for i in data:
            binary_count[j] += int(i[j])

    bitlen = len(data)/2
    gamma = ""
    epsilon = ""

    for i in binary_count:
        if i > bitlen:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))

def part2():
    data = sys.stdin.read().splitlines()

    oxygen_data = copy.deepcopy(data)
    co2_data = copy.deepcopy(data)


    for j in range(len(data[0])):
        oxy_count = 0 
        for i in oxygen_data:
            if i[j] == "1":
                oxy_count += 1

        if oxy_count >= len(oxygen_data)/2:
            oxygen_data = list(filter(lambda x: x[j] == "1", oxygen_data))
        else:
            oxygen_data = list(filter(lambda x: x[j] == "0", oxygen_data))
        
        co2_count = 0
        for i in co2_data:
            if i[j] == "0":
                co2_count += 1
        
        if len(co2_data) == 1:
            pass
        elif co2_count <= len(co2_data)/2:
            co2_data = list(filter(lambda x: x[j] == "0", co2_data))
        else:
            co2_data = list(filter(lambda x: x[j] == "1", co2_data))

        print(oxygen_data,co2_data)


    print(int(oxygen_data[0], 2) * int(co2_data[0], 2))

part2()