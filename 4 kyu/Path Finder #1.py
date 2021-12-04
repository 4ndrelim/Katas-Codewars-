# Description #
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West).
# Return true if you can reach position [N-1, N-1]; false otherwise

# Note:
# 1. Empty positions are marked '.'
# 2. Walls are marked 'W'
# 3. Start and exit positions are empty in all test cases
# 4. Maze is represented as a string joined by the newline char, '\n'


def path_finder(maze):
    maze = maze.split('\n')
    N = len(maze)
    if N == 1: #check if start == end
        return True
    queue = [(0,0)] #DFS
    seen, moves = {(0,0)}, [(1,0), (0,1), (-1,0), (0,-1)]
    while queue:
        curr = queue.pop()
        for r,c in moves:
            row, col = curr[0]+r, curr[1]+c
            if (row,col) == (N-1,N-1):
                return True
            if 0<=row<N and 0<=col<N and maze[row][col] == '.' and (row,col) not in seen:
                queue.append((row,col))
                seen.add((row,col))
    return False
