#https://www.hackerrank.com/contests/projecteuler/challenges/euler077

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

t = int(input())
memo = [0] * 1000
for i in range(t):
    n = int(input())
    for j in range(2,int(n/2)):
        if isprime(j):

