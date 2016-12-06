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
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
# Great Common divisor
def gcd(a, b):
    while (a == 0):
        return b
    return gcd(b%a, a)
a = gcd(3,25)
print(a)

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
# a is the list, d is the value to be searched
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
        print new
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




