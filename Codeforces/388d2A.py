n = int(input())
a = [0] * 100001
a[2] = 1
a[3] = 1
for i in range(3, n+1):
	last = a[i-2]
	a[i] = last + 1
if n%2 == 0:
	two = a[n]
	twos = ['2'] * a[n]
	twos = ' '.join(twos)
	print(a[n])
	print(twos)
else:
	two = a[n]
	twos = ['2'] * (a[n]-1)
	twos = ' '.join(twos)
	print(a[n])
	print(twos+' 3')