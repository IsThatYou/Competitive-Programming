cases = input().split()
n = int(cases[0])
x = int(cases[1])

array = input().split()
array = [int(x) for x in array]
'''
a = [0]*100001
for i in array:
	a[int(i)] += 1
sums = 0
for i in range(len(a)):
	if a[i]:
		num = i
		interest = num^x
		if a[interest]:
			su = a[i] * a[interest]
			sums += su
		a[i] =0
		a[interest] =0
print(sums)
'''

a = {}
for i in array:
	if i in a:
		a[i] += 1
	else:
		a[i] = 1
sums = 0

for i in a:
	if a[i] != 0:
		num = i
		interest = num^x
		if interest in a:
			if interest == i:
				su = 0
				counter = a[i]-1
				for p in range(a[i]-1):
					su += counter
					counter-=1
				sums += su
			else:
				su = a[i] * a[interest]
				sums += su
			a[interest] =0
print(sums)