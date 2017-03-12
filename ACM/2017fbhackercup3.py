import math
a = open("fightingthezombie.in")
b = open("output.txt", "w", newline = "\n")
cases = int(a.readline())
for i in range(cases):
	inpu1 = a.readline()
	inpu2 = a.readline().split()
	H = int(inpu1.split()[0])
	S = int(inpu1.split()[1])
	answer = 0
	method = inpu2
	for j in range(S):
		X = int(method[j].split('d')[0])
		Y = 0
		Z = 0
		if '-' in method[j].split('d')[1]:
			Y = int(method[j].split('d')[1].split('-')[0])
			Z = -1 * int(method[j].split('d')[1].split('-')[1])
		elif '+' in method[j].split('d')[1]:
			Y = int(method[j].split('d')[1].split('+')[0])
			Z = int(method[j].split('d')[1].split('+')[1])
		else:
			Y = int(method[j].split('d')[1])
		maximum = X * Y
		minimum  = X
		below  = H - Z
		if below < 0:
			result = 1
		else:
			array = [0] * maximum
			for z in range(Y):
				array[z] = 1
			for z in range(X-1):
				newarray = [0] * maximum
				for p in range(maximum):
					sums = 0
					if p - Y >= 0:
						for u in range(p-Y, p):
							sums += array[u]
					else:
						for u in range(p):
							sums += array[u]
					newarray[p] = sums
				array = newarray
			count = 0
			sums = 0
			for z in range(maximum):
				if z == below-1:
					break 
				sums += array[z]
				if array[z] != 0:
					count += 1
			if count == 0:
				result = 1
			else:
				result = 1 - sums/(math.pow(Y, X))
		if result > answer:
			answer = result


	print("Case #{}: {:f}".format(i+1, answer), file=b)



a.close()
b.close()