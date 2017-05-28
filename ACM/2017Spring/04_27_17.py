#https://www.hackerrank.com/contests/codecracker/challenges/interesting-tree
#https://www.hackerrank.com/contests/101hack33/challenges/longest-path
def depth(node, edges,colors):
    if (node not in edges) or (len(edges[node])==0):
        #depth[node] =0
        return 1
    children = []
    for i in edges[node]:
        children.append(depth(i, edges, colors))

    return max(children)+1
def f():
    n = int(input())
    colors = [int(i) for i in input().split()]
    parents = [int(i) for i in input().split()]
    nodes = {}
    nodes[1] = []
    for i in range(len(parents)):
        parent = parents[i]
        child = i+2
        if parent not in nodes:
            nodes[parent] = []
        if colors[parent-1] and colors[i+1]:
            nodes[parent].append(child)
    maxmax = 0
    for i in range(n):
        o = i+1
        if o in nodes:
            maximum = [0]
            for j in nodes[o]:
                if colors[j-1]:
                    maximum.append(depth(j, nodes,colors))
            if colors[o-1]:
                maximum.append(1)
            sums = 0
            if len(maximum) <2:
                maximum = sorted(maximum, reverse=True)
                sums = maximum[0]
            else:
                maximum = sorted(maximum,reverse = True)
                sums = maximum[0] + maximum[1]
                if sums == 16:
                    print(maximum)
            if sums > maxmax:
                maxmax = sums
    print(maxmax)
f()