#https://www.hackerrank.com/challenges/bfsshortreach <<-- finished
#https://www.hackerrank.com/challenges/dijkstrashortreach
#https://www.hackerrank.com/challenges/beautiful-path
import queue
def find_child(fromto, a):
    childrens = set()
    childrens.add(a)
    for i in fromto:
        if a in i:
            childrens.add(i[0])
            childrens.add(i[1])
    childrens.remove(a)
    return childrens
def Breadth_First_Search_Shortest_Reach():
    n = int(input())
    for i in range(n):
        n,m = [int(i) for i in input().split()]
        fromto = []
        for j in range(m):
            u,v = [int(i) for i in input().split()]
            fromto.append((u,v))
        s = int(input())
        result = [0] * (n)
        toExplore = [s]
        distance = 0
        found = set()
        while len(toExplore)!=0:
            newExplore = set()
            for z in toExplore:
                if z not in found:
                    result[z-1] = distance
                if z not in found:
                    found.add(z)
                    for q in find_child(fromto, z):
                        newExplore.add(q)
            toExplore = newExplore
            distance+=1
        for i in range(len(result)):
            if i != (s-1):
                if result[i] != 0:
                    print(result[i]*6,end=' ')
                else:
                    print(-1,end=' ')
        print()

#Breadth_First_Search_Shortest_Reach()
def find_child2(fromto, a):
    childrens = set()
    for i in fromto:
        if a == i[0]:
            childrens.add((i[2], i[1]))
        if a == i[1]:
            childrens.add((i[2],i[0]))
    childrens.remove(a)
    return childrens

def dijkstra(s, t, childrens):
    distance = 0
    pq = queue.PriorityQueue()
    pq.put((distance, s))
    found = set()
    result = 10**9
    while not pq.empty():
        a = pq.get()
        found.add(a)
        if a[1] == t:
            if a[0] < result:
                result = a[0]
        if a not in found:
            chi = childrens[a[1]]
            for i in chi:
                p = (i[0] + a[0], i[1])
                pq.put(p)

def Dijkstra_Shortest_Reach_2():
    n = int(input())
    for i in range(n):
        n,m = [int(i) for i in input().split()]
        fromto = [[] for x in range(n)]
        for j in range(m):
            x,y,r = [int(d) for d in input().split()]
            fromto[x-1].append((r, y))
            fromto[y - 1].append((r, x))
        s = int(input())
        distance = 0
        results = [-1] * n
        pq = queue.PriorityQueue()
        pq.put((distance,s))
        found = set()
        while not pq.empty():
            new = pq.get()
            found.add(new)
            distance = new[0]
            if results[new[1]-1] > distance:
                results[new[1]-1] = distance
            for i in find_child2(fromto, new[1]):


Dijkstra_Shortest_Reach_2()