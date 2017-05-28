#!/bin/python3
#https://www.hackerrank.com/contests/codeagon/challenges/elemental-orbs

import sys


s = int(input().strip())
for a0 in range(s):
    n,e = input().strip().split(' ')
    n,e = [int(n),int(e)]
    b = list(map(int, input().strip().split(' ')))
    # your code goes here
