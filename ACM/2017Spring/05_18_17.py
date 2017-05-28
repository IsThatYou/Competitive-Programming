#https://www.hackerrank.com/challenges/two-strings <-- finished, greedy
#https://www.hackerrank.com/challenges/angry-children <-- finished, greedy,sort
#https://www.hackerrank.com/challenges/weighted-uniform-string <--finished
def f():
    n = int(input())
    for i in range(n):
        fi = input()
        se = input()
        solved = False
        for j in fi:
            if j in se:
                solved = True
                print("YES")
                break
            if solved:
                break
        if not solved:
            print("NO")

#f()
def s():
    n = int(input())
    k = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    diff = 1000000005
    for i in range(n-k+1):
        first = arr[i]
        last = arr[i+k-1]
        dif = last - first
        if dif < diff:
            diff = dif
    print(diff)
#s()
def t():
    s = input()
    n = int(input())
    last = -1
    sums = 0
    superset = set()
    for i in range(len(s)):
        query = s[i]
        if query == last:
            sums += ord(query)-96
            superset.add(sums)
        else:
            sums = 0
            sums += ord(query)-96
            superset.add(sums)
        last = query
    for i in range(n):
        query = int(input())
        if query in superset:
            print("Yes")
        else:
            print("No")

t()