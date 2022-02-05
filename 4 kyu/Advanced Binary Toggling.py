# Description #
You are given a N x N grid of switches that are on (1) or off (0). The task is to activate all switches using a toggle operation.

Executing a toggle operation at coordinates (x, y) will toggle all switches in the row y and column x

import numpy as np
def toggle_row_col(grid, size, res):
    for y, row in enumerate(grid):
        for x, num in enumerate(row):
            if num == 0:
                res.extend([(index, y) for index in range(size)])
                res.extend([(x, index) for index in range(size) if index!=y])
    
def solve(grid):
    res = []
    size = len(grid)
    grid = np.array(grid)
    
    #case of grid with even dimensions
    #toggle each bit if 0
    if size == 0: return res
    if not size%2:
        toggle_row_col(grid, size, res)
    
    #case of grid with odd dimensions
    #consider the next (smaller) even board. Once solved, the whole board can be solved by considering the element at index (size-1,size-1)
    else:
        size-=1
        toggle_row_col(grid[:size, :size], size, res)
        if grid[size][size] == 0: res.append((size, size))
    
    return res
