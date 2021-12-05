# Description #
# How many zeroes are at the end of the factorial of 10? 
# 10! = 3628800, i.e. there are 2 zeroes. 16! (or 0x10!) in hexadecimal would be 0x130777758000, which has 3 zeroes

# Write a function, which will find the number of zeroes at the end of (number) factorial in arbitrary radix = base for larger numbers.
# Note:
# 1. base is an integer from 2 to 256
# 2. number is an integer from 1 to 1'000'000
# 3. Second argument: number is always declared, passed and displayed as a regular decimal number


def prime_factors(num):
    d = {}
    while num%2 == 0:
        d[2] = d.get(2,0)+1
        num//=2
    for i in range(3, int(num**0.5)+1, 2):
        while num%i == 0:
            d[i] = d.get(i,0)+1
            num//=i
    if num > 2: #itself is a prime
        d[num] = 1
    return d
  
def zeroes (base, number):
    d = prime_factors(base)
    min_count = float('inf')
    for prime, pow in d.items():
        num, count = number, 0
        while num >= prime:
            num//=prime
            count+=num
        min_count = min(min_count, count//pow)
    return min_count
