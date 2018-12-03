import math
m = int(1e9 + 7)
n,q = [int(x) for x in input().split()]
arr = [int(x) for x in input().strip()]
def iterative_power(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            #print(result,base,power)
            result = (result * base) % m
            #print(result)

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        #print(base,base*base)
        base = (base * base) % m

    return result
for i in range(q):
    l,r = [int(x) for x in input().split()]
    length = r-l+1
    sums =0
    for j in range(l-1,r):
        sums += arr[j]
    begin = length
    ans = 0
    mult = 0.5
    a = iterative_power(2,sums)%m
    ans = (ans+a-1)%m
    mult = (a/2) + (a/2)-1
    #print(ans,mult)
    #print(length,sums)
    b = iterative_power(2,length-sums)%m
    if b<1:
        c = 0
    else:
        c = ((b-1) * mult)%m
        #print(mult,c)
    ans = (ans+c)%m
    print(int(ans))
