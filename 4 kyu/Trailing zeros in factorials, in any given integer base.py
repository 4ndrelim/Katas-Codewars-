# Description #

# A factorial (of a large number) will usually contain some trailing zeros. 
# Your job is to make a function that calculates the number of trailing zeros, in any given base.
# Factorial is defined like this: n! = 1 * 2 * 3 * 4 * ... * n-2 * n-1 * n

# Here's two examples to get you started:
# trailing_zeros(15, 10) == 3
# #15! = 1307674368000, which has 3 zeros at the end

# trailing_zeros(7, 2) == 4
# #7! = 5030 = 0b1001110110000, which has 4 zeros at the end

# Note: num will be a non-negative integer, base will be an integer larger or equal to two.


  
def find_prime(num):
    d = {}
    while not num%2:
        d[2] = d.get(2,0)+1
        num//=2
    for p in range(3,int(num**0.5)+1, 2):
        if not num//p:
            break
        while not (num%p):
            num//=p
            d[p] = d.get(p,0)+1
    if num>2:
        d[num] = 1
    return d

def trailing_zeros(num, base):
    zeros = float('inf')
    primes = find_prime(base)
    for p, e in primes.items():
        red_num, count = num, 0
        while red_num:
            red_num//=p
            count+=red_num
        count//=e
        zeros = min(zeros, count)
    return zeros
