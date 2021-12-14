# Incomplete

def solve(board):
    row = [[False for _ in range(9)] for _ in range(9)]
    col = [[False for _ in range(9)] for _ in range(9)]
    grid = [[False for _ in range(9)] for _ in range(9)]
    for idx in range(81):
        i = idx//9
        j = idx%9
        num = board[i][j]
        if num != 0:
            row[i][num-1], col[j][num-1], grid[i//3 * 3 + j//3][num-1] = True, True, True
    
    def fill_board(index):
        if index > 80:
            return board
        i = index//9
        j = index%9
        if board[i][j] != 0:
            return fill_board(index+1)
        for num in range(9):
            if row[i][num] or col[j][num] or grid[i//3 * 3 + j//3][num]:
                continue
            board[i][j] = num+1
            row[i][num], col[j][num], grid[i//3 * 3 + j//3][num] = True, True, True 
            if fill_board(index+1):
                return board
            board[i][j] = 0
            row[i][num], col[j][num], grid[i//3 * 3 + j//3][num] = False, False, False
        return False
    
    return fill_board(0)
