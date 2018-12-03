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
    b  =[]
    found = False
    min = n
    for j in range(1,n+1):
        a = round((j)/n)- floor((j)//n)
        print(a)
        # possible improve by checking during computation
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
    for j in range(len(survey)):
        count = survey[j]
        if ref[count] ==1:
            result += 1
        else:
            w = bisect_right(b, count)
            if w != length:
                index = b[w]

                c = index - count
                if c < remaining:
                    tasks.append(c)
            negatives += 1
    tasks.sort()
    
    create = min * 2
    while remaining >0:

    result -= negatives 