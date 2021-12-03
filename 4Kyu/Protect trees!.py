# Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

# If there are multiple solutions (and there will be), return as far as possible the result with the largest possible values:


# Examples:
# decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

# For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

# Note:
# Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

# Hint
# Very often xk will be n-1.

def decompose(n):
    # your code
    res = []
    #helper tries to find composition for curr_sum to hit target sum; exceeding it would return False
    #curr_sum is sum of all sqaures in res
    def helper(curr_sum):
        if curr_sum == n**2:
            return True
        elif curr_sum > n**2:
            return False
        upper_bound = int((n**2 - curr_sum)**0.5)
        if curr_sum == 0:
            upper_bound = n-1
        for i in range(upper_bound, 0, -1):
            if i not in res:
                res.append(i)
                if helper(curr_sum+i**2):
                    return True
                res.pop()
        return False
    return sorted(res) if helper(0) else None
  
  
  

#O(N**2) complexity
def decompose_slow(n):
    # your code
    t = 0
    res = [n]
    while res:
        p = res.pop()
        t+=p**2
        for i in range(p-1, 0, -1):
            if t-i**2 >= 0:
                t-=i**2
                res.append(i)
        if t == 0:
            break
    return sorted(res) if res else None
