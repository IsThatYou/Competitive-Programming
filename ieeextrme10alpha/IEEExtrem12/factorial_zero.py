# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
import math
def primeFactors(n): 
    # Print the number of two's that divide n 
    dic = {}
    while n % 2 == 0: 
        if 2 in dic:
            dic[2] +=1
        else:
            dic[2] = 1
        n = n / 2
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
            n = n / i 
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        if n in dic:
            dic[n] +=1
        else:
            dic[n] = 1
    return dic
#print(primeFactors(8))
# numpy and scipy are available for use
def f(x,num):
    ans = 0
    while True:
        temp = math.floor(num/x)
        if temp <= 0:
            break
        ans = ans + temp
        x = x*x
    return ans
#print(f(3,10))
def binarySearch(l, r, x,b_factor): 
    #print(x,b_factor)
    while l <= r: 
        mid = l + (r - l)//2; 
        #print(l,r, mid)        
        # Check if x is present at mid 
        if f(b_factor,mid) == x: 
            newval = mid-1
            while True:
                if f(b_factor,newval) != x:
                    break
                newval-=1
            return newval+1
                    
            #return mid 
        # If x is greater, ignore left half 
        elif f(b_factor,mid) < x: 
            l = mid + 1
        # If x is smaller, ignore right half 
            #print(f(b_factor,mid))
        else: 
            r = mid - 1
            #print(f(b_factor,mid))
      
    # If we reach here, then the element 
    # was not present 
    return -1
import numpy
import scipy

T = get_number()
for i in range(T):
    B,N = [int(x) for x in input().split()]
    base_factors = primeFactors(B)
    trailling = 0
    start = 2
    save = primeFactors(B)
    for j in base_factors:
        base_factors[j] *= N
    allnum = list(save.keys())
    allnum.sort(reverse=True)
    leading = allnum[0]
    index = binarySearch(0,10e12,N*save[leading],leading)
    if index>0:
        getout = False
        index2 = index
        for j in range(1,len(allnum)):
            goal = save[allnum[j]]*N
            cal = f(allnum[j], index)
            
            while cal < goal:
                missing = goal-cal
                index2+=1
                factors = primeFactors(index2)
                if leading in factors:
                    print(-1)
                    getout = True
                    break
                if allnum[j] in factors:
                    cal = cal + factors[allnum[j]]
            if getout:
                break
                
        if not getout:
            print(index2)
            #print(int(index))
    else:
        print(index)
    