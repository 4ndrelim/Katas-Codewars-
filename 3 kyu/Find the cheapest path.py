# Description #
# Your task is to find the path through the field which has the lowest cost to go through.

# As input you will receive:
#   1. a toll_map matrix (as variable t) which holds data about how expensive it is to go through the given field coordinates
#   2. a start coordinate (tuple) which holds information about your starting position
#   3. a finish coordinate (tuple) which holds information about the position you have to get to
  
# As output you should return:
# 1. the directions list

# CLARIFICATIONS:
#   1. the start and finish tuples have the (x, y) format which means start = (x_1, y_1) and finish = (x_2, y_2), start_pos = field[x_1][y_1] and finish_pos = field[x_2][y_2]
#   2. the total cost is increased after leaving the matrix coordinate, not entering it
#   3. the field will be rectangular, not necessarily a square
#   4. the field will always be of correct shape
#   5. the actual tests will check total_cost based on your returned directions list, not the directions themselves, so you shouldn't worry about having multiple possible solutions

  
  
from heapq import heappop, heappush
MOVES = {(1,0): 'down', (0,1): 'right', (-1,0): 'up', (0,-1): 'left'}
def cheapest_path(t, start, finish):
    r, c = len(t), len(t[0])
    
    def ecd(coord):
        i,j = coord[0], coord[1]
        return ((i-finish[0])**2 + (j-finish[1])**2)**0.5
    
    h_c, count = ecd(start), 0
    q, x = [(h_c, h_c, 0, count, start, [])], set()
    while q:
        _, _, cost, _, coord, path = heappop(q)
        if coord in x:
            continue
        if coord == finish:
            return path
        x.add(coord)
        for d, dir in MOVES.items():
            dx,dy = d
            new_x, new_y = coord[0]+dx, coord[1]+dy
            if 0<=new_x<r and 0<=new_y<c:
                n_c = t[coord[0]][coord[1]]+cost
                h_c = ecd((new_x, new_y))
                t_c = n_c+h_c
                n_path = path[:] + [dir]
                count+=1
                heappush(q, (t_c, h_c, n_c, count, (new_x, new_y), n_path))
    return "Something went wrong.."
