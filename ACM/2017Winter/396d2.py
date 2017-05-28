#http://codeforces.com/contest/766/problem/B
n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a, reverse = True)
new = []
diff = 1000000000
finish = False
for i in range(2,len(a)):
    if a[i] + a[i-1] > a[i-2]:
        print("YES")
        finish = True
        break

if not finish:
    print("NO")