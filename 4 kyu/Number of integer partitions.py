# Description #
# An integer partition of n is a weakly decreasing list of positive integers which sum to n.

# For example, there are 7 integer partitions of 5:
# [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].

# Write a function which returns the number of integer partitions of n. 
# The function should be able to find the number of integer partitions of n for n at least as large as 100


def partitions(n):
    known = [[False for i in range(n)] for i in range(n)]
    def split(r, k): #find number of ways to split r identical balls into k boxes such that no box is empty
        if r < k or k == 0:
            return 0
        if k == 1 or r == k:
            return 1
        if known[r-1][k-1]:
            return known[r-1][k-1]
        ways = [split(r-k, i) for i in range(1, k+1)]
        known[r-1][k-1] = sum(ways)
        return known[r-1][k-1]
   
    return sum([split(n, i) for i in range(1,n+1)])
