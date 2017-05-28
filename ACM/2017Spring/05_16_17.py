#Maxflow problem, ford-fulkerson alogrithm
#maximum biparte matching
#www.hackerrank.com/contests/acmuci-spring-2017-homework/challenges/maxflow
#www.hackerrank.com/challenges/crab-graphs
def f():
    n,k = [int(i) for i in input().split()]
    edges = [[] for i in range(n)]
    for i in range(k):
        a,b = [int(i) for i in input().split()]
        edges[a].append(b)

    final = 0
    while True:
        queue = [(0,0)]
        discorvered = set()
        mem = [-1]*n
        result = []
        while len(queue)!=0:
            a = queue.pop(0)
            last = a[0]
            new = a[1]
            if new not in discorvered:
                mem[new] = last
                if new == n-1:
                    b = new
                    while b != 0:
                        result.append(b)
                        b = mem[b]
                    break
                discorvered.add(new)
                for i in edges[new]:
                    if i not in discorvered:
                        queue.append((new,i))
        if len(result)>0:
            result.sort()
            start = 0
            for i in result:
                edges[start].remove(i)
                start = i
            final +=1
        else:
            break
    print(final)
f()