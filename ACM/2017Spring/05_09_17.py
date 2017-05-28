#www.hackerrank.com/challenges/array-left-rotation <<-- finished
#www.hackerrank.com/challenges/game-of-rotation
#www.hackerrank.com/contests/acmuci-spring-2017-homework/challenges/array-rotation-4 <<-- finished
def f():
    n, k = [int(i) for i in input().split()]
    arr = input().split()
    for i in range(n):
        print(arr[(k+i)%n],end=' ')
#f()

def s():
    n = int(input())
    arr = [int(i) for i in input().split()]
    result = 0
    for i in range(n):
        result += arr[i] * (i+1)
    prefixsums = [0] * n
    prefixsums[0] = arr[0]
    for i in range(1, n):
        prefixsums[i] = prefixsums[i-1] + arr[i]
    maxval = result
    for i in range(1, n):
        newval = result + prefixsums[i-1]* (n-i) - (prefixsums[n-1]-prefixsums[n-i-1]) * i
        if newval > maxval:
            maxval = newval
    print(maxval)

s()
def t():
    n,q = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    k = 0
    for i in range(q):
        q,x = [int(j) for j in input().split()]
        if q == 1:
            k += x

        elif q == 2:
            print(arr[(k+x)%n])
#t()