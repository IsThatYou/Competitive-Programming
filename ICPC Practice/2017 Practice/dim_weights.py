import math

n = int(input())
graph = {}
for i in range(n):
    name, low, factor = [x for x in input().split()]
    graph[name] = (int(low), int(factor))
while True:
    a = input()
    if a =='':
        break
    a1,a2,a3,w1 = [int(x) for x in a.split()]
    vol = a1 * a2 * a3
    minimum = 10**9
    select = ""
    for i in graph:
        if vol > graph[i][0]:
            new_w = math.ceil(vol/graph[i][1])
            new_w = max(new_w, w1)
            if new_w < minimum:
                minimum = new_w
                select = i
        else:
            new_w = w1
            if new_w < minimum:
                minimum = new_w
                select = i
    

    print(select, minimum)