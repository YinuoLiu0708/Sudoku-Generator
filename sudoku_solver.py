"""Solve Sudoku through backtracking"""
import random




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
    return None
    
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
    blank = find_empty(bo)
    if not blank:
        return True
    else:
        # blankCell records (row, col)
        row,col = blank

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i
        
            if solve(bo):
                return True
            bo[row][col] = 0
    
    return False

def find_empty(bo):
# return the place of blank cell
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)
        
    return None

def valid(bo,num,pos):
    # Check row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check coloumn
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check square
    # Find which square the blank cell lays
    square_x = pos[0] // 3
    square_y = pos[1] // 3

    for i in range(square_x*3, square_x*3+3):
        for j in range(square_y*3,square_y*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True
        
def generate():
# Generate a sudoku (blank cell: 35-50)
    board = [[0 for x in range(9)] for x in range(9)]
    randomboard(board)
    solve(board)

    n = random.randint(35,50)
    i = 0
    while i < n:
        board[random.randint(0,8)][random.randint(0,8)] = 0
        i += 1
    return board