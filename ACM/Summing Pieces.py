# https://www.hackerrank.com/challenges/summing-pieces
# https://www.hackerrank.com/challenges/substring-diff
# https://www.hackerrank.com/challenges/wet-shark-and-two-subsequences
n = int(input())
s = input().split()
dict = {}
''' RIGHT BUT TOO SLOW
def g(a):
    sums = 0
    for i in a:
        sums += int(i)

    return sums
def f(current):
    if len(current) == 0:
        return 0
    elif len(current) == 1:
        return int(current[0])
    else:
        sums = 0
        #if current in dict:
            #sums = dict[current]
        #else:
        for i in range(1, len(current)+1):
            front = current[:i]
            back = current[i:]
            result = g(front) * len(front)
            b = len(back)-1
            if b == -1:
                b = 0
            sums += result * 2**(b) + f(back)
        #dict[current] = sums
        return sums
print(f(s))
'''
