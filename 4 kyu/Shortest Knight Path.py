# Description #
# Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other. 
# The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.
# The knight is not allowed to move off the board. The board is 8x8


def knight(p1, p2):
    start = (8-int(p1[1]), ord(p1[0]) - ord('a'))
    end = (8-int(p2[1]), ord(p2[0]) - ord('a'))
    queue = [(start,0)] #BFS
    seen = {start} #checking in set is O(1)
    moves = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
    
    while queue:
        curr = queue.pop(0)
        if curr[0] == end:
            return curr[1]
        for r,c in moves:
            row, col = curr[0][0]+r, curr[0][1]+c
            if 0<=row<8 and 0<=col<8 and (row,col) not in seen:
                queue.append(((row,col), curr[1]+1))
                seen.add((row,col))
