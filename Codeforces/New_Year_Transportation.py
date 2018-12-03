n,t = [int(x) for x in input().split()]
n = n-1
array = [int(x) for x in input().split()]
counter = 0
while True:
    if counter +1 == t:
        print("YES")
        break
    elif counter >n-1:
        print("NO")
        break
    counter = counter + array[counter]


