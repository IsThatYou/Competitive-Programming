# https://www.hackerrank.com/challenges/birthday-cake-candles <<-- finished.  trivial
# https://www.hackerrank.com/challenges/connected-cell-in-a-grid bfs/dfs, find all the cluster
def f():
    n = int(input().strip())
    height = [int(height_temp) for height_temp in input().strip().split(' ')]
    a = max(height)
    b = height.count(a)
    print(b)
#f()
def edges(matrix, a, b):
    neighbor = []
    for i in range(3):
        for j in range(3):
            if i == 1 and j ==1:
                continue
            else:
                if a + i - 1 >= 0 and b + j -1 >= 0 and a + i -1 < len(matrix) and b + j -1 < len(matrix[0]):
                    neighbor.append((a + i - 1, b + j - 1))
    return neighbor
def s ():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        row = [int(j) for j in input().split()]
        matrix.append(row)
    found = set()
    maxsize = 0
    for i in range(n):
        for j in range(m):
            node = (i, j)
            if node not in found:
                currsize = 1
                queue = [node] #to be explored
                found.add(node)
                while len(queue) >0:
                    newqueue = set()
                    for z in queue:
                        e = edges(matrix, z[0], z[1])
                        for each in e:
                            if each not in found:
                                newqueue.add(each)
                                found.add(each)
                                currsize+=1
                    queue = newqueue
                maxsize = max(maxsize, currsize)
                


s()