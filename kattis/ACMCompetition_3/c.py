n = int(input())
a = [int(x) for x in input().split()]
last = 2
length = 2**(-3/4)
root2 = 2**(0.5)

need = 2 
sums = 0
found = False
for i in range(len(a)):
    
    if 0<need <=2:
        sums += length
    elif need >2:
        sums += need/2 * length
    need -= a[i]
    if need <=0:
        found = True
        break
    need = need * 2
    length = length/root2
if not found:
    print("impossible")
else:
    print(sums)

