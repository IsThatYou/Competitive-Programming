import math
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n = n//b
    return digits[::-1]
def find_desire(b):
    result = 2147483649
    if b == 0:
        return 4
    length = math.ceil(math.sqrt(b))
    for i in range(1, length):
        if b % i == 0 and i > 3 and i < result:
            result = i
        elif b % i == 0 and b/i >3 and b/i < result:
            result = b/i
    return result

print(numberToBase(19, 8))
a = int(input())
while a != 0:
    b = a - 3
    if b >= 0:
        c = find_desire(b)
        if int(c) == 2147483649:
            print('No such base')
        else:
            print(int(c))
    else:
        print('No such base')
    a = int(input())


