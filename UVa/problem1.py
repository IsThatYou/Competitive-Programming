
def binary_search(array, num, s,e):
    length = e-s
    mid = length//2
     
    value = array[s+mid]
    if value == num:
        return s+mid
    else:
        
        if num>value:
            if s!=e and mid != s:
                return binary_search(array, num,s+mid+1,e) 
            else:
                return -1
        else:
            if s!=e and mid !=e:
                return binary_search(array, num,s,s+mid-1)
            else:
                return -1

    
a = input().split()
n = int(a[0])
q = int(a[1])
counter = 0
while n!=0 and q!=0:
    
    array = []
    queries = []
    for i in range(n):
        a = input()
        array.append(int(a))
    for i in range(q):
        a = input()
        queries.append(int(a))
    array.sort()
    counter+=1
    print("CASE# " + str(counter)+":")
    for a0 in queries:
        result = binary_search(array, a0, 0, n-1)
        if result == -1:
            print(str(a0) + " not found")
        else:
            while array[result-1] == a0:
                result = result -1
            print(str(a0) + " found at " + str(result +1))
            print(1)
    a = input().split()
    n = int(a[0])
    q = int(a[1])
