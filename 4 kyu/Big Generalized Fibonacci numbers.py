# Description #

# Fibonacci sequence is defined as follows: F(n+1) = F(n) + F(n-1), where F(0) = 0, F(1) = 1

# You are given two lists of integers A and B of same size, and a positive integer n.
# List A represents first values of the sequence, namely F(0) == A(0), F(1) == A(1), ..., F(len(A)-1) = A(len(A)-1)
# List B represents coefficients of recurrent equation F(n) = B(0)*F(n-1) + B(1)*F(n-2) + ... + B(len(B)-1)*F(n-len(B))
# n is the index of number in the sequence, which you need to return.
# Note: solution must have O(log n) complexity to pass the tests.

# Range of numbers:
# There are 100 random tests. 2 <= len(A) == len(B) <= 5, 0 <= n <= 100000. Initial values are in range [-5; 5], and the coefficients are in range [-2; 2]


# trick: Consider matrix product
def matrix_mul(A,B):
    return [[sum([A[row][i] * B[i][col] for i in range(len(B))]) for col in range(len(B[0]))] for row in range(len(A))]

def power(n, M, F):
    if n == 0 or n == 1: return M
    M = power(n//2, M, F)
    M = matrix_mul(M,M)
    if n%2:
        M = matrix_mul(M, F)
    return M
    
def generalized_fibonacchi(a, b, n):
    length = len(a)
    M = [[0 for i in range(length)] for j in range(length)]
    M[0] = b[:]
    for i in range(1, length):
        M[i][i-1] = 1
    M = power(n-length+1, M, M)
    return sum([M[0][i]*a[length-1-i] for i in range(length)])
        
    #O(n) 
    #if n < len(a): return a[n]
    #cache = a
    #for i in range(len(a), n+1):
        #cache.append(sum(list(map(lambda x,y: x*y, [cache[i-1-j] for j in range(len(a))], b))))
    #return cache[n] 
