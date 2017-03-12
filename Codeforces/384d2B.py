def fastexp(x,n):
    result = 1
    currentpower = x
    while n > 0:
        if n % 2 == 1:
            result = (result * currentpower) 

        currentpower = (currentpower * currentpower)
        n = n//2

    return result
cases = input().split()
n = int(cases[0])
k = int(cases[1])
if k % 2 != 0:
	print(1)
else:
	for i in range(2, n+1):
		a = fastexp(2, i)
		b = a/2
		if (k - b)%a ==0:
			print(i)
			break