# Description #
# The prime 149 has 3 permutations which are also primes: 419, 491 and 941.

# There are 3 primes below 1000 with three prime permutations:
# 149 ==> 419 ==> 491 ==> 941
# 179 ==> 197 ==> 719 ==> 971
# 379 ==> 397 ==> 739 ==> 937

# But there are 9 primes below 1000 with two prime permutations:
# 113 ==> 131 ==> 311
# 137 ==> 173 ==> 317
# 157 ==> 571 ==> 751
# 163 ==> 613 ==> 631
# 167 ==> 617 ==> 761
# 199 ==> 919 ==> 991
# 337 ==> 373 ==> 733
# 359 ==> 593 ==> 953
# 389 ==> 839 ==> 983

# Finally, we can find 34 primes below 1000 with only one prime permutation:
# [13, 17, 37, 79, 107, 127, 139, 181, 191, 239, 241, 251, 277, 281, 283, 313, 347, 349, 367, 457, 461, 463, 467, 479, 563, 569, 577, 587, 619, 683, 709, 769, 787, 797]

# Note:
#   1. Each set of permuted primes are represented by its smallest value, for example the set 149, 419, 491, 941 is represented by 149, and the set has 3 permutations
#   2. the original number (149 in the above example) is not counted as a permutation
#   3. permutations with leading zeros are not valid

# Your task is to create a function that takes two arguments:
#   1. an upper limit (n_max) and
#   2. the number of prime permutations (k_perms) that the primes should generate below n_max

# The function should return the following three values as a list:
#   1. the number of permutational primes below the given limit,
#   2. the smallest prime such prime,
#   3. and the largest such prime
# If no eligible primes were found below the limit, the output should be [0, 0, 0]

# Examples:
# Let's see how it would be with the previous cases:

# permutational_primes(1000, 3) ==> [3, 149, 379]
# ''' 3 primes with 3 permutations below 1000, smallest: 149, largest: 379 '''

# permutational_primes(1000, 2) ==> [9, 113, 389]
# ''' 9 primes with 2 permutations below 1000, smallest: 113, largest: 389 '''

# permutational_primes(1000, 1) ==> [34, 13, 797]
# ''' 34 primes with 1 permutation below 1000, smallest: 13, largest: 797 '''



import itertools
def permutational_primes(n_max, k_perms):
    primes = [True for i in range(n_max+1)] #ignore 0th and 1st index
    p = 2
    while (p*p < n_max+1):
        if primes[p]:
            for i in range(p*p, n_max+1, p):
                primes[i] = False
        if p == 2:
            p+=1
        else:
            p+=2
    res = set()
    for i in range(2, n_max+1):
        if primes[i]:
            curr = str(i)
            perms = set((itertools.permutations(curr)))
            act_perms = []
            for p in perms:
                num = int(''.join(p))
                if num // 10**(len(p)-1) == 0 or num > n_max or not primes[num]: #ignore invalid perms
                    continue
                act_perms.append(num)
            if len(act_perms) == k_perms+1: #min_prime of each permutation is not considered as part of total count
                res.add(min(act_perms))
    return [len(res), min(res), max(res)] if res else [0,0,0]
