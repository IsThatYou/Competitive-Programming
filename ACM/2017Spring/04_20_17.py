#https://www.hackerrank.com/challenges/primsmstsub <<-- finished. MST
#https://www.hackerrank.com/challenges/torque-and-development <<-- make a library node
from queue import PriorityQueue
def f():
     N,M = [int(i) for i in input().split()]
     edges = {}
     for i in range(M):
         x,y,r = [int(j) for j in input().split()]
         if x not in edges:
             edges[x] = []
         if y not in edges:
             edges[y] = []
         edges[x].append((y,r))
         edges[y].append((x,r))
     start = int(input())
     q = PriorityQueue()
     for i in edges[start]:
         q.put((i[1], start,i[0]))
     found = set()
     found.add(start)
     totalweight = 0
     while not q.empty():
         cheap = q.get()
         if cheap[2] not in found:
             found.add(cheap[2])
             totalweight+=cheap[0]
             for i in edges[cheap[2]]:
                 q.put((i[1], start, i[0]))
     print(totalweight)

f()
def s():
    pass
#s()