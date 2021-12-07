# Description #
# Personal Note: This kata is similar to Number of Integer Partitions kata
  
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. 
# Two sums that differ only in the order of their summands are considered the same partition. 
# If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
# 4
# 3 + 1
# 2 + 2
# 2 + 1 + 1
# 1 + 1 + 1 + 1


  def exp_sum(n):
    #find no. ways to split r identical balls into k bins
    #such that no bins are empty
    def split(r, k , cache={}):
        if r < k or k == 0:
            return 0
        if r == k or k == 1:
            return 1
        if (r,k) in cache:
            return cache[(r,k)]
        cache[(r,k)] = sum(split(r-k, i) for i in range(1,k+1))
        return cache[(r,k)]
    return sum(split(n, i) for i in range(1,n+1))
