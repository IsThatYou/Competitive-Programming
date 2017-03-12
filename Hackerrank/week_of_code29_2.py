# https://www.hackerrank.com/contests/w29/challenges/big-sorting
#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
new = sorted(unsorted, key=lambda x: (len(x),x))
for i in new:
	print(i)
