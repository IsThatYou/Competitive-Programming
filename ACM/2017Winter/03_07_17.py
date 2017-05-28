# https://www.hackerrank.com/challenges/kangaroo <<--finished
# https://www.hackerrank.com/challenges/two-arrays <<-- finished
# https://www.hackerrank.com/challenges/sherlock-and-anagrams

#!/bin/python3

import sys

def Kangaroo():
    x1,v1,x2,v2 = input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
    if x1 > x2:
        dv = v2 - v1
        dx = x1 - x2
        if dv > 0:
            if dx%dv == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif x1 < x2:
        dv = v1 - v2
        dx = x2 - x1
        if dv > 0:
            if dx%dv == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("YES")
#Kangaroo()
def Permuting_two_arrays():
    n = int(input())
    for i in range(n):
        shout = input().split()
        length = int(shout[0])
        k = int(shout[1])
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        a = sorted(a)
        b = sorted(b, reverse = True)
        for i in range(length):
            if a[i] + b[i] <k:
                print("NO")
                break
        else:
            print("YES")
#Permuting_two_arrays()
def Sherlock_and_anagrams():
    n = int(input())
    for i in range(n):
        a = input()
        new = {}
        last = ''
        final = 0
        for j in range(len(a)):
            if a[j] not in new:
                new[a[j]] = [1,0, [j]]
            else:
                new[a[j]][0] += 1
                keep =0
                bino = []
                bint = []
                #print(list(range(new[a[j]][2] +1,j)), list(range(j-1, new[a[j]][2], -1)))
                # check for each instance found before
                for q in new[a[j][2]]:
                    for z,p in zip(list(range(new[a[j]][2] +1,j)), list(range(j-1, new[a[j]][2], -1))):
                        bino.append(a[z])
                        bint.append(a[p])
                        if z>= p:
                            break
                        elif keep >0:
                            print(bino, bint)
                            if sorted(bino) == sorted(bint):
                                final += 1
                        else:
                            if a[z] == a[p]:
                                final += 1
                            else:
                                keep+=1

                new[a[j]][2].append(j)

            if a[j] == last:
                new[a[j]][1] += 1
            last = a[j]
        count = 0
        for item in new:
            numb = new[item][0]
            sums = 0
            for j in range(numb-1, 0,-1):
                sums += j
            sums *= 2
            sums -= new[item][1]
            count += sums
        print(count + final)

Sherlock_and_anagrams()