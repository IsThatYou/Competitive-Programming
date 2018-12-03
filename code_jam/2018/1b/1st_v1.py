import math

def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
t = int(input())
for i in range(t):
    n,l = [int(x) for x in input().split()]
    survey = [int(x) for x in input().split()]
    remaining = n - sum(survey)
    ref = [0] * (n+1)
    ref_dif = [0] * (n+1)
    b  =[]
    found = False
    min = n
    for j in range(1,n+1):
        a = int(((j/n)*100)+0.5) -  math.floor(((j)/n)*100)
        c = abs(((j/n)*100)-int(((j/n)*100)+0.5))
       
        # possible improve by checking during computation
        ref_dif[j] = c
        if a == 0:
            ref[j] = -1
            
        else:
            if not found:
                min = j
                found = True
            ref[j] = 1
            b.append(j)
    length = len(b)
    result = 0
    negatives = 0
    tasks = []
    create = min 
    for j in range(len(survey)):
        count = survey[j]
        if ref[count] ==1:
            
            result += ref_dif[count]
        else:
            w = bisect_right(b, count)
            if w != length:
                index = b[w]

                c = index - count
                if (c <= remaining) and (c<create):
                    tasks.append((c,count))
                else:
                    result -=ref_dif[count]
            
    
    
    
    tasks.append((create,0))
    tasks.sort(key=lambda tup: tup[0])
    curindex = 0
    lentask = len(tasks)
    print(remaining)
    while remaining >0:
        cur = tasks[curindex]
        done = False
        if cur[0] <= remaining:
            result += ref_dif[cur[0] + cur[1]]
            print("rua")
            print(result)
            remaining -= cur[0]
            curindex +=1
            done = True
            if curindex == lentask:
                curindex -=1
        else:
            result -= ref_dif[remaining]
            break

    if not done:
        while curindex< lentask:
            wa = tasks[curindex] 
            result -= ref_dif[wa[0] + wa[1]]
            curindex += 1
    if result<0:
        print(result)
        print(int(abs(result)+0.5))
        result = 100- int(abs(result)+0.5)
        
    else:
        result = 100+int(result+0.5)
    
    print("Case #%d: %d" %(i+1, result))