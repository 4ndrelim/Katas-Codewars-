# Description #

# A format for expressing an ordered list of integers is to use a comma separated list of either
# 1. individual integers or
# 2. a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.


def solution(args):
    length = len(args)
    res, i = '', 0
    while i < length:
        start, diff = str(args[i]), 0
        while i+1 < length and args[i+1] - args[i] == 1:
            diff+=1
            i+=1
        if diff > 1:
            res+= start+'-'+str(args[i])+','
        elif diff == 1:
            res+= start+','+str(args[i])+','
        else:
            res+= start+','
        i+=1
    return res[:-1]
