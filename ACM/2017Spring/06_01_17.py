#https://www.hackerrank.com/challenges/pacman-bfs bfs
#https://www.hackerrank.com/challenges/pacman-astar a* search
#https://www.hackerrank.com/challenges/n-puzzle a* search

def neighbors(edges, x,y):
    result =  []
    if x !=0:
        result.append((x-1,y))
    if y != 0:
        result.append((x, y-1))
    if y+1 < len(edges[0]):
        result.append((x,y+1))
    if x+1< len(edges):
        result.append((x+1,y))
    return result
def f():
    x,y = [int(i) for i in input().split()]
    fx,fy = [int(i) for i in input().split()]
    r,c = [int(i) for i in input().split()]
    matrix = []
    for i in range(r):
        a = input()
        matrix.append(a)
    queue = [(x,y)]
    discovered = []
    count = 0
    trace = [[0]*c for i in range(r)]
    trace[x][y] = (x,y)
    while len(queue) != 0:
        item = queue.pop(0)
        if item not in discovered:
            if matrix[item[0]][item[1]] == "-" or matrix[item[0]][item[1]] == "P":
                count+= 1
                for i in neighbors(matrix, item[0], item[1]):
                    queue.append(i)
                    trace[i[0]][i[1]] = item
                discovered.append(item)
            if matrix[item[0]][item[1]] == ".":
                count+=1
                discovered.append(item)
                break
    print(count)
    for i in discovered:
        print(i[0],i[1])
    tracearray = []
    traceback = (fx,fy)
    print(fx,fy)
    counter =0
    print(trace[5][2])
    print(trace[5][3])
    while traceback != (x,y):
        counter+=1
        tracearray.append(traceback)
        traceback = trace[traceback[0]][traceback[1]]
        if counter == 3:

            print(traceback)
            break
    print(len(tracearray))
    tracearray.append((x,y))
    for i in reversed(tracearray):
        print(i[0],i[1])




f()