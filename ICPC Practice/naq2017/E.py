import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: 
        return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom
p = int(input())
for i in range(p):
    k, n,m = [int(x) for x in input().split()]
    sums =0
    for j in range(m+2):
        sums += (((-1)**j) * (ncr(n+1,j)) * ((m+1-j)**n))
        sums = sums%1001113
    print(k,sums)
