# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:
# apples, pears # and bananas
# grapes
# bananas !apples


# The output expected would be:
# apples, pears
# grapes
# bananas

def solution(string,markers):
    parsed = string.split('\n')
    res = ''
    for s in parsed:
        e = len(s)
        for i, char in enumerate(s):
            if char in markers:
                e = i
                break
        res+=s[:e].strip() + '\n'
    return res[:-1]
