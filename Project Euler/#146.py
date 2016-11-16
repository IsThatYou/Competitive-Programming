limit = 150000000
result = 0
def IsProbablePrime(num):
    for i in range(2, int(num/2)):
        remain = num % i
        if remain == 0:
            return False
    return True
                   
for i in range (10, limit, 10): 

    squared = i * i;

    if squared % 3 != 1: continue
    if squared % 7 != 2 & squared % 7 != 3: continue

    if (squared % 9 == 0 & squared % 13 == 0 & squared % 27 == 0):
        continue
    print (i)

    if IsProbablePrime(squared + 1)  and  IsProbablePrime(squared + 3) and IsProbablePrime(squared + 7) and IsProbablePrime(squared + 9) and IsProbablePrime(squared + 13) and IsProbablePrime(squared + 27) and not IsProbablePrime(squared + 19) and not IsProbablePrime(squared + 21):
        result += i
        

print (result)
