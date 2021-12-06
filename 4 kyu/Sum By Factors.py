# Description #
# Given an array of positive or negative integers e.g
# I = [i1,..,in]

# you have to produce a sorted array P of the form
# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

# P will be sorted by increasing order of the prime numbers. 
# The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

# Example:
# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

# Note:
# It can happen that a sum is 0 if some numbers are negative!
# E.g: I = [15, 30, -45], 5 divides 15, 30 and (-45) so 5 appears in the result.
# The sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.


def find_prime(num):
    num = abs(num)
    primes = set()
    while num%2 == 0:
        num//=2
        if 2 not in primes:
            primes.add(2)
    for i in range(3, int(num**0.5)+1, 2):
        while num%i == 0:
            num//=i
            if i not in primes:
                primes.add(i)
    if num > 2:
        primes.add(num)
    return primes
  
def union(set1, set2):
    for num in set2:
        set1.add(num)
        
def sum_for_list(lst):
    primes = set()
    for num in lst:
        union(primes, list(find_prime(num)))
    res = []
    for p in primes:
        res.append([p, sum(map(lambda x: x if x%p == 0 else 0, lst))])
    return sorted(res)
