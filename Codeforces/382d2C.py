n = int(input())

if n == 2:
	print(1)
elif n == 3:
	print(2)
else:
	x = 2
	y = 3
	counter = 0
	while x+ y <= n:
		x, y = y, x+y
		counter += 1
	print(2+counter)