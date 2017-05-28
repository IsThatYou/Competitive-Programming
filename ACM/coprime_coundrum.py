import math
import mathhelp

'''
https://projecteuler.net/problem=250
'''

def main():
    #DP fo project euler 250
    lis = []
    for i in range(1, 250251):
        lis.append(mathhelp.fast_exp(i, i, 10**16))
    arr = [0] * 250
    arr[0] = 1
    for val in lis:
        newarr = [0] * 250
        for i in range(250):
            newarr[i] = (arr[i] + arr[(i+val)%250])%(10**16)
        arr = newarr

    print((arr[0]-1))

'''
Principle of Inclusion/Exclusion
'''
#main()
primes = mathhelp.sieve(10**5)


def just_primes(x):
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
#print(just_primes(5))
def coprime(x,y):
    if math.gcd(x,y) == 1:
        return True
    return False
a = int(input())
#qa = int(math.sqrt(a)) + 1
qa = int(a//2) + 1
result = 0
for i in range(3, qa):
    nprimes = just_primes(i)
    interest = i
    if len(nprimes) != 0:
        for j in nprimes:
            interest = interest * (j-1)/j
        print(interest, i)
        result += interest-1
    else:
        result += i-2
print(result)
# https://www.hackerrank.com/challenges/arthur-and-coprimes

## This doesn't work since we don't know if the product of these two would exceed the n.
## we only know the number of coprimes it has.

# USE THIS INSTEAD https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
