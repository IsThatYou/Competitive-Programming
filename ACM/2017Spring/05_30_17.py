#https://open.kattis.com/problems/improbable     maximum biparthite matching
#https://open.kattis.com/problems/visual
def f():
    r,c = [int(i) for i in input().split()]
    arr = []
    for i in range(r):
        a = [int(j) for j in input().split()]
        arr.append(a)
    side = []
    side1  = [1] * r
    sideindex = []
    for i in range(r):
        b = max(arr[i])
        sideindex.append((i,arr[i].index(b)))
        side.append(b)
    front = []
    frontindex = []
    front1 = [1] * c
    for i in range(c):
        brr = []
        for j in range(r):
            brr.append(arr[j][i])
        b = max(brr)
        front.append(b)
        for j in range(r):
            if arr[j][i] == b:
                frontindex.append((j,i))
                break
    print(frontindex)
    #for i in range(r):
    #    for j in range(c):


f()