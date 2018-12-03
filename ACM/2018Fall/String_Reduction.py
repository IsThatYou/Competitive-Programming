#https://www.hackerrank.com/challenges/string-reduction/problem
case  = int(input())
for i in range(case):
	string = input().strip()
	a = 0
	b = 0
	c = 0
	for char in string:
		if char =='a':
			a+=1
		elif char == 'b':
			b += 1
		else:
			c += 1
	if (a==0 and b==0) or (b==0 and c==0) or (a ==0 and c ==0):
		print(a+ b+ c)
	else:
		a = a%2
		b = b%2
		c = c%2
		if (a == b) and (b== c):
			print(2)
		else:
			print(1)