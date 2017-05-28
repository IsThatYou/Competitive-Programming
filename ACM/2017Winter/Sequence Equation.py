n = input()
p = input().split()
for i in range(1, int(n)+1):
    for q in range(1, int(n)+1):
        if str(i) == p[q-1]:
            index = str(q)
            for j in range(1, int(n)+1):
                if index == p[j-1]:
                    print(j)
