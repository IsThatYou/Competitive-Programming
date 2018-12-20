
# Python program to print prime factors 
import math 
def primeFactors(n): 
    # Print the number of two's that divide n 
    dic = {}
    while n % 2 == 0: 
        if 2 in dic:
            dic[2] += 1
        else:
            dic[2] = 1
        n = n / 2 
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            n = n / i 
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    return dic
n = int(input())
arr = primeFactors(n)
arr2 = []
for key in arr:
    arr2.append(arr[key])
length = len(arr2)
ans = 0
#print("ura")
while True:
    sqrt = True
    if len(arr2) == 0:
        break
    for i in arr2:
        if i%2 == 1:
            sqrt = False
            break
    if sqrt:
        ans += 1
        for i in range(length):
            arr2[i] = arr2[i]/2
    else:
        break
p = 0
start = 1
if len(arr2) ==0:
    a = 1
else:
    a = max(arr2)
for i in range(1000):
    if start<a:
        start *= 2
        p += 1
    else:
        break
plus1 = False
for i in range(length):
    if arr2[i] <start:
        plus1 = True
        break
if plus1:
    ans += p + 1
else:
    ans += p
ans0 = 1
for i in arr:
    ans0 *= i
print(int(ans0),ans)