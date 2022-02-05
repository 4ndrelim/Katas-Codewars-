# Description #

# The Padovan sequence is the sequence of integers P(n) defined by the initial values P(0)=P(1)=P(2)=1 and the recurrence relation P(n)=P(n-2)+P(n-3).

# The first few values of P(n) are
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...

# Task:
# The task is to write a method that returns i-th Padovan number for i around 1,000,000

# Examples:
# Padovan.Get(0) == 1
# Padovan.Get(1) == 1
# Padovan.Get(2) == 1
# Padovan.Get(n) == Padovan.Get(n-2) + Padovan.Get(n-3)


def matrix_mul(A,B):
    return [[sum([A[row][i] * B[i][col] for i in range(len(B))]) for col in range(len(B[0]))] for row in range(len(A))]

def power(M, n):
    if n == 0 or n == 1: return M

    M = power(M, n//2)
    M0 = [[1,1,0],
         [0,1,1],
         [1,0,0]]
    M = matrix_mul(M,M)
    if n % 2:
        M  = matrix_mul(M, M0)
    return M

def padovan(n):
    if n in [0,1,2]: return 1
    odd = True if n%2 else False
    M = [[1,1,0],
         [0,1,1],
         [1,0,0]]
    M = power(M, (n+1)/2 -1 if odd else n/2 - 1)
    res = [[1],
           [1],
           [1]]
    res = matrix_mul(M, res)
    return res[1][0] if odd else res[0][0]
