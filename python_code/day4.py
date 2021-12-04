import sys
import copy

# given a 5 by 5 board, find if there is a row or column with all the same number
def win_check(board):

    for i in range(5):
        for j in range(5):
            if len(set(board[i])) == 1:
                return True
            if len(set([row[j] for row in board])) == 1:
                return True
    return False

def calculate_score(board):
    score = 0
    for row in board:
        for num in row:
            if num != "x":
                score += int(num)
    return score


def part1():
    data = sys.stdin
    input_numbers = data.readline().strip().split(",")
    bingo_boards = []

    count = 0
    temp_board = []

    for line in data:
        line = line.strip().split()
        if line != []:
            temp_board.append(line)
            count += 1
        if count % 5 == 0:
            if temp_board != []:
                bingo_boards.append(temp_board)
            temp_board = []
            count = 0
        
    print(input_numbers)
    print(bingo_boards)
    
    for num in input_numbers:
        for board in bingo_boards: 
            for i in range(5):
                for j in range(5):
                    if num == board[i][j]:
                        board[i][j] = "x"
            if win_check(board) == True:
                print(board)
                print(num)
                return calculate_score(board) * int(num)
                 
def part2():
    data = sys.stdin
    input_numbers = data.readline().strip().split(",")
    bingo_boards = []

    count = 0
    indentity = 0
    temp_board = []

    for line in data:
        line = line.strip().split()
        if line != []:
            temp_board.append(line)
            count += 1
        if count % 5 == 0:
            if temp_board != []:
                bingo_boards.append([temp_board, indentity])
                indentity += 1
            temp_board = []
            count = 0
        

    winning_boards = []
    indentity_lst = []

    for num in input_numbers:
        for board in bingo_boards: 

            board, indentity = board

            for i in range(5):
                for j in range(5):
                    if num == board[i][j]:
                        board[i][j] = "x"


            if indentity in indentity_lst:
                continue
            elif win_check(board) == True:
                winning_boards.append([copy.deepcopy(board), num])
                indentity_lst.append(indentity)

            

    lastboard = winning_boards[-1]
    print(winning_boards)
    
    return calculate_score(lastboard[0]) * int(lastboard[1])        


print(part2())