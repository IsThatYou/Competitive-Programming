#https://codeforces.com/contest/1062/problem/D
import math
n = int(input())
arr = [0] * (n+1)
for i in range(2,n+1):
	count = 0
	#print("i:",i)
	for j in range(2, math.floor(i**0.5) +1):
		#print(j)
		if (i%j == 0):
			score = int(i/j)
			if score !=1:
				count += 4 * score
				if (j!=score):
					count += 4 * j

	arr[i] = arr[i-1] + count
#print(arr)
print(int(arr[-1]))