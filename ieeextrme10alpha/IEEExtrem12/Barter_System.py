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
def modInverse(a, m) : 
        # If a and m are relatively prime, 
        # then modulo inverse is a^(m-2) mode m 
    return(power(a, m - 2, m)) 
# To compute x^y under modulo m 
def power(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
  
# Function to return gcd of a and b 
  
# Driver Program 
#a = 1; m = 7
#modInverse(a, m) 

# numpy and scipy are available for use
import numpy
import scipy
dic = {}
a = get_number()
for i in range(a):
    fr = get_word()
    to = get_word()
    coef = get_number()
    if fr in dic:
        dic[fr].append((to,coef))
    else:
        dic[fr] = [(to,coef)]
    if to in dic:
        dic[to].append((fr,-1*coef))
    else:
        dic[to] = [(fr,-1*coef)]

def dfs(start,nu,de,visited,to):
    if start==to:
        return [True,nu,de]
    visited.add(start)
    a = False
    b = 1
    c = 1
    for currency_child,exchange_rate in dic[start]:
        if currency_child not in visited:
            if exchange_rate>0:
                a,b,c = dfs(currency_child,(nu*exchange_rate)%998244353,de,visited,to)

            else:
                #print(exchange_rate)
                temp = modInverse(-1*exchange_rate, 998244353)
                a,b,c = dfs(currency_child,nu,(de*temp)%998244353,visited,to)
            if a:
                break
            
    return [a,b,c]
#dic2 = []
def dfs2(start,nu,de,visited,to):
    stack = [(start,nu,de)]
    while stack:
        (vertex,nu,de) = stack.pop()
        if vertex in dic2:
            if to in dic2[vertex]:
                return (1,dic2[vertex][to][0],dic2[vertex][to][1])
        if (vertex == to):
            return (1,nu,de)
        visited.add(vertex)
        for currency_child,exchange_rate in dic[vertex]:
            if currency_child not in visited:
                if exchange_rate>0:
                    temp =(nu*exchange_rate)%998244353
                    if currency_child == to:
                        return (1,temp,de)
                    else:
                        stack.append((currency_child,temp,de))
                else:
                    temp = (modInverse(-1*exchange_rate, 998244353) * de)%998244353
                    if currency_child == to:
                        return (1,nu,temp)
                    else:
                        stack.append((currency_child,nu,temp))
    return (0,1,1)

b = get_number()
for i in range(b):
    fr = get_word()
    to = get_word()

    stack = fr
    visited = set()
    numerator = 1
    denominator = 1
    #a,b,c=dfs(stack,numerator,denominator,visited,to)
    a,b,c = dfs2(stack,1,1,visited,to)
    if a:
        print((b*c)%998244353)
    else:
        print(-1)



