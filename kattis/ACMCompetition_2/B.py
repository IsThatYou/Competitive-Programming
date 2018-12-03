while True:
    graph = []
    n = input()
    if n =="-1":
        break
    n = int(n)
    for i in range(n):
        line = [int(x) for x in input().split()]
        graph.append(line)
    if n==1:
        print(0)
    elif n ==2:
        print(0,1)
    else:
        ans = [0 for x in range(n)]
        for i1 in range(n): 
            for j1 in range(len(graph[i1])):
                if graph[i1][j1] ==1 and graph[j1][i1] ==1:
                    for z1 in range(i1,n):
                        if (graph[i1][z1] == 1) and (graph[j1][z1]==1):
                            ans[i1] = 1
                            ans[j1] = 1
                            ans[z1] = 1
        
        for i2 in range(n):
            if ans[i2] == 0:
                print(i2,end=" ")
        print()
