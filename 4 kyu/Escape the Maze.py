# Description #


# You are given the whole maze maze as a 2D grid, more specifically in your language:
#   1. an array of strings where maze[0][0] is the top left-hand corner
#   2. maze[len(maze) - 1][len(maze[0]) - 1] is the bottom right-hand corner

# Inside this 2D grid:
#   1. ' ' is some walkable space
#   2. '#' is a thorn bush (you can't pass through)
#   3. '^', '<', 'v' or '>' is your sleeping body facing respectively the top, left, bottom or right side of the map.
                        
# Task:
# Write the function escape that returns the list/array of moves you need to do relatively to the direction you're facing in order to escape the maze (you won't be able to see the map when you wake up). 
# Output is an array with the following instructions:
#   1. 'F' move one step forward
#   2. 'L' turn left
#   3. 'R' turn right
#   4. 'B' turn back
# Note: 
#   1. 'L','R', and 'B' ONLY perform a rotation and will not move your body
#   2. If the maze has no exit, return an empty array.

# Tips:
# This is a real maze, there is no "escape" point. Just reach the edge of the map and you're free!
# You don't explicitely HAVE to find the shortest possible route, but you're quite likely to timeout if you don't ;P
# Aside from having no escape route the mazes will all be valid (they all contain one and only one "body" character and no other characters than the body, "#" and " ". 
# Besides, the map will always be rectangular, you don't have to check that either)

                                                               
                                                               
def escape(maze):
    d = {'v': (1,0), '>': (0,1), '^': (-1,0), '<': (0,-1)}
    MOVES = {'>': {'>': ['F'], 'v': ['R', 'F'], '<': ['B', 'F'], '^': ['L', 'F']},
             'v': {'v': ['F'], '<': ['R', 'F'], '^': ['B', 'F'], '>': ['L', 'F']},
             '<': {'<': ['F'], '^': ['R', 'F'], '>': ['B', 'F'], 'v': ['L', 'F']},
             '^': {'^': ['F'], '>': ['R', 'F'], 'v': ['B', 'F'], '<': ['L', 'F']}}
    start, s_d = None, None
    l, w = len(maze), len(maze[0])
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char in 'v><^':
                start = (i,j)
                s_d = char
                break
    q, x = [(start, [s_d])], {start}
    while q: #BFS
        coord, path = q.pop(0)
        for next_d, m in d.items():
            r, c = m[0] + coord[0], m[1] + coord[1]
            if 0<=r<l and 0<=c<w and maze[r][c] != '#' and (r,c) not in x:
                if r == l-1 or r == 0 or c == 0 or c == w-1:
                    res = []
                    path.append(next_d)
                    for i in range(len(path)-1):
                        res.extend(MOVES[path[i]][path[i+1]])
                    return res
                else:
                    x.add((r,c))
                    q.append((((r,c), path[:]+[next_d])))
    return []
