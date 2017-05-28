# http://codeforces.com/contest/779/problem/A <<--finsihed
# http://codeforces.com/contest/779/problem/B <<--finished
# http://codeforces.com/contest/779/problem/C <<--finished
# http://codeforces.com/contest/779/problem/D
def Pupils_redistribution():
    n = int(input())
    g1 = input().split()
    g1d = [0]*5
    g2 = input().split()
    g2d = [0]*5
    for i in g1:
        g1d[int(i)-1] += 1
    for i in g2:
        g2d[int(i)-1] += 1
    nd = [0] * 5
    for i in range(len(g1d)):
        a = g1d[i]-g2d[i]
        if a%2 == 0:
            nd[i] = a/2
        else:
            print("-1")
            break
    else:
        if sum(nd) ==0:
            sums = 0
            for i in nd:
                if i >0:
                    sums += i
            print(int(sums))
        else:
            print("-1")
#Pupils_redistribution()
def Weird_rounding():
    r= input().split()

    n = r[0]
    lenn = len(n)
    n2 = n
    k = int(r[1])
    ten = 10**k
    count = 0
    for i in range(lenn):
        if int(n2) % ten == 0:
            break
        if int(n2[lenn-i-1]) != 0:
            count += 1
            n2 = n2[:(lenn-i-1)] + n2[(lenn-i):]
    if int(n2) == 0 and len(n2) >1:
        print(count + len(n2) - 1)
    else:
        print(count)
#Weird_rounding()

## quick select for kth smallest  linear time
def Dishonest_sellers():
    a = input().split()
    n = int(a[0])
    k = int(a[1])
    a = input().split()
    b = input().split()
    diff = [0] * n
    for i in range(n):
        diff[i] = (int(b[i]) - int(a[i]),i)
    diff = sorted(diff, reverse = True)
    count = 0
    for i in range(n):
        if i < k:
            count += int(a[diff[i][1]])
        else:
            if diff[i][0] >= 0:
                count += int(a[diff[i][1]])
            else:
                count+= int(b[diff[i][1]])
    print(count)
#Dishonest_sellers()
def String_game():
    t = input()
    p = input()
    order = input().split()

String_game()