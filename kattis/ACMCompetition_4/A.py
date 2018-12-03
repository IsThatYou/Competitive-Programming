a,b,c = [int(x) for x in input().split()]
d = a + b
remainder = 0
result = 0
while d >= c:
    new_d = d//c
    remainder = d-new_d*c
    result += new_d
    d = new_d + remainder
print(result)
