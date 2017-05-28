#!/bin/python3
#https://www.hackerrank.com/contests/codeagon/challenges/matchstick-warehouse-thief

import sys


n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
crate = []
for crate_i in range(c):
   crate_t = [int(crate_temp) for crate_temp in input().strip().split(' ')]
   crate.append(crate_t)
crate = sorted(crate, key = lambda x: x[1], reverse = True)
result = 0
for i in range(len(crate)):
    new_n = n - crate[i][0]
    if new_n >= 0:
        result += crate[i][0] * crate[i][1]
        n = new_n
    else:
        result += n * crate[i][1]
        break
print(result)

