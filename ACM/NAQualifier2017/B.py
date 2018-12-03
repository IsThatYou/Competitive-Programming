import queue
n,m,f,s,t = [int(x) for x in input().split()]
graph = {}
for a0 in range(m):
    i,j,c = [int(x) for x in input().split()]
    if i in graph:
        graph[i].append((j,c))
    else:
        graph[i] = [(j,c)]
    if j in graph:
        graph[j].append((i,c))
    else:
        graph[j] = [(i,c)]

graphf = {}
for a1 in range(f):
    u, v = [int(x) for x in input().split()]
    graphf[u] = v
    
if f > 0:
    minn = []
    for a2 in graphf:
        u = a2
        v = graphf[a2]
        newgraph = dict(graph)
        for a3 in newgraph[u]:
            if a3[0] == v:
                newgraph[u].remove(a3)
                break
        for a3 in newgraph[v]:
            if a3[0] == u:
                newgraph[v].remove(a3)
                break
        newgraph[u].append((v,0))
        newgraph[v].append((u,0))
        #print(newgraph) 
        t1 = [50001]*n
        pq = queue.PriorityQueue()
        
        #unvisited = {node: None for node in range(n)} 
        pq.put((0,s,s))
        #unvisited[s] = 0
        #print(unvisited)
        visited = set()
        while True:
            if t in visited:
                break
            #candidates = [node for node in unvisited.items() if node[1] or node[1]==0]
            #print(candidates) 
            
            #newnode, curcost = sorted(candidates, key = lambda x: x[1])[0]
            newnode = pq.get()
            curcost = newnode[0]
            newnode = newnode[1]
            for a4 in newgraph[newnode]:
                dest = a4[0]
                cost = a4[1]
                newcost = curcost + cost
                if dest in visited:
                    continue
                if newcost < t1[dest]:
                    t1[dest] = newcost
                    #unvisited[dest] = newcost
            #del unvisited[newnode]
            visited.add(newnode)
            #if not unvisited:
            #    break
            
        minn.append(t1[t])
    print(min(minn))

else:
    t1 = [50001]*n
    pq = queue.PriorityQueue()
    
    unvisited = {node: None for node in range(n)} 
    #pq.put((0,s,s))
    unvisited[s] = 0
    #print(unvisited)
    visited = set()
    while True:
        if t in visited:
            break
        candidates = [node for node in unvisited.items() if node[1] or node[1]==0]
        #print(candidates) 
        newnode, curcost = sorted(candidates, key = lambda x: x[1])[0]
        #curcost = newnode[0]
        for a4 in graph[newnode]:
            dest = a4[0]
            cost = a4[1]
            newcost = curcost + cost
            if dest not in unvisited:
                continue
            if newcost < t1[dest]:
                t1[dest] = newcost
                unvisited[dest] = newcost
        del unvisited[newnode]
        visited.add(newnode)
        if not unvisited:
            break
        
    print(t1[t])
