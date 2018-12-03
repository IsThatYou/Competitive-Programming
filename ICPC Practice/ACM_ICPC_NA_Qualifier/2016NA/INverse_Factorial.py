import math
def calc_log(n):
	sums = 0
	for i in range(1,int(n)+1):
		sums += math.log10(i)

	return int(sums+1)
num = input().strip()
goal = len(num)
if goal == 1:
	num = int(num)
	if num == 1:
		print(1)
	elif num == 2:
		print(2)
	else:
		print(3)
else:
	start = 1
	end = 3*1e5
	#print(calc_log(5))
	for i in range(100):
		mid = math.floor((start+end)/2)
		
		num = calc_log(mid)
		#print(mid,num)
		if num == goal:
			break
		elif num<goal:
			start = mid
		else:
			end = mid
	print(mid)

