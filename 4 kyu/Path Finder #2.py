# Description #
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). 
# Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position. Otherwise, return false.

# Note:
# 1. Empty positions are marked '.'
# 2. Walls are marked 'W'
# 3. Start and exit positions are empty in all test cases
# 4. Maze is represented as a string joined by the newline char, '\n'


def path_finder(maze):
    maze = maze.split('\n')
    N = len(maze)
    queue = [((0,0),0)] #BFS
    seen = {(0,0)}
    if N == 1: #start is end
        return 0
    while queue:
        curr, step = queue.pop(0)
        for r,c in [(1,0), (0,1), (-1,0), (0,-1)]:
            row, col = curr[0]+r, curr[1]+c
            if (row, col) == (N-1, N-1):
                return step+1
            if 0<=row<N and 0<=col<N and (row,col) not in seen and maze[row][col] == '.':
                queue.append(((row,col), step+1))
                seen.add((row,col))
    return False
