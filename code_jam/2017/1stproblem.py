# bfs is too slow, I suspect this problem can be solved with other algos
def bfs(arr,k):
    toexplore = []
    toexplore.append(arr)
    found = set()
    distance = 0
    length = len(arr)
    while len(toexplore) != 0:
        newexplore = []
        for i in toexplore:
            if i not in found:
                found.add(i)
                if i == "+" * length:
                    return distance
                else:
                    dic = [[] for q in range(k+1)]
                    for j in range(length-k+1):
                        count = 0
                        newl = list(i)
                        for z in range(j,j+k):
                            if newl[z] =='-':
                                newl[z] = '+'
                                count += 1
                            elif newl[z] =='+':
                                newl[z] = '-'
                        dic[count].append(''.join(newl))
                    for j in range(k, -1,-1):
                        if len(dic[j]) != 0:
                            for z in dic[j]:
                                newexplore.append(z)
        distance+=1
        toexplore = newexplore

a = open('A-large.in', 'r')
first = True
counter = 1
b = open("out.txt", "w")
for i in a:
    if first:
        t = int(i.strip())
        first = False
    else:
        print(counter)
        new = i.strip().split()
        arr = new[0]
        k = int(new[1])
        answer = bfs(arr,k)
        if answer == None:
            b.write("Case #" + str(counter) + ": " + "IMPOSSIBLE" + "\n")
        else:
            b.write("Case #" + str(counter) +": "+ str(answer) + "\n")
        counter += 1