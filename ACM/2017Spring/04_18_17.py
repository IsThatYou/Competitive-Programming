#https://www.hackerrank.com/challenges/qheap1 <<-- finished, using 2 pq
#https://www.hackerrank.com/challenges/jesse-and-cookies
#https://www.hackerrank.com/challenges/minimum-average-waiting-time
from queue import PriorityQueue
def f():
    q = PriorityQueue()
    n = int(input())
    keep = PriorityQueue()
    for i in range(n):

        a = input().strip()
        if len(a) == 1:
            a = int(a)
            c = q.get()
            print(c)
            q.put(c)
        else:
            cmd,val = [int(j) for j in a.split()]
            if cmd == 1:
                q.put(val)
            elif cmd == 2:
                b = q.get()
                if val ==b:
                    while not keep.empty():
                        c = q.get()
                        d = keep.get()
                        if c != d:
                            q.put(c)
                            keep.put(d)
                            break
                else:
                    q.put(b)
                    keep.put(val)
#f()
def s():
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    q = PriorityQueue()
    for i in a:
        q.put(i)
    b = q.get()
    count =0
    d = False
    if b < k:
        c =-1
        q.put(b)
        while not q.empty():
            b = q.get()
            c = q.get()
            if b<k:
                new = b + 2 * c
                q.put(new)
                count += 1
            else:
                break
        if b < k:
            print(-1)
            d = True
    if not d:
        print(count)

s()