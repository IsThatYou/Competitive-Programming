import operator
a = "qwertyuiop"
b = "asdfghjkl"
r = "zxcvbnm"
dick = {}
for i,c in enumerate(a):
    dick[c] = (0,i)
for i,c in enumerate(b):
    dick[c] = (1,i)
for i,c in enumerate(r):
    dick[c] = (2,i)
def distance(s1,s2):
    f = dick[s1]
    s = dick[s2]
    return abs((f[0]-s[0]))+abs((f[1]-s[1]))
def distance1(s1,s2):
    sums = 0
    for i,c in zip(s1,s2):
        f = distance(i,c)
        sums += f
    return sums

cases = int(input())
for i in range(cases):
    a=input().split()
    std,n = a
    n = int(n)
    results = []
    for j in range(n):
        comparee = input().strip()
        result = distance1(std,comparee)
        results.append((comparee,result))
    results = sorted(results,key=operator.itemgetter(1,0))
    
    for j in results:
        print(j[0],j[1])


