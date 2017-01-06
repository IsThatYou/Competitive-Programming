# CHECK THE METHOD HE USED

import sys
import math
counter = 0
casenum = 0
#__________________________________________
a = []
for i in range(55):
	a.append([0]*55)
a[0][0]=a[1][0]=a[1][1]=1;
for i in range(2, 51):
	a[i][0]=1;
	for j in range(1, i + 1):
		a[i][j]=a[i-1][j-1]+a[i-1][j];
#___________________________________________
def combinations(a, b):
	d = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
	return d
for case in sys.stdin:
	if counter == 0:
		casenum = case
		counter += 1
	else:
		inp = case.split()

		steps = int(inp[1])
		steps4 = int(steps//4)
		steps2 = int((steps%4)//2)
		sums = 0
		while steps4 >= steps2:
			if steps4 * 4 + steps2 * 2 == steps:
				num = 0
				#if steps2 == 0:
					#num = 1
				#else:
					#num = combinations(steps4, steps2)
				num = a[steps4 + steps2][steps2]
				pos = num**2
				sums += pos
			steps4 -= 1
			steps2 += 2
		print(inp[0]+ ' ' + str(sums))
		counter += 1