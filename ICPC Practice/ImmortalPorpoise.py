from math import sqrt
import sys
counter = 0
casenum = 0
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
def F_10(n):
	pass

def get_9(a):
	b = ''.join(list(a)[-9:])
	return int(b)

def F2(a, b, n):
	counter = 0
	while counter < n:
		c = a + b
		if c > 10**9:
			c = get_9(str(c))
		a, b = b, c
		counter += 1
	return b



fib43 = int(F(43))
fib44 = int(F(44))
find = False
i = 0

for case in sys.stdin:
	if counter == 0:
		casenum = case
		counter += 1
	else:
		inp = case.split()
		n = int(inp[1])
		fib = 0
		if n <= 44:
			fib = int(F(n))
		else:
			rest = n - 44
			fib = F2(fib43, fib44, rest)
		print(fib)
		counter += 1
