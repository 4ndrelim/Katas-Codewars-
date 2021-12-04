# Your task, is to create a NxN spiral with a given size
# Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

# Because of the edge-cases for tiny spirals, the size will be at least 5.
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.


import numpy as np
def spiralize(size):
    # Cycles every 4
    if size == 1:
        return [[1]]
    elif size == 2:
        return [[1,1],
                [0,1]]
    elif size == 3:
        return [[1,1,1],
                [0,0,1],
                [1,1,1]]
    elif size == 4:
        return [[1,1,1,1],
                [0,0,0,1],
                [1,0,0,1],
                [1,1,1,1]]
        
    arr = np.array(spiralize(size-4))
    arr = np.pad(arr, ((1,1),(1,1)), 'constant')
    arr[1][0] = 1
    arr = np.pad(arr, ((1,1),(1,1)), 'constant', constant_values = 1)
    arr[1][0] = 0
    return arr.tolist()
