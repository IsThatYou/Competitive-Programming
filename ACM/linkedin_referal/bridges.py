import math
def cosh(a,d,s):
    x = d/(2*x)
    cos = math.exp(-1*x) + math.exp(x)
    cos = cos/2
    return (cos*a-a-s)
def sinh(a,d,s):
    x = d/(2*x)
    sin = math.exp(x) - math.exp(-1*x)
    sin = sin/2
    return (2*a*sin)
d, s = int(input().split())
start =0
end = 10**12

while True:
    new_a = (start + end)/2
    new_b = (start+end)/3
    new_c = (2*(start+end))/3
    mid = cosh(new_a,d,s)
    left = cosh(new_b,d,s)
    right = cosh(new_c,d,s)
    if mid > left:
        if mid >right:
            if left >right:
                start = new_c

            else:
                
                
        elif mid <right:
            start = new_b
            end = new_c

