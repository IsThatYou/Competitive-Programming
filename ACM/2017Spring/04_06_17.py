#https://www.hackerrank.com/challenges/the-quickest-way-up <<-- finished, bfs, a bit special
#https://www.hackerrank.com/challenges/even-tree
#https://www.hackerrank.com/challenges/torque-and-development
def bfs(lad, snak):
    #help f()
    if 1 in lad.keys():
        toExplore = [lad[1]]
    else:
        toExplore = [1]
    found = set()
    distance = 0
    while len(toExplore) > 0:
        newExplore = []
        for z in toExplore:
            found.add(z)
            #print(z)
            if z + 6 >= 100:
                if z != 100:
                    distance += 1
                return distance
            for i in range(1,7):
                add = z + i
                if add in lad.keys():
                    add = lad[add]
                if add in snak.keys():
                    add = snak[add]
                if add not in found:
                    newExplore.append(add)
                found.add(add)

        toExplore = newExplore
        distance+=1

def f():
   t = int(input())
   for i in range(t):
       n = int(input())
       lad = {}
       for j in range(n):
           start, end = [int(z) for z in input().split()]
           lad[start] = end
       m = int(input())
       snak = {}
       for j in range(m):
           start, end = [int(z) for z in input().split()]
           snak[start] = end

       a = bfs(lad, snak)
       if a == None:
           print(-1)
       else:
           print(a)
#f()
def len_tree(edges, s, w):
    #using bfs
    found = set()
    found.add(w)
    toexplore = [s]
    #while len(toexplore)!=
def len_tree2(edges, s,w):
    sums = 0

    for i in edges[s-1]:
        if i in w:
            continue
        else:
            sums += 1 + len_tree2(edges, i, 0)
    return sums
def bfs2(edges):
    # helper for s
    toExplore = [1]
    found = set()
    distance = 0
    while len(toExplore)!=0:
        for i in toExplore:
            for j in edges[i-1]:
                iset = set()
                iset.add(i)
                jset = set()
                jset.add(j)
                a = len_tree2(edges, i, jset)
                b = len_tree2(edges, j, iset)
def s():
    n, m = [int(i) for i in input().split()]
    edges = [[] for i in range(n)]
    for i in range(m):
        u, v = [int(j) for j in input().split()]
        edges[u-1].append(v)
        edges[v-1].append(u)
    print(edges)
    print(len_tree2(edges, 1, 6))
    #a = bfs2(edges)

s()