#https://www.hackerrank.com/contests/hourrank-17/challenges/gcd-matrix
#!/bin/python3

import sys
def gcd(a, b):
    while (a == 0):
        return b
    return gcd(b%a, a)

n,m,q = input().strip().split(' ')
n,m,q = [int(n),int(m),int(q)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
for a0 in range(q):
    r1,c1,r2,c2 = input().strip().split(' ')
    r1,c1,r2,c2 = [int(r1),int(c1),int(r2),int(c2)]
    arr = set()
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            g = gcd(a[i],b[j])

            arr.add(g)

    print(len(arr))

