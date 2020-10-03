'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.


'''

res = []

def isValid(board, row, col):
    n = len(board)
    # check above
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # check left top
    i, j, step= row, col, min(row, col)
    while step > 0:
        i -= 1
        j -= 1
        if board[i][j] == 'Q':
            return False
        step -= 1
    # check right top
    i, j, step= row, col, min(row, n-1-col)
    while step > 0:
        i -= 1
        j += 1
        if board[i][j] == 'Q':
            return False
        step -= 1
    
    return True
    
def generate_board(board):
    n = len(board)
    new_board = []
    for i in range(n):
        new_board.append(''.join(board[i]))

    return new_board

def backtrack(board, row):
    if row == len(board):
        res.append(generate_board(board))
        return
    for col in range(len(board)):
        if not isValid(board, row, col):
            continue
        print(row, col)
        board[row][col] = 'Q'
        backtrack(board, row + 1)
        board[row][col] = '.'

def solveNQueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return res

print(solveNQueens(4))


    

