def doubles(maxk, maxn):
    # note complexity of python's '/' operator
    return sum(sum((n+1)**(-2*k) for n in range(1,maxn+1))/k for k in range(1,maxk+1))


