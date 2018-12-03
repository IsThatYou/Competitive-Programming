
def dfs(first,maxx,m,numb):
    d = 2
    result = case01(m,numb)
    while m**d<=numb:
        a = m**d
        se = 1    
        if first:
            while numb-a*se >= 0:
                result += dfs(False,d,m,numb-a*se)
                se+=1
        else:
            while numb-a*se >= 0 and d <=maxx:
                result += dfs(False,d,m,numb-a*se)
                se+=1
        d+=1
    return(result)
def dfs2(first,maxx,m,numb):
    
    return(result)
def case01(m,numb):
    result = 0
    counter = 0
    while numb+1-m*counter >=0:
        result += numb+1- m*counter
        counter += 1
    return(result)
p = int(input())
for i in range(p):
    a,m,n = [int(x) for x in input().split()]
    numbs = n//m
    result = numbs+1
    counter = 1
    print(dfs(True,2,m,numbs))
    

