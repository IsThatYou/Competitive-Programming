# https://www.hackerrank.com/contests/hourrank-18/challenges/wheres-the-marble <<-- finished
# https://www.hackerrank.com/contests/hourrank-18/challenges/super-six-substrings <<--

from functools import reduce
def Wheres_the_marble():
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    for a0 in range(n):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        if a == m:
            m = b
        elif b == m:
            m = a
    print(m)
#Wheres_the_marble()

def Super_six_substrings():
    s = input().strip()
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
        else:
            constructed = s[i]
            if int(constructed)%6 == 0:
                count+=1
            for j in range(i+1, len(s)):
                constructed = constructed+ s[j]
                result = 0
                for z in constructed:
                    result += int(z)
                if int(constructed[-1]) % 2 ==0 and result%3 == 0:
                    count += 1

    #count = sum(all) + sum(zeros)
    print(count)

Super_six_substrings()