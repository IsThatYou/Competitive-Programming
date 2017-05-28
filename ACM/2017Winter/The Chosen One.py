# unfinished
# unfinished
#!/bin/python3

import sys
# TOO SLOWWWW W W W WWWW WWWWW
def factor(a):
    results = []
    for i in range(2, int(a/2)+1):
        if a % i == 0:
           results.append(i)
    results.append(a)
    return results
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
dic = {}
for i in range(n):
    interested = a[i]
    factors = factor(interested)
    for j in factors:
        group = dic.setdefault(j, [])
        group.append(i)
for i in dic:
    if len(dic[i])+1 == n:
        print(i)
        break


