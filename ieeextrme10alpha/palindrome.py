import math
cases = int(input())
def check_even(n):
    if (n % 2 == 0):
        # even
        return True
    else:
    # odd
        return False
def solveeq(wrong, total):
    a = total - wrong
    b = wrong - a
    return a, b
for case in range(cases):
    inp = input().split()
    change = int(inp[0])
    s = inp[1]
    if change > len(s):
        print(0)
        
    elif len(s)//2 == len(s)/2:
        sums = 0
        #even
        half = int(len(s)/2)
        index = []
        for i in range(half):
            if s[i] != s[len(s) - i - 1]:
                index.append(i)
        if len(index) == change:
            sum += math.pow(2, change)
        elif change > len(index):
            correct = half - len(index)
            for j in range(len(index), len(index) * 2+1):
                sub = change - j
                if sub == 0:
                    a,b = solveeq(len(index), change)
                    d = math.factorial(a+b)/math.factorial(max(a,b))
                    t = (math.pow(24,a) * math.pow(2, b))*d
                    sums += t
                if sub > 0:
                    eo = check_even(sub)
                    if (eo):
                        a, b = solveeq(len(index), j)
                        d = math.factorial(a + b) / math.factorial(max(a, b))
                        t = (math.pow(24, a) * math.pow(2,b))*d
                        chance = sub/2
                        factor = 0
                        if chance > correct:
                            factor = 0
                        else:
                            while chance != 0 and chance <= correct:
                                factor += 1
                                chance -= 1
                        sums += factor * 25 * t
        print(int(sums))

    else:
        #odd
        half = len(s) // 2
        index = []
        sums = 0
        for i in range(half):
            if s[i] != s[len(s) - i - 1]:
                index.append(i)
        if change == 1 and len(index) == 0:
            sums += 25
        if len(index) == change:
            c = math.pow(2,change)
            sums += c

        elif change > len(index):

            for j in range(len(index), len(index) * 2+1):
                correct = half - len(index)
                sub = change - j
                if sub == 0:
                    a, b = solveeq(len(index), change)
                    d = math.factorial(a + b) / math.factorial(max(a, b))
                    t = math.pow((math.pow(24,a) * math.pow(2,b)), d)
                    sums += t
                if sub > 0:
                    eo = check_even(sub)
                    if (eo):
                        a, b = solveeq(len(index), j)
                        d = math.factorial(a + b) / math.factorial(max(a, b))
                        t = math.pow((math.pow(24,a) * pow(2,b)), d)
                        chance = sub / 2
                        factor = 0
                        if chance > correct:
                            factor = 0
                        else:
                            while chance != 0 and chance <= correct:
                                factor += 1
                                chance -= 1
                        sums += factor * 25 * t
                    else:
                        a, b = solveeq(len(index), j)
                        d = math.factorial(a + b) / math.factorial(max(a, b))
                        t = (math.pow(24, a) * math.pow(2, b))* d
                        chance = sub // 2
                        factor = 1
                        if chance-1 > correct:
                            factor = 0
                        else:
                            while chance != 0 and chance <= correct + 1:
                                factor += 1
                                chance -= 1
                        sums += factor * 25 * t

        print(int(sums))