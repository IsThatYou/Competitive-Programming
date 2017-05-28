inpu = input().split()
n = int(inpu[0])
k = int(inpu[1])
if k > n:
    print(-1)
elif k==2 and n>k:
    print(-1)
else:
    n1 = n-2
    k1 = k-2-1
    n2 = n1-k1
    result = k1 + n2*2
    print(result)


