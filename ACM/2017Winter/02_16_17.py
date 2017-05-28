# http://codeforces.com/contest/765/problem/A <<--finished
# http://codeforces.com/contest/765/problem/B <<--finished
# http://codeforces.com/contest/765/problem/C <<--finished
# http://codeforces.com/problemset/problem/765/D

def Neverending_competitions():
    n = int(input())
    home = input()
    for i in range(n):
        new = input()
    if n % 2 == 0:
        return "home"
    else:
        return "contest"
#print(Neverending_competitions())

def Code_obfuscation():
    s = input()
    a = [0] * 26
    okay = True
    for i in s:
        for j in range(ord(i)-97):
            if not a[j]:
                okay = False
                break
        if okay:
            a[ord(i) - 97] = 1
        else:
            break
    if okay:
        print("YES")
    else:
        print("NO")

#Code_obfuscation()

def Table_Tennis_Game_2():
    n = input().split()
    k = int(n[0])
    a = int(n[1])
    b = int(n[2])
    if a >= k and b>=k:
        return int(a/k) + int(b/k)
    elif a % k == 0 and a != 0:
        return int(a/k)
    elif b % k == 0 and b != 0:
        return int(b/k)
    else:
        return -1
#print(Table_Tennis_Game_2())
def Artsem_and_Saunders():
    
