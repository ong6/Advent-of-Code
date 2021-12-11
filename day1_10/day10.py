import statistics

def part1():
    f = open("day10.txt", "r")
    data = f.read().split()

    expected = []
    for bracket in data:
        stack = []
        for i in bracket:
            if i == '[' or i == '{' or i == '(' or i == '<':
                stack.append(i)
            else:
                temp = stack.pop()
                if i == ']' and temp != '[':
                    expected.append(i)
                    break
                if i == '}' and temp != '{':
                    expected.append(i)
                    break
                if i == ')' and temp != '(':
                    expected.append(i)
                    break
                if i == '>' and temp != '<':
                    expected.append(i)
                    break

    print(expected) 

    count = 0
    for i in expected:
        if i == ')':
            count += 3
        if i == ']':
            count += 57
        if i == '}':
            count += 1197
        if i == '>':
            count += 25137

    print(count)

def part2():
    f = open("day10.txt", "r")
    data = f.read().split()

    to_remove = []

    for bracket in data:
        stack = []
        for i in bracket:
            if i == '[' or i == '{' or i == '(' or i == '<':
                stack.append(i)
            else:
                temp = stack.pop()
                if i == ']' and temp != '[':
                    to_remove.append(bracket)
                    break
                if i == '}' and temp != '{':
                    to_remove.append(bracket)
                    break
                if i == ')' and temp != '(':
                    to_remove.append(bracket)
                    break
                if i == '>' and temp != '<':
                    to_remove.append(bracket)
                    break
    
    new = [x for x in data if x not in to_remove]
    incomplete_list = []
    for bracket in new:
        stack = []
        for i in bracket:
            if i == '[' or i == '{' or i == '(' or i == '<':
                stack.append(i)
            else:
                temp = stack.pop()
                if i == ']' and temp == '[' or i == '}' and temp == '{' or i == ')' and temp == '(' or i == '>' and temp == '<':
                    continue
        incomplete_list.append(stack)
    
    results = []
    for stack in incomplete_list:
        score = 0
        for i in stack[::-1]:
            score *= 5
            if i == '[':
                score += 2
            if i == '{':
                score += 3
            if i == '(':
                score += 1
            if i == '<':
                score += 4
        results.append(score)

    print(statistics.median(results))


part2()