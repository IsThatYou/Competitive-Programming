#https://www.hackerrank.com/contests/hourrank-17/challenges/organizing-containers-of-balls
#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    num_type = [0]*n
    num_con = [0]*n
    for count, i in enumerate(M):
        for count2, j in enumerate(i):
            num_con[count] += j
            num_type[count2] += j
    solved = False
    for i in num_type:
        solved = False
        for count, j in enumerate(num_con):
            if i == j:
                num_con[count] = -1
                solved = True
                break
        if solved == False:
            break
    if solved == False:
        print("Impossible")
    else:
        print("Possible")

