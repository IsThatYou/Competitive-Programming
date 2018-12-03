import queue
w, h = [int(x) for x in input().split()]
graph = []
start = 0
for a0 in range(h):
    a = input()
    graph.append(a)
    for j in range(w):
        if a[j] == "P":
            start = (a0,j)

visited = set()
q = queue.Queue()
q.put(start)
s = 0
def neib(node):
    result = []
    if (node[0]-1,node[1]) not in visited:
        result.append((node[0]-1,node[1]))
    if (node[0]+1,node[1]) not in visited:
        result.append((node[0]+1,node[1]))
    if (node[0],node[1]-1) not in visited:
        result.append((node[0],node[1]-1))
    if (node[0],node[1]+1) not in visited:
        result.append((node[0],node[1]+1))
    return result
def bomb(node):
    result = []
    if graph[node[0]-1][node[1]] == "T":
        return True
    if graph[node[0]+1][node[1]] == "T":
        return True
    if graph[node[0]][node[1]-1] == "T":
        return True
    if graph[node[0]][node[1]+1] == "T":
        return True
    return False
while not q.empty():
    node = q.get()
    bombs= False
    if graph[node[0]][node[1]]!="#" and bomb(node):
        bombs = True
    if graph[node[0]][node[1]] == "G":
        
        if node not in visited:
            s += 1
        if (not bombs) and (node not in visited):
            
            visited.add(node)
            for a1 in neib(node):
                q.put(a1)
        visited.add(node)
    elif graph[node[0]][node[1]] == "." or graph[node[0]][node[1]] == "P":
        if (not bombs) and (node not in visited):
            visited.add(node)
            for a1 in neib(node):
                q.put(a1)
    elif graph[node[0]][node[1]] == "#":
        visited.add(node)
        continue
print(s)

