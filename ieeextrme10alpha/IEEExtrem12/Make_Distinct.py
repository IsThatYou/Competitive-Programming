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
def floorSearch(arr, low, high, x): 
  
    # If low and high cross each other 
    if (low > high): 
        return -1
  
    # If last element is smaller than x 
    if (x >= arr[high]): 
        return high 
  
    # Find the middle point 
    mid = int((low + high) / 2) 
  
    # If middle point is floor. 
    if (arr[mid] == x): 
        return mid 
  
    # If x lies between mid-1 and mid 
    if (mid > 0 and arr[mid-1] <= x  
                and x < arr[mid]): 
        return mid - 1
  
    # If x is smaller than mid,   
    # floor must be in left half. 
    if (x < arr[mid]): 
        return floorSearch(arr, low, mid-1, x) 
    # If mid-1 is not floor and x is greater than 
    # arr[mid], 
    return floorSearch(arr, mid+1, high, x) 
# numpy and scipy are available for use
import numpy
arr = [0,2,4,6,1000]
x = 5
index = floorSearch(arr, 0, 4, x)
print(index)
N = get_number()
#seen = set()
line = list(map(int, input().strip().split()))
line.sort()
high_dic = [line[0]-1]
low_dic = [-2*(10e6)]
for i in range(1,N):
    if (line[i]-line[i-1] -1)>0:
        high_dic.append(line[i]-1)
        low_dic.append(line[i-1]+1)
high_dic.append(2*(10e6))
low_dic.append(line[-1]+1)
last = line[0]
for i in range(1,N):
    if line[i] == last:
        last = line[i]

# seen = set(line)
# track = [0] * (2*(10e6))
# for i in seen:
#     track[i] = 1
# cl = line[0]
# cr = line[0]
# last = line[0]
# negatives = -1
# for i in range(1,N):
#     if line[i] == last:
#         new_cr = i+1
#         if (line[i]- cl) <= (
        
        
#     else:
#         if i < N-1:
#             if line[i+1] == last:
#             new_cl = i - 1
#             while True:
#                 if track[new_cl] == 0:
#                     break
#                 else:
#                     new_cl = new_cl -1 
#                     if new_cl <0:
#                         new_cl = negatives
#     last = line[i]
            
            
            
        