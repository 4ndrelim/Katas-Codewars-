# Description # Simpler version of Sudoku Validator kata

# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. 
# The cells of the sudoku board may also contain 0's, which will represent empty cells. 
# Boards containing one or more zeroes are considered to be invalid solutions.

# Note: The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9


def valid_solution(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return False
            for k in range(9):
                if board[r][k] == board[r][c] and k != c: #check the rth row
                    return False
                if board[k][c] == board[r][c] and k != r: #check the cth col
                    return False
                
            #check grid
            for i in range(3):
                for j in range(3):
                    c_r = r//3 * 3 + i
                    c_c = c//3 * 3 + j
                    if board[c_r][c_c] == board[r][c] and (c_r != r or c_c != c):
                        return False
    return True
