n = int(input())
m = int(input())
graph = [[0]*n for i in range(n)]
for i in range(m):
    x,y,w = [int(x) for x in input().split()]
    count = w
    square = 1
    cc = 0
    number = 1
    while count!=0:
        x1 = x-cc
        y1 = y-cc
        loca_c = 0
        for j in range(number):
            if square == 1:
                graph[x1][y1] +=count
            else:
                if loca_c == 0:
                    x1 += 1
                    if x1 >=0 and x1 <n and y1>=0 and y1<n:
                        graph[x1][y1] +=count
                    
                if loca_c == 1:
                    y1 += 1
                    if x1 >=0 and x1 <n and y1>=0 and y1<n:
                        graph[x1][y1] +=count

                if loca_c == 2:
                    x1 -= 1
                    if x1 >=0 and x1 <n and y1>=0 and y1<n:
                        graph[x1][y1] +=count

                if loca_c == 3:
                    y1 -= 1
                    if x1 >=0 and x1 <n and y1>=0 and y1<n:
                        graph[x1][y1] +=count
            if square == 1:
                loca_c +=1
            elif (j+1)%(square-1)==0:
                loca_c +=1
        

        square = square + 2
        number = square**2 - (square-2)**2
        count-=1
        cc+=1
maximum = 0
for i in graph:
    for j in i:
        if j > maximum:
            maximum = j
print(maximum)
