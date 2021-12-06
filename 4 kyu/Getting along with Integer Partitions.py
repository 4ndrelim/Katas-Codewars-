# Description #
# In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. 
# Two sums that differ only in the order of their summands are considered the same partition.
# For example, 4 can be partitioned in five distinct ways:
# 4, 3 + 1, 2 + 2, 2 + 1 + 1, 1 + 1 + 1 + 1

# enum(5) -> [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]

# The number of parts in a partition grows very fast. For n = 50 number of parts is 204226, for 80 it is 15,796,476.
# It would be too long to tests answers with arrays of such size. So our task is the following:

#   1. n being given (n integer, 1 <= n <= 50) calculate enum(n) ie the partition of n. We will obtain something like that:
#     enum(n) -> [[n],[n-1,1],[n-2,2],...,[1,1,...,1]] (order of array and sub-arrays doesn't matter). This part is not tested.

#   2. For each sub-array of enum(n) calculate its product. If n = 5 we'll obtain after removing duplicates and sorting:
#                                                       prod(5) -> [1,2,3,4,5,6]
#                                                       prod(8) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 18]

# If n = 40 prod(n) has a length of 2699 hence the tests will not verify such arrays. Instead our task number 3 is:
#   3. return the range, the average and the median of prod(n) in the following form (example for n = 5):
#                                                       "Range: 5 Average: 3.50 Median: 3.50"

# Note: Range is an integer, Average and Median are float numbers rounded to two decimal places (".2f" in some languages)


# old
from functools import reduce
from operator import mul

def part(n):
    known_prod = {i for i in range(1,n+1)}
    
    #find prod of sub-arrays of size-k
    def find_prod(size, k, curr_list, curr_sum):
        if (curr_list and curr_list[0] > round(n/2)) or len(curr_list) > k:
            return
        if len(curr_list) == k:
            if curr_sum <= n:
                known_prod.add(reduce(mul, curr_list))
            return
                
        for i in range(curr_list[-1] if curr_list else 2, size+1):
            if (curr_sum + i) > n:
                break
            curr_list.append(i)
            find_prod(size-i, k, curr_list, curr_sum + i)
            curr_list.pop()
        return
    
    for i in range(2,round(n/2)+1):
        find_prod(n, i, [], 0)
    
    known_prod = sorted(list(known_prod), reverse = True)
    length = len(known_prod)
    range_ = known_prod[0] - known_prod[-1]
    avg = round(sum(known_prod)/length ,2)
    median = known_prod[length//2] if length % 2 else (known_prod[length//2] + known_prod[length//2 -1])/2

    return f"Range: {range_} Average: {avg:.2f} Median: {median:.2f}"
