#https://www.hackerrank.com/contests/hourrank-17/challenges/the-hurdle-race
#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
m = max(height)
if m > k:
    print(m-k)
else:
    print(0)

