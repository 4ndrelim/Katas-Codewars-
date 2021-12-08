# Description #

# Consider a sequence u where u is defined as follows:
#   1. The number u(0) = 1 is the first one in u.
#   2. For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
#   3. There are no other numbers in u.
  
# Take u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...

# Task:
# Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

# Example:
# dbl_linear(10) should return 22


def dbl_linear(n):
    c, curr = 0, 1
    q1 = [3]
    q2 = [4]
    while c<n:
        new = None
        if q1[0] < q2[0]:
            new = q1.pop(0)
        else:
            new = q2.pop(0)
        if new == curr:
            continue
        curr = new
        q1.append(curr*2+1)
        q2.append(curr*3+1)
        c+=1
    return curr
