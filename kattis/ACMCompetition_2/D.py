import math
d,s = [int(x) for x in input().split()]
start = 0
end = 10**12
def func(a,s):
    return(a*((math.exp(d/(2*a))+math.exp(-1*(d/(2*a))) )/2-1)-s )


