# Description #

# In this kata you will have to calculate fib(n) where:
# fib(0) := 0
# fib(1) := 1
# fin(n + 2) := fib(n + 1) + fib(n)
  
# Write an algorithm that can handle n up to 2000000.
# Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input


def matrix_mul(A,B):
    return [[sum([A[row][i]*B[i][col] for i in range(len(B))]) for col in range(len(B[0]))] for row in range(len(A))]

def power(F, n):
    if n == 0 or n == 1: return F
    M = [[1,1],
         [1,0]]
    F = power(F, n//2)
    F = matrix_mul(F,F)
    if n%2:
        F = matrix_mul(F, M)
    return F
        
def fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 0: return 0
    negative = False
    if n < 0:
        n = 0-n
        if n%2 == 0: negative = True
        
    F = [[1,1],
         [1,0]]
    
    F = power(F, n-1)
    return 0-F[0][0] if negative else F[0][0]
