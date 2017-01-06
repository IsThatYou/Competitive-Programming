def mul(A, B):

def pow(A, p):
	# for matrix
	if (p == 1):
		return A
	if (p % 2):
		return mul(A, pow(A, p-1))
	X = pow(A, p/2)
	return mul(X, X)

def pow(x, n):
	# for number
	if n < 0: 
		return pow(1/x, -1*n)
	elif n == 0:
		return 1
	elif n == 1:
		return x
	elif (n%2 == 0):
		return pow(x * x, n/2)
	elif n%2:
		return x * pow(x * x, (n-1)/2)