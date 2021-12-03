# Description #
# Given an array X of positive integers, its elements are to be transformed by running the following operation on them as many times as required:

# if X[i] > X[j] then X[i] = X[i] - X[j]

# When no more transformations are possible, return its sum ("smallest possible sum").

# For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:

# X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
# X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
# X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
# X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
# X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
# The returning output is the sum of the final transformation (here 9).



#define gcd function or import from math lib
def gcd(int1, int2):
    if int1 == int2:
        return int1
    r_prev = max(int1,int2)
    r = min(int1, int2)
    while r:
        r_prev, r = r, r_prev%r
    return r_prev

def solution(a):
    for i in range(len(a)-1):
        gcd_v = gcd(a[i], a[i+1])
        a[i], a[i+1] = gcd_v, gcd_v
    return len(a) * a[-1]
