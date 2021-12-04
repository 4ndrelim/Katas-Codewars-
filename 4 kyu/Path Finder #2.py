


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
