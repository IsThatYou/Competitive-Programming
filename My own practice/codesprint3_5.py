import sys

sys.setrecursionlimit(2000)
n = int(input())
c = list(map(int,input().split()))
graph = {}
for a0 in range(n-1):
    x, y = input().split()
    x, y = [int(x),int(y)]
    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = []
        graph[x].append(y)
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = []
        graph[y].append(x)

def lookfor(node):
    subnodes = graph[node]
    sums = -2 *c[node-1] + 1
    visited[node-1] = 1
    included = set()
    included.add(node)
    for i in subnodes:
        if visited[i-1] == 0:
            val = lookfor(i)
            if val[1] >0:
                sums += val[1]
                included.update(val[0])
    if sums >0:
        return (included, sums)
    else:
        #change something later
        return (included,sums)
def lookfor2(node):
    subnodes = graph[node]
    sums = -1*(-2 *c[node-1] + 1)
    visited[node-1] = 1
    included = set()
    included.add(node)
    for i in subnodes:
        if visited[i-1] == 0:
            val = lookfor2(i)
            if val[1] >0:
                sums += val[1]
                included.update(val[0])
    if sums >0:
        return (included, sums)
    else:
        #change something later
        return (included,sums)
maximum = 0
dongxi = set()
for a1 in range(n):
    if c[a1] == 0:
        node = a1 + 1
        visited = [0] * n
        strange = lookfor(node)
        if strange[1] > maximum:
            maximum = strange[1]
            dongxi = strange[0]
    else:
        node = a1 + 1
        visited = [0] * n
        strange = lookfor2(node)
        print(strange)
        if strange[1] > maximum:
            maximum = strange[1]
            dongxi = strange[0]

print(maximum)
print(len(dongxi))
for i in dongxi:
    print(i,end=' ')
print()

