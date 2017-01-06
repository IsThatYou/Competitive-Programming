#n_init = int(input()) 
#n=n_init
def sieve(n):
    mark = [i % 2 for i in range(n)]
    mark[1] = 0
    mark[2] = 1
    for value in range(3,n,2):
        if mark[value] == 1:
            for i in range(value * 3, n, value * 2):
                mark[i] = 0
    return mark
def getPrimes(m):
    sieves = sieve(m)
    primes = [i for i, f in enumerate(sieves) if f]
    return primes, sieves
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
def find(n):
	for i in range(n, -1, -1):
		if isprime(i) and (i!=(n-1)):
			return i
def main():
	n_init = int(input()) 
	n=n_init
	a = find(n)
	b = n-a
	result = 1
	while b != 0:
		n = b
		a = find(n)
		b = n-a
		result += 1
	
	if n_init%2:
		if result >3:
			result = 3
	elif n_init%2==0:
		if result >2:
			result = 2
	
	print(result)
main()
'''
for i in range(2, 2000000000):
	re = main(i)
	if re > 3:
		print(re, i)
'''
#test