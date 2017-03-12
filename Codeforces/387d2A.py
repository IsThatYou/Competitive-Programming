import math
def factorize_spe(a):
	minimum = 1000005
	target = 0
	for i in range(1,math.ceil(math.sqrt(a))+1):
		if a%i == 0:
			dis = a/i - i
			if dis<minimum:
				minimum = dis
				target = i
	return target
n = int(input())
a=int(factorize_spe(n))
b= int(n/a)
print("{} {}".format(a, b))