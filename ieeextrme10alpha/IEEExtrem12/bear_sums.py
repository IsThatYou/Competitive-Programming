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
        
def 

# numpy and scipy are available for use
import numpy
import scipy

T = get_number()

for case in range(T):
    S = get_number()
    E = get_number()
    l = 

res = a + b
print(res)