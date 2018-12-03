# Written by Junlin Wang
# Pyton 2.7

d1 = input('divisble by:')
d2 = input('divisble by:')
digit = input('how many digits:')

# fisrt method (faster)
def gcd(a, b):
    while (a == 0):
        return b
    return gcd(b%a, a)

def lcm(a, b):
    c = gcd(a, b)
    a1 = a/c
    b1 = b/c
    return c * a1 * b1

a = lcm(d1, d2)
pmax = 10**digit
maxf = pmax/a
start = a * maxf
end = 10**(digit - 1)

for i in range(start, end, -1 * a):
    if (i == int(str(i)[::-1])):
        print i
        break

# second method (one line but slower)
print max(filter(lambda x: x%d1 ==0 & x%d2 ==0,[x for x in xrange(10**(digit-1), 10**digit) if str(x) == str(x)[::-1]]))




