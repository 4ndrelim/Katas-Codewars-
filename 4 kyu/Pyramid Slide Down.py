# Description #
# Let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:
#    /3/
#   \7\ 4 
#  2 \4\ 6 
# 8 5 \9\ 3


# Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. 
# As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

# Your task is to write a function that takes a pyramid representation as argument and returns its' largest 'slide down'. For example,
# longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23

# Note:
# Tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. 
# You must come up with something more clever than that.


def longest_slide_down(pyramid):
    #do not fixate on a computing a path
    
    #top-down
    while pyramid[1:]:
        first = pyramid.pop(0)
        n = len(first)
        for i in range(len(pyramid[0])):
            pyramid[0][i] += max(first[i-1] if i-1>=0 else 0, first[i] if i<n else 0)
    return max(pyramid[-1])
            
    #bottom-up. preferred.
    while pyramid[1:]:
        last = pyramid.pop()
        for i in range(len(pyramid[-1])):
            pyramid[-1][i]+=max(last[i], last[i+1])
    return pyramid[0][0]
