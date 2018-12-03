import Queue
m,n = [int(x) for x in input().split()]
graph = []
for i in range(m):
    line = input()
    line = list(line)
    graph.append(line)
x,y = [int(x) for x in input().split()]

#build a graph
for i in range(m):
    for j in range(n):

def search_and_fill(graph,x,y):
    queue = Queue.queue()
    queue.put((x,y))
    visited = set()
    while True:
        node = queue.get()
        for i in neibhors(node):

    
def neibhors(location):
    x = location[0]
    y = location[1]
    if (x>0 and 
