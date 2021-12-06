# Description #
# Your are given a string containing the current state of the control crystals inner pathways (labeled as "X") and its gaps (labeled as "."). 
# Generate the shortest path from the start node (labeled as "S") to the goal node (labeled as "G") and return the new pathway (labeled with "P" characters).
# If no solution is possible, return the string "Oh for crying out loud..." (in frustration).

# Rules:
#   1. Nodes labeled as "X" are not traversable.
#   2. Nodes labeled as "." are traversable.
#   3. A pathway can be grown in eight directions (up, down, left, right, up-left, up-right, down-left, down-right), so diagonals are possible.
#   4. Nodes labeled "S" and "G" are not to be replaced with "P" in the case of a solution.
#   5. The shortest path is defined as the path with the shortest euclidiean distance going from one node to the next.
#   6. If several paths are possible with the same shortest distance, return any one of them.

# Note: 
# Mazes won't always be squares.
# Your solution will have to be efficient because it will have to deal with a lot of maps and big ones.

# Caracteristics of the random tests:
#   1. map sizes from 3x3 to 73x73 (step is 5 from one size to the other, mazes won't always be squares)
#   2. 20 random maps for each size.
#   3. Overall, 311 tests to pass with the fixed ones.

                                  

from heapq import heappop, heappush
class Node:
    def __init__(self, curr, parent):
        self.curr = curr
        self.p = parent
def wire_DHD_SG1(existing_wires):
    m = existing_wires.split('\n')
    start, end = None, None
    for i, row in enumerate(m):
        m[i] = list(m[i])
        for j, char in enumerate(row):
            if char == 'S':
                start = (i,j)
            elif char == 'G':
                end = (i,j)
    MOVES = {(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)}
    def ecd(coord, d = end):
        i,j = coord[0], coord[1]
        return ((i-d[0])**2 + (j-d[1])**2)**0.5
    
    s = Node(start, None)
    s_cost, count, explored = ecd(s.curr), 0, set()
    queue = [(s_cost, s_cost, 0, count, s)]
    
    while queue: #A* search
        _, _, cost, _, node = heappop(queue)
        if node.curr in explored:
            continue
        if node.curr == end:
            node=node.p
            while node.curr != start and node.curr != None: #accounts for start is end as well
                m[node.curr[0]][node.curr[1]] = 'P'
                node = node.p
            for i in range(len(m)):
                m[i] = ''.join(m[i])
            return '\n'.join(m)
            
        explored.add(node.curr)
        for dy, dx in MOVES:
            i,j = node.curr[0]+dy, node.curr[1]+dx
            if 0<=i<len(m) and 0<=j<len(m[0]) and m[i][j] != 'X':
                h_c = ecd((i,j))
                g_c = cost+ecd((i,j), node.curr)
                t_c = g_c+h_c
                count+=1
                heappush(queue, (t_c, h_c, g_c, count, Node((i,j), node)))
        
    return "Oh for crying out loud..."
