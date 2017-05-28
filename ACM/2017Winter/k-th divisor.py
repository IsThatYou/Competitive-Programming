import math
def sieve(n):
    if n == 1:
        return[0]
    if n == 2:
        return[0,0]
    mark = [i % 2 for i in range(n)]
    mark[1] = 0
    mark[2] = 1
    for value in range(3,n,2):
        if mark[value] == 1:
            for i in range(value * 3, n, value * 2):
                mark[i] = 0
    return mark

inpu1 = input().split()
def prime_factorization(num):
    primes = sieve(math.ceil(num ** .5)) # if primes are not prebuilt
    reduced = {}
    for i in range(len(primes)):
        if primes[i] == 1:
            prime = i
            if prime <= num and num % prime == 0:
                reduced[prime] = 0
                while num % prime == 0:
                    reduced[prime] += 1
                    num //= prime
    return reduced
def prime_factorization2(num):
    #primes = sieve(math.ceil(num ** .5))
    reduced = {}
    if num % 2 == 0:
        reduced[2] = 0
        while num % 2 == 0:
            reduced[2] += 1
            num //= 2
    for i in range(3, math.ceil(num ** .5)+1, 2):
        if num % i == 0:
            reduced[i] = 0
            while num % i == 0:
                reduced[i] += 1
                num //= i
    if num > 2:
        reduced[num] = 1
    return reduced
def factor1(a, k, n):
    counter = 1
    if k == counter:
        return 1
    if k == n:
        return a
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            counter += 1
            if k == counter:
                return(i)
            if k == (n-counter+1):
                return int(a/i)
    return -1

n = int(inpu1[0])
k = int(inpu1[1])
a = prime_factorization2(n)
sum =1
for i in a:
    sum *= (a[i]+1)
print(a)
if k > sum:
    print(-1)
else:
    print(factor1(n, k, sum))

