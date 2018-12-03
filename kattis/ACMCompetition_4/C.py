import queue
n,m = [int(x) for x in input().split()]
arr = [-1] * n
for i in range(n):
    num = int(input())
    arr[i] = num
arrset = {}
for i in range(m):
    fr,to = [int(x) for x in input().split()]
    if fr in arrset:
        arrset[fr].append(to)
    else:
        arrset[fr] = [to]
    if to in arrset:
        arrset[to].append(fr)
    else:
        arrset[to] = [fr]

v = [0] * n
#bfs
def bfs(node):
    visited = set()
    q = queue.Queue()
    q.put(node)
    sums = 0
    while not q.empty():
        node = q.get()
        if node not in visited:
            sums += arr[node]
            v[node] =1 
            visited.add(node)
            for i in arrset[node]:
                    q.put(i)
    return sums

answered = False
for i in range(n):
    if v[i] ==0: 
        result = bfs(i)
        if result !=0:
            print("IMPOSSIBLE")
            answered = True
            break
if not answered:
    print("POSSIBLE")
