c = input().split()
a = int(c[0])
b = int(c[1])
if a == b:
	print('1')
else:
	count = 0
	while a <= b:
		count += 1
		a *= 3
		b *= 2
	print(count)
