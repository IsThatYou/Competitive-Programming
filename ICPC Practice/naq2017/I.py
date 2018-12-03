import sys
from multiprocessing import Process
import time
where = ["down","right", "up", "left"]
def callhit(n):
    direction = where[n]
    print(direction)
    sys.stdout.flush()
    a = input()
    if a =="ok":
        return(direction)
    if a== "solved":
        sys.exit()
        return("solved")
    if a== "wrong":
        sys.exit()
    return("wall")
def alleq(n):
    if n[0] ==n[1] and n[1] ==n[2] and n[2] ==n[3]:
        return True
    return False
def checkloop(track, direcs,counts,graph):
    c = counts[:]
    if c[0] !=0:
        if alleq(c):
            graph[1][where.index(direcs[-1])-2] = -1
            return True
        for i in range(len(direcs)):
            c[where.index(direcs[i])] -=1
            if alleq(c) and c[0]!=0:
                graph[i+1][where.index(direcs[-1])-2] = -1
                
                return True

        return False
def main():
    graph = {}
    track = [1]
    direcs = []
    counts = [0,0,0,0]
    counter = 1
    cur = counter
    last = 0
    solved = False
    while not solved:
        cur = track[-1]
        #print(cur, last)
        if cur not in graph:
            
            graph[cur] = [0,0,0,0]
            if last:
                graph[cur][where.index(last)] = 1
            
        next_node = "wall"
        for i in range(4):
            if graph[cur][i] == 0:
                next_node = callhit(i)
                if next_node != last and next_node != "wall":
                    graph[cur][i] = 1
                    counts[where.index(next_node)] += 1
                    last = where[where.index(next_node)-2]
                    direcs.append(next_node)
                    counter += 1
                    track.append(counter)
                    break
                if next_node == "wall":
                    graph[cur][i] = -1
            
        #print("rua1", alleq(counts))
        #print(track,direcs)
        if next_node == "wall" or(checkloop(track,direcs,counts,graph)):
            if len(track) == 1:
                print("no way out")
                sys.stdout.flush()
                sys.exit()
                break
            a = track.pop()
            c = direcs.pop()
            
            counts[where.index(c)] -= 1
            graph[track[-1]][where.index(c)] = -1
            print(where[where.index(c)-2])
            sys.stdout.flush()
            b = input()
            if b != "ok":
                print("no way out")
                sys.stdout.flush()
                sys.exit()
                break
            last = where[where.index(c)]
main()
#action_process = Process(target =main())
#action_process.start()
#action_process.join(timeout=2)
#action_process.terminate()
#print("no way out")
    



        
