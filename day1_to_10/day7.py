import sys
import statistics

def part1():
    data = sys.stdin.read().split(",")
    data = [int(x) for x in data]
    median = statistics.median(data)
    mean = statistics.mean(data)
    
    count = 0 
    for i in data:
        count += abs(i - median)

    print(count)

def part2():
    data = sys.stdin.read().split(",")
    data = [int(x) for x in data]
    mean = int(statistics.mean(data))
    count = 0 

    for i in data:
        n = abs(i - mean)
        summation = (n * (n +1))/2
        count += summation

    print(count)

part2()