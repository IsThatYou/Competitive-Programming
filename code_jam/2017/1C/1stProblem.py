import math
t = int(input())
b = open("out.txt", "w")
for i in range(t):
    n,k = [int(j) for j in input().split()]
    pancakes = []
    maxr = 0
    for j in range(n):
        r,h = [int(z) for z in input().split()]
        if (r>maxr):
            maxr = r
        pancakes.append((r,h))
    topsize = 0
    sidesize = 0
    pancakes2=sorted(pancakes, key=lambda x:(x[0], x[0]*x[1]),reverse=True)
    top = pancakes2[0]
    pancakes1=sorted(pancakes2[1:], key=lambda x: x[0] * x[1], reverse = True)

    new = pancakes1[:k]
    new = sorted(new, key = lambda x: x[0], reverse =True)
    print(i, pancakes)
    try:
        bot = new[0]
    except:
        bot=(0,1)
    topsize = (bot[0]**2) *math.pi
    if ((top[0]**2)*math.pi - (bot[0]**2) *math.pi)>(2*math.pi*bot[1]*bot[0] -2*math.pi*top[0]*top[1]):
        try:
            new[-1] = top
        except:
            pass
        topsize = (top[0]**2)*math.pi
    if n==k:
        new = pancakes
    for j in new:
        oh = 2*math.pi*j[0] * j[1]
        sidesize += oh
    b.write("Case #" + str(i+1) + ": " + str(sidesize+topsize) + "\n")

