#2016 Greater New York Region ACM Regional Contest
#2017 North American Practice Contest 08
p = int(input())
for i in range(p):
    k, n = [int(x) for x in input().split()]
    array = []
    for j in range(n//10 +1):
        array += [int(x) for x in input().split()]
    comp = sorted(array)
    counter =0
    for j in range(n):
        if array[j] == comp[counter]:
                counter += 1
    print(k,n-counter)
