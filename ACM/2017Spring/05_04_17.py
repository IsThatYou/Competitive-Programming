#http://codeforces.com/contest/803
#A <<- finished, constructive algorithm 
#B <<- finished, shortest path
#D
import math
def A():
    n,k = [int(i) for i in input().split()]
    new = [[0]*n for i in range(n)]
    count = 0
    for i in range(n, 0, -1):
        if k<=0:
            break
        k-=1
        new[count][n-i] = 1
        if k <= 0:
            break
        for j in range(n-i+1, n):
            if k-2 >= 0:
                k-=2
                new[count][j] = 1
                new[j][count] = 1

            else:
                break
        if k<=0:
            break
        count+=1
    if k > 0:
        print("-1")
    else:
        for i in new:
            for j in i:
                print(j,end=' ')
            print()
#A()
def B():
    n = int(input())
    arr = input().split()
    result = [0] * n
    death_count = 1
    last_index = -1
    for each in range(n):
        if arr[each] == '0':
            death_count+=1
            if death_count ==2:
                death_count -=1
                inbetween = each - last_index-1
                if last_index != -1:
                    if inbetween >0:
                        for i in range(math.ceil(inbetween/2)):
                            result[last_index+i+1] = i+1
                            result[each-i-1]=i+1
                else:
                    for i in range(each):
                        result[i] = each-i
                last_index = each
    huo = 1
    for i in range(last_index+1, n):
        result[i] = huo
        huo+=1
    for i in result:
        print(i, end=' ')


B()