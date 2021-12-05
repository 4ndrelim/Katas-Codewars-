# Description # 
# Write a function that will solve a 9x9 Sudoku puzzle. 
# The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square


def sudoku(puzzle): # Naive sudoku solver (Brute force approach)
    def is_safe(coord, num):
        r,c = coord
        for k in range(9): #check rth row
            if puzzle[r][k] == num:
                return False
            if puzzle[k][c] == num: #check cth col
                return False 
        #check grid
        for i in range(3):
            for j in range(3):
                c_r, c_c = r//3*3+i, c//3*3+j
                if puzzle[c_r][c_c] == num:
                    return False
        return True
    empty_pos = []
    def find_empty():
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    empty_pos.append((i,j))
    
    find_empty()
    
    def helper():
        if not empty_pos:
            return puzzle
        curr = empty_pos.pop()
        for k in range(1,10):
            if is_safe(curr, k):
                puzzle[curr[0]][curr[1]] = k
                if helper():
                    return puzzle
                puzzle[curr[0]][curr[1]] = 0
        empty_pos.append(curr)
        return False
    return helper()
