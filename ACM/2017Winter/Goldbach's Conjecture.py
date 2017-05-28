# http://poj.org/problem?id=2262

import mathhelp

primes = mathhelp.getPrimes(1000000)[0][1:]
first = int(input())
while first != 0:
    done = False
    for i in range(len(primes)):
        prime = primes[i]
        if first-prime in primes:
            done = True
            print("{} = {} + {}".format(first,prime, first-prime))
            break
    first = int(input())
    if not done:
        print("Goldbach's conjecture is wrong.")