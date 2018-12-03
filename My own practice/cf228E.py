inputs = [int(x) for x in input().split(' ')]
number_cities = inputs[0]
number_roads = inputs[1]
graph = {}
for i in range(number_roads):
    inputs = [int(x) for x in input().split(' ')]
    fro = inputs[0]
    to = inputs[1]
    state = inputs[2]
    if state: 
        if fro in graph:
            graph[fro].append((to,state))
            graph[-1*fro].
        else:
            graph[fro] = []
            graph[fro].append((to,state))
        if to in graph:
            graph[to].append((fro,state))
        else:
            graph[to] = []
            graph[to].append((fro,state))
    
print(graph)
def dfs(node):
    connected = graph[node]
    for i in connected:
        if i is not in visited:
            dfs(i)


