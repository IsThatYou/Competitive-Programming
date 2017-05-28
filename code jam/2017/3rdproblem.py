import queue
import math
def bfs(n,burn):
    toexplore = queue.PriorityQueue()
    toexplore.put(-1*n)
    a1=-1
    a2=-1
    for i in range(burn):
        a = toexplore.get()
        a = -1*a
        if a%2 == 0:
            a1 = a//2
            a2 = a1-1
        else:
            a1 = a//2
            a2 = a//2
        toexplore.put(-1*a1)
        toexplore.put(-1*a2)
    return (a1,a2)
def log(n, burn2):
    if burn2 ==0:
        b = 0
    else:
        b = int(math.log(burn2,2))
    toexplore = [n]
    for i in range(b):
        newexplore = []
        for a in toexplore:
            if a % 2 == 0:
                a1 = a // 2
                a2 = a1 - 1
            else:
                a1 = a // 2
                a2 = a // 2
            newexplore.append(a1)
            newexplore.append(a2)
        toexplore=newexplore
    lol = burn2-2**b
    ans = sorted(toexplore, reverse=True)
    ans = ans[lol]
    if ans % 2 == 0:
        a3 = ans // 2
        a4 = a3 - 1
    else:
        a3 = ans // 2
        a4 = ans // 2
    return(a3, a4)
a = open('test.txt', 'r')
first = True
counter = 1
b = open("out.txt", "w")
for i in a:
    if first:
        t = int(i.strip())
        first = False
    else:
        n,k = [int(j) for j in i.strip().split()]
        burn = k
        #ans2 = bfs(n, burn)
        ans2 = log(n,burn)
        print(counter)
        b.write("Case #" + str(counter) + ": " + str(ans2[0])+" "+ str(ans2[1]) + "\n")
        counter+=1
a.close()
b.close()