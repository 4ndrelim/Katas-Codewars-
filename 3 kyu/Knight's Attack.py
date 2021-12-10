from heapq import heappush, heappop



from heapq import heappush, heappop
def attack(start, dest, obstacles):
    def ecd(coord, end):
        return (((coord[0]-end[0])**2 + (coord[1]-end[1])**2)**0.5)/5**0.5 #approx dist count
    obstacles = set(obstacles) #check in set is O(1)
    MOVES = {(1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1), (2,1)}
    O = (start, dest)
    stored_cost = [{start:0}, {dest:0}]
    count1, count2 = 0, 0
    count = [count1, count2]
    c1 = ecd(start, dest)
    c2 = ecd(dest, start)
    q = [ [(c1, 0, count1, start)], [(c2, 0, count2, dest)] ]
    while q[0] and q[1]:
        for i in range(2):
            _, cost, _, coord = heappop(q[i])
            if coord in stored_cost[i] and coord in stored_cost[1-i]:
                return stored_cost[i][coord] + stored_cost[1-i][coord]
            for dy, dx in MOVES:
                r,c = coord[0]+dy, coord[1]+dx
                n_c = cost+1
                if (r,c) not in obstacles and n_c < stored_cost[i].get((r,c),float('inf')):
                    stored_cost[i][(r,c)] = n_c
                    count[i]+=1
                    heappush(q[i], (n_c+ecd((r,c), O[1-i]), n_c, count[i], (r,c)))
    return None


# Uninformed search is too slow.
# def attack(start, dest, obstacles):
#     MOVES = {(1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1), (2,1)}
#     O = (start, dest)
#     stored_cost = [{start:0}, {dest:0}]
#     count1, count2 = 0, 0
#     count = [count1, count2]
#     q = [ [(0, count1, start)], [(0, count2, dest)] ]
#     while q[0] and q[1]:
#         for i in range(2):
#             cost, _, coord = heappop(q[i])
#             if coord in stored_cost[i] and coord in stored_cost[1-i]:
#                 return stored_cost[i][coord] + stored_cost[1-i][coord]
#             for dy, dx in MOVES:
#                 r,c = coord[0]+dy, coord[1]+dx
#                 n_c = cost+1
#                 if (r,c) not in obstacles and n_c < stored_cost[i].get((r,c),float('inf')):
#                     stored_cost[i][(r,c)] = cost+1
#                     count[i]+=1
#                     heappush(q[i], (n_c, count[i], (r,c)))
#     return None
