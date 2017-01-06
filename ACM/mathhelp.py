# Get Prime in a list
import math
def sieve(n):
    mark = [i % 2 for i in range(n)]
    mark[1] = 0
    mark[2] = 1
    for value in range(3,n,2):
        if mark[value] == 1:
            for i in range(value * 3, n, value * 2):
                mark[i] = 0
    return mark

'''
def sieve(n):
    list = [False] * (n + 1)
    Primes = []
    for i in range(2, n + 1):
        if not list[i]:
            Primes.append(i)
            for j in range(2 * i, n + 1, i):
                list[j] = True
    return Primes
'''

primes = sieve(10 ** 6)


def prime_factorization(num):
    # primes = sieve(num) # if primes are not prebuilt
    reduced = {}
    for prime in primes:
        if prime <= num and num % prime == 0:
            reduced[prime] = 0
            while num % prime == 0:
                reduced[prime] += 1
                num //= prime
    return reduced


def prime_factorization2(num):
    reduced = {}
    if num % 2 == 0:
        reduced[2] = 0
        while num % 2 == 0:
            reduced[2] += 1
            num //= 2
    for i in range(3, math.ceil(num ** .5), 2):
        if num % i == 0:
            reduced[i] = 0
            while num % i == 0:
                reduced[i] += 1
                num //= i
    if num > 2:
        reduced[num] = 1


primes = sieve(1000)
def just_primes(num):
    # primes = sieve(math.ceil(num**.5))
    divisible = []
    if num % 2 == 0:
        divisible.append(2)
        num //= 2
    for prime in primes:
        while num % prime == 0:
            if not prime in divisible:
                divisible.append(prime)
            num //= (prime)
    if num > 2:
        divisible.append(num)
    return divisible

# This one doesn't return itself, if it is a prime
def just_primes2(x):
    # primes = sieve(math.ceil(num**.5))
    num = x
    divisible = []
    if num % 2 == 0:
        divisible.append(2)
        num //= 2
        if num == 1:
            return []
    for i in range(len(primes)):
        if primes[i] == 1:
            prime = i
            if prime > num:
                break
            while num % prime == 0:
                if not prime in divisible:
                    divisible.append(prime)
                num //= prime
                if x/prime == 1:
                    return []
    if num > 2:
        divisible.append(num)
    return divisible
def num_coprimes(num):
    factorized = just_primes(num)
    coprimes = num
    # print(factorized)
    for p in factorized:
        coprimes *= (1 - 1 / p)
    return int(coprimes)

def getPrimes(m):
    sieves = sieve(m)
    primes = [i for i, f in enumerate(sieves) if f]
    return primes, sieves

def isprime(nums):
    logicallist = []
    for n, i in enumerate(nums):
        i = int(i)
        if i == 0 or i == 1:
            logicallist.append(0)
        elif i == 2:
            logicallist.append(1)
        elif i > 2:
            if i % 2 == 0:
                logicallist.append(0)
            else:

                for j in range(3, int(i**(1/2.0)) + 1, 2):
                    if i % j == 0:
                        logicallist.append(0)

                if len(logicallist) != n + 1:
                    logicallist.append(1)

    return logicallist
# Great Common divisor
def gcd(a, b):
    while (a == 0):
        return b
    return gcd(b%a, a)
a = gcd(3,25)


# Find Least Common Mutiplier
def lcm(a, b):
    c = gcd(a, b)
    a1 = a/c
    b1 = b/c
    return c * a1 * b1

# Get 26 letters in a list
def getLetters():
    a = [i for i in range(97, 123)]
    a = map(lambda x: chr(x), a)
    return a

# BinarySearch
def binarySearch(a, d):
    low = 0
    up = len(a) -1
    x = a[(up + low)/2]
    if d == x: return (up + low)/2
    while d!= x:
        if d > x:
            low = (low + up)/2 + 1
            x = a[(low + up )/2]
        elif d < x:
            up = (low + up)/2 - 1
            x = a[(low + up)/2]
        if d == x:
            return (up + low)/2
def decimal2binary(num):
    i = 0
    bin = []
    while 2**i <= num:
        i += 1
    n = i - 1
    bin.append('1')
    num1 = num
    new = num1 - 2**n
    num1 = new

    while n > 0:
        n -= 1
        new = num1 - 2**n
        print(new)
        if new >= 0:
            bin.append('1')
            num1 = new
        else:
            bin.append('0')
    return bin

#any number to a base.  represented as a list of intergers in that base.
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]


def fast_exp(x,n,m):
    result = 1
    currentpower = x
    while n > 0:
        if n % 2 == 1:
            result = (result * currentpower) % m

        currentpower = (currentpower * currentpower) % m
        n = n//2

    return result

