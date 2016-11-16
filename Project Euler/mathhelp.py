# Get Prime in a list
def sieve(n):
    mark = [i % 2 for i in range(n)]
    mark[1] = 0
    mark[2] = 1
    for value in range(3,n,2):
        if mark[value] == 1:
            for i in range(value * 3, n, value * 2):
                mark[i] = 0
    return mark
 
def getPrimes(m):
    sieves = sieve(m)
    primes = [i for i, f in enumerate(sieves) if f]
    return primes, sieves
# Great Common divisor

def gcd(a, b):
    if b > a: a, b = b, a
    while b > 0:
        remainder = a % b
        a = b
        b = remainder
    return a
#

    
    

