
n, m = input().split()
n = int(n)
m = int(m)

def winner(turn):
    if turn:
        return 'win'
    else:
        return 'lose'
dp = {}
#import profile

def run_game(ss1, ss2, my_turn):
    s1 = max(ss1,ss2)
    s2 = min(ss1,ss2)

    #print(s1, s2)
    if s1 == s2:
        result = winner(my_turn)
        return result
    elif s1 % s2 == 0:
        result = winner(my_turn)
        return result
    else:
        if (str(s1)+str(s2)+str(my_turn)) in dp:
            return dp[str(s1)+str(s2)+str(my_turn)]
        length = s1//s2
        if my_turn:
            new_turn = False
        else:
            new_turn = True
        if my_turn:
            ns1 = 0
            ns2 = 0
            for i in range(length):
                nss1 = s2
                nss2 = (s1%s2) + i*nss1
                #print(ns1, ns2, my_turn)
                ns1 = max(nss1, nss2)
                ns2 = min(nss1, nss2)

                if run_game(ns1, ns2, new_turn) == 'lose':
                    pass
                else:
                    dp[(str(ns1)+ str(ns2)+str(new_turn))] = 'win'
                    return 'win'
            #dp1[(h1, h2)] = 'lose'
            if (ns1,ns2,my_turn) not in dp:
                dp[(str(ns1)+ str(ns2)+str(new_turn))] = 'lose'
            return 'lose'
        else:
            ns1 = 0
            ns2 = 0
            for i in range(0, length):
                nss1 = s2
                nss2 = (s1 % s2) + i * nss1
                #print(ns1,ns2, my_turn)
                ns1 = max(nss1, nss2)
                ns2 = min(nss1, nss2)

                if run_game(ns1, ns2, new_turn) == 'win':
                    pass
                else:
                    dp[(str(ns1)+ str(ns2)+str(new_turn))] = 'lose'
                    return 'lose'
            if (ns1, ns2, my_turn) not in dp:
                dp[(str(ns1)+ str(ns2)+str(new_turn))] = 'win'
            return 'win'






l = m
r = n
result = run_game(l,r, True)
print(result)
#print(dp)
#main()
#profile.run('main()')


