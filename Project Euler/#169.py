# This problem has to do with binary
# 10 = 0b1010
# seperate them into 'forests' seperated by 0s
x = int(input())
count = 0
ones = []
#x = 10**25
a=10086

while a != 0:
	a = x >> count
	if a % 2 != 0:
		ones.append(count+1)
	count+=1

def find(array):
	if len(array) == 1:
		return array[0]
	
	else:
		return (array[-1] - array[-2] + 1) * find(array[:-1]) - len(array[:-1])

def find2(array):
	first = array[0]
	last = array[1]
	mult = last-first
	cons = first - 1
	result = mult * first + cons
	for i in range(2,len(array)):
		mid = array[i] -array[i-1]


		result = result * mid + cons
	return result
def find3(array):
	if len(array) == 1:
		return array[0]
	first = array[0]
	last = array[1]
	mult = last-first
	cons = first - 1
	result = mult * first + cons
	cons = result - first
	for i in range(2,len(array)):
		mid = array[i] -array[i-1]
		new_result = result * mid + cons
		cons = new_result-result
		result = new_result
	return result 
final = find3(ones)
print(final)

memo = {}
# the ultimate solution:
def f(x):
    if x in memo: 
    	return memo[x]
    if (x == 0): 
    	return 1
    ans = 0;
    if x % 2 == 1:
        ans = f(x // 2)
    else:
        ans = f(x // 2) + f(x//2 - 1)
    memo[x] = ans
    return ans
print(f(x))