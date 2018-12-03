n = int(input())
d = input()
y,x = [int(x) for x in input().split()]
graph = [[0]*n for i in range(n)]
graph[x][y] = 1
result = [[0]*n for i in range(n)]
result[x][y] = 1
made_move = 2
while True:
    
    if d == 's':
        if (y+1)<n and graph[x][y+1] == 0:
            y+=1
            graph[x][y] = 1
            result[x][y] = made_move
            made_move += 1
        else:
            if (x-1)>=0 and graph[x-1][y] ==0:
                x-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (x+1)<n and graph[x+1][y] ==0:
                x+=1 
                graph[x][y] = 1
                
                result[x][y] = made_move
                made_move += 1
            elif (y-1)>=0 and graph[x][y-1] ==0:
                y-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            else:
                break
    elif d == 'n':
        if (y-1)>=0 and graph[x][y-1] == 0:
            y-=1
            graph[x][y] = 1
            result[x][y] = made_move
            made_move += 1
        else:
            if (x-1)>=0 and graph[x-1][y] ==0:
                x-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (x+1)<n and graph[x+1][y] ==0:
                x+=1 
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (y+1)<n and graph[x][y+1] ==0:
                y+=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            else:
                break
    elif d == 'e':
        if (x+1)<n and graph[x+1][y] == 0:
            x+=1
            graph[x][y] = 1
            result[x][y] = made_move
            made_move += 1
        else:
            if (y-1)>=0 and graph[x][y-1] ==0:
                y-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (y+1)<n and graph[x][y+1] ==0:
                y+=1 
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (x-1)>=0 and graph[x-1][y] ==0:
                x-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            else:
                break
    elif d == 'w':
        if (x-1)>=0 and graph[x-1][y] == 0:
            x-=1
            graph[x][y] = 1
            result[x][y] = made_move
            made_move += 1
        else:
            if (y-1)>=0 and graph[x][y-1] ==0:
                y-=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (y+1)<n and graph[x][y+1] ==0:
                y+=1 
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            elif (x+1)<n and graph[x+1][y] ==0:
                x+=1
                graph[x][y] = 1
                result[x][y] = made_move
                made_move += 1
            else:
                break
#print(result)
for i in range(n):
    for j in range(n):
        print(result[j][i],end=' ')
    print()
