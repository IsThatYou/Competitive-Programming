# https://www.hackerrank.com/challenges/handshake <<-- finished
# https://www.hackerrank.com/challenges/a-chocolate-fiesta <<-- finished
# https://www.hackerrank.com/challenges/consecutive-subsequences

def Handshake():
    T = int(input().strip())
    for a0 in range(T):
        N = int(input().strip())
        N = N-1
        print(int(int(N+1)*(N/2.0)))
#Handshake()

def A_chocolate_fiesta():
    n = int(input())
    A = input().split()
    MOD = 10**9 + 7
    even = []
    odd = []
    for i in A:
        i = int(i)
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    e = len(even)
    e_len = 1
    for i in range(e):
        e_len = (2 * e_len)%MOD
    e_len = e_len-1
    o = len(odd)-1

    if o > 0:
        o_len = 1
        for i in range(o):
            o_len = (2*o_len)%MOD
        o_len = o_len-1
    else:
        o_len = 0
    #print(o_len)
    result = (e_len+o_len+o_len*e_len)%MOD
    print(result)
#A_chocolate_fiesta()

def Consecutive_subsequence():
    t = int(input())
    for i in range(t):
        n,k = [int(x) for x in input().split()]
        s = input().split()
        newl = []
        first = [0] * k
        first[s[0]%k] += 1
        for i in range(1, len(s)):
            i = int(s[i])
            col = newl[-1]
            index = i%k
            for j in range(k):
                if j == index:
                    if s[j] ==0 :
                        s[j] += 1
Consecutive_subsequence()