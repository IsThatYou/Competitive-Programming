cases = int(input())

for i in range(cases):
    n = int(input())
    b = input().split()
    for g in range(len(b)):
        b[g] = int(b[g])
    b.sort()
    counter = 0
    ls = [0]*n
    for j in range(len(b)):
        if int(b[j])>j:
            break
        for z in range(int(b[j]),n):
            if ls[z] == 0:
                break
            ls[z] = ls[z] + 1
        ls[j] += 1
    sum = 1
    for q in range(len(ls)):
        sum = (sum * ls[q])%1000000007
    print(sum)
'''
for i in range(cases):
    n = int(input())
    b = input().split()
    ls = [0] * (n+1)
    for j in b:
        ls[int(j)] += 1

    options = ls[0]
    total = 1
    for z in range(1, n):
        total = (total*options)
        options = options - 1 + ls[z]
    print(total)
'''