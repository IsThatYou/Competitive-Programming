k = int(input())
graph = {}
a = 1
while True:
    b = input()
    if b== "-1":
        break
    a = [int(x) for x in b.split()]
    parent = a[0]
    for j in a[1:]:
        graph[j] = parent
lis = [k]
while True:
    nex = graph[k]
    lis.append(nex)
    if nex in graph:
        k = nex
    else:
        break
for i in lis:
    print(i,end=" ")
print()
