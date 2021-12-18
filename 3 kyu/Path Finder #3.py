# Description #
# You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). 
# Return minimal number of climb rounds to target location [N-1, N-1]. 
# Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

# Note: Location altitude is defined as an integer number (0-9)


from heapq import heappop, heappush

def path_finder(area): #Dijkstra's
    MOVES = {(0,1), (1,0), (0,-1), (-1,0)}
    area = area.split('\n')
    N = len(area)
    def abs(x):
        return x * ((x>0) - (x<0))
    
    shortest_dist, count = {(0,0): 0}, 0
#     explored = set() #explored tracker not nec here.
    queue = [(0,count,(0,0))]
    
    while queue:
        cost, _, coord = heappop(queue)
#         if coord in explored:
#             continue
        if coord == (N-1,N-1):
            return shortest_dist[coord]
#         explored.add(coord)
        for dx,dy in MOVES:
            n_x, n_y = coord[1]+dx, coord[0]+dy
            if 0<=n_x<N and 0<=n_y<N:
                diff = abs(int(area[n_y][n_x]) - int(area[coord[0]][coord[1]]))
                n_cost = cost + diff
                if n_cost < shortest_dist.get((n_y, n_x), float('inf')):
                    shortest_dist[(n_y, n_x)] = n_cost
                    count+=1
                    heappush(queue, (n_cost, count, (n_y, n_x)))
                    
    return "Something went wrong.."
  
  # Note: A* would be difficult to implement because need to ensure h_cost is not overestimated. 
