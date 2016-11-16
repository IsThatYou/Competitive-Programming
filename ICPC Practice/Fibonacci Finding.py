def fastexp(x,n,m):
    result = 1
    currentpower = x
    while n > 0:
        if n % 2 == 1:
            result = (result * currentpower) % m

        currentpower = (currentpower * currentpower) % m
        n = n//2

    return result
print('sd')
print(fastexp(2, 13,100000000000))
print('sd')
def sieve(n):
    l = [False] *(n+1)
    primes = []
    for i in range(2, n+1):
        if not l[i]:
            primes.append(i)
            for j in range(1, n+1, i):
                l[j] = True
    return primes
#for 2x2 matrix
def exp_m(x1, y1, x2, y2, n, m):
    sx1 = x1
    sy1 = y1
    sx2 = x2
    sy2 = y2
    while n > 0:
        if n % 2 == 1:




print(exp_m(1,1,1,0,10,100000000))