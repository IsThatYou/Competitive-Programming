#www.hackerrank.com/challenges/flatland-space-stations <<- finished
#www.hackerrank.com/challenges/sherlock-and-valid-string <<- finished
#www.hackerrank.com/challenges/greedy-florist <<- finished
def f():
    n,m = [int(i) for i in input().split()]
    ss = [int(i) for i in input().split()]
    ss=sorted(ss,reverse = True)
    ss1 = ss[:]
    last = ss.pop()
    if len(ss) == 0:
        next = n
    else:
        next = ss.pop()
    result = [n]*n
    for i in range(n):
        if len(ss) != 0:
            if i!=n and i>=next:
                last = next
                next = ss.pop()
        else:
            if i != n and i >= next:
                last = next


        sub = i-last
        if sub >=0:
            result[i] = sub

    last = ss1.pop(0)
    if len(ss1) == 0:
        next = -1
    else:
        next = ss1.pop(0)
    for i in range(n-1, -1,-1):
        if len(ss1) != 0:
            if i!=-1 and i<=next:
                last = next
                next = ss1.pop(0)
        else:
            if i != -1 and i <= next:
                last = next
        sub = last-i
        if sub >=0 and sub<result[i]:
            result[i] = sub
    print(max(result))


#f()
def s():
    s = input()
    arr = list(s)
    rua = [0] * 26
    for char in arr:
        rua[ord(char)-97] +=1
    printed = False
    for i in range(26):
        if rua[i] >0:
            temp = list(rua)
            temp2 = list(rua)
            temp2 = list(filter(lambda x: x!=0, temp2))
            if max(temp2) == min(temp2):
                print("YES")
                printed = True
                break
            temp[i] -=1
            temp = list(filter(lambda x: x!=0, temp))
            if max(temp) == min(temp):
                print("YES")
                printed = True
                break
    if printed:
        pass
    else:
        print("NO")

#s()

def t():
    n,k = [int(i) for i in input().split()]
    cost = [int(i) for i in input().split()]
    cost = sorted(cost,reverse = True)
    multiplier = 0
    totalcost = 0
    for i in range(n):
        if i%k ==0:
            multiplier+=1
        totalcost += multiplier * cost[i]
    print(totalcost)
t()