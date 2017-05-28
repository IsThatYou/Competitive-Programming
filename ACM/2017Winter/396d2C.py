#http://codeforces.com/contest/766/problem/C
n = int(input())
s = input()
cons = [int(i) for i in input().split()]
long = [1]
lent = [len(s)]
dp = {}
def f(current, length):

    if len(current) == 1:
        if length < lent[-1]:
            lent.append(length)
        return 1
    else:
        sums = 0
        li = cons[ord(current[0])-97]
        if li < len(current):
            for i in range(1, li + 1):
                go = True
                for j in range(1, i):
                    if cons[ord(current[j])-97] < i:
                        go = False
                if go:
                    if current[i:] in dp:
                        result = dp[current[i:]]
                    else:
                        result = f(current[i:], length+1)
                    sums += result
                    if current[i:] not in dp:
                        dp[current[i:]] = result
            return sums
        else:
            for i in range(1, len(current)):
                go = True
                for j in range(1, i):
                    if cons[ord(current[j]) - 97] < i:
                        go = False
                if go:
                    if current[i:] in dp:
                        result = dp[current[i:]]
                    else:
                        result = f(current[i:], length+1)
                    sums += result
                    if current[i:] not in dp:
                        dp[current[i:]] = result
            go2 = True
            for i in current:
                if cons[ord(i) - 97] < len(current):
                    go2 = False
                    break
            if go2:
                if len(current) > long[-1]:
                    long.append(len(current))
                if length < lent[-1]:
                    lent.append(length)
                sums += 1
            return sums

print(f(s,0))
print(long[-1])
print(lent[-1]+1, lent)