case = int(input())
# have a visited node list to keep track

def check(nodes, num):
    visited = set()
    start = nodes[0][0]
    to = nodes[0][1]
    del nodes[0]
    visited.add(start)
    visited.add(to)
    while True:
        if len(visited) == num:
            return True
        else:
            count = 0
            for i in range(len(nodes)):
                if to == nodes[i][0]:
                    to = nodes[i][1]
                    visited.add(to)
                    del nodes[i]
                    count += 1
                    break
            if count == 0:
                return False


for i in range(case):
    a = input().split()
    b = int(a[0])
    c = int(a[1])
    visited = []
    nodes = []
    reverse_nodes = []
    distinct = set()
    for j in range(c):
        d = input().split()
        start = d[0]
        end = d[1]
        distinct.add(start)
        distinct.add(end)
        nodes.append((start,end))
        reverse_nodes.append((end, start))
    if check(nodes, len(distinct)) and check(reverse_nodes, len(distinct)):
        print("Gotta Catch Them All!")
    else:

        print("Oh! Oh!")
