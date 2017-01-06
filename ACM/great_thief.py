import sys
'''
15 = 3 * 5
0,1,2   0,1,2,3,4
2 * 4 = 8

45 = 3^2 * 5
0,1,2,3,4,5,6,7,8,9
0,1,2,3,4
6 * 4 ( take out 0,3,6)
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


def num_coprimes2(num):
    factorized = just_primes(num)
    coprimes = num
    # print(factorized)
    for p in factorized:
        coprimes *= (1 - 1 / p)
    return int(coprimes)


map = [0] * (10 ** 6 + 1)
map[0] = 1
map[1] = 4

for a in range(2, 10 ** 6 + 1, 1):
    map[a] = (map[a - 1] + (num_coprimes2(a) * 2))

print('begin input:\n')

for line in sys.stdin:
    print(map[int(line)])