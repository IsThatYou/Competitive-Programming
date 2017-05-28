#https://www.hackerrank.com/contests/w28/challenges/the-great-xor
#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = 0
    for i in range(1, x):
        if x^i > x:
            result += 1
    print(result)

    # smart way
    #
    #x^(1<<flour(log(x)+1)-1)

