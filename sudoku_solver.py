"""Solve Sudoku through backtracking"""
import random

# create a blank board consisting of 0
board = [[0 for x in range(9)] for x in range(9)]


def randomboard(bo):
    choice1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    pos1 = random.choice(choice1)
    bo[pos1[0]][pos1[1]] = random.randint(1,10)
    choice2 = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
    pos2 = random.choice(choice2)
    bo[pos2[0]][pos2[1]] = random.randint(1,10)
    choice3 = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]
    pos3 = random.choice(choice3)
    bo[pos3[0]][pos3[1]] = random.randint(1,10)
    return bo
    
def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(9):
            if j % 3 == 0 and j != 0: 
                print(" | ", end="" )
            
            if j == 8:
                print(bo[i][j])  
            else:
                print(str(bo[i][j]) + " ", end="")
            

def solve(bo):
    find = find_empty(bo)


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)
        
    return None

board = randomboard(board)
print_board(board)
