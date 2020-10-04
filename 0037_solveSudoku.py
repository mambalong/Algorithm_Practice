digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def isValid(board, r, c, num):
    for i in range(9):
        # column
        if board[i][c] == num:
            print('c')
            return False
        # row
        if board[r][i] == num:
            print('r')
            return False
        # grid
        if board[r//3*3+i//3][c//3*3+i%3] == num:
            print('g')
            return False
    return True

def backtrack(board, r, c):
    # reach the end of a row, row + 1
    if c == 9:
        return backtrack(board, r+1, 0)
    # base case, we find the solution
    if r == 9:
        return True
    # there is already a digit at (r, c)
    print(r,c)
    if board[r][c] != '.':
        return backtrack(board, r, c+1)
    
    for num in digits:
        # if the num cannot be here, continue
        if not isValid(board, r, c, num):
            continue
        board[r][c] = num
        if backtrack(board, r, c+1):
            return True
        board[r][c] = '.'
    return False


def solveSudoku(board):
    backtrack(board, 0, 0)
    print(board)

board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
# for d in digits:
#     print(d, '+', isValid(board, 0, 2, d))
solveSudoku(board)
