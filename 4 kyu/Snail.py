# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]


import numpy as np
def snail(snail_map):
    ret = []
    map = np.array(snail_map)
    while len(map) > 0:
        ret.extend(map[0].tolist())
        map = np.rot90(map[1:])
    return ret
  
  
 #old sol
def snail_old(snail_map):
    sorted_list = []
    while snail_map:
        #append top row
        top = snail_map.pop(0)
        sorted_list.extend(top)
        
        if len(snail_map) !=0:
            #append right col
            btm = snail_map.pop()
            if len(snail_map) !=0:
                for num_line in snail_map:
                    sorted_list.append(num_line.pop())
                    
            #append btm row
            btm.reverse()
            sorted_list.extend(btm)
            
            #append left col
            if len(snail_map) !=0:
                to_add = []
                for num_line in snail_map:
                    to_add.append(num_line.pop(0))
                to_add.reverse()
                sorted_list.extend(to_add)
                
    return sorted_list
