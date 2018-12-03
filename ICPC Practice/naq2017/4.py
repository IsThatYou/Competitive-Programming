
def dfs(pos,depth):
    if pos == 1 and depth == 1:
        return (1, 1)
    #elif pos == 1 and depth == 1:
    #    return (1,1)
    newpos = (pos+1)//2
    if not(pos%2):
        a=dfs(newpos, depth-1)
        return (a[0]+a[1],a[1])
    else:
        a=dfs(newpos, depth-1)
        return (a[0],a[0]+a[1])
    
p = int(input())
for i in range(p):
    a,num = [int(x) for x in input().split()]
    d = 0
    for j in range(33):
        if (2**j-1) >= num:
            d = j
            break
    pos = num - 2**(d-1)+1
    result = dfs(pos, d)
    print(str(a) + " " + str(result[0])+ "/" + str(result[1]))

