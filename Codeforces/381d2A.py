inputs = input().split()
n = int(inputs[0])
a = int(inputs[1])
b = int(inputs[2])
c = int(inputs[3])
remainder = n%4
remainder = 4-remainder
least = 10000000010
if remainder == 4:
	print(0)
elif remainder == 1:
	least = a
	if (b + c)< least:
		least = b+ c
	if 3*c < least:
		least = 3*c
	print(least)
elif remainder == 2:
	if b < least:
		least = b
	if a * 2 < least:
		least = a * 2
	if c * 2 < least:
		least = c* 2
	print(least)
elif remainder == 3:
	if c< least:
		least = c
	if a * 3 < least:
		least = a* 3
	if (a+b)<least:
		least = a+b
	if (a + b*3) < least:
		least = a+b*3

	print(least)
