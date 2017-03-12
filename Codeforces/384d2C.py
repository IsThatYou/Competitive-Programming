n = int(input())
def gcd(a, b):
    while (a == 0):
        return b
    return gcd(b%a, a)
def lcm(a, b):
    c = gcd(a, b)
    a1 = a/c
    b1 = b/c
    return c * a1 * b1
if n*(n+1) >1000000000:
	print(-1)
else:
	print("{} {} {}".format(int(n), int(n+1), int(n*(n+1))))
'''
n_num = 2/n
done = False
for i in range(2, 10000):
	if done:
		break
	if 3/i <n_num:
		break
	if 1/i < n_num:
		for j in range(i+1, 10000):
			if 1/i + 1/j < n_num:
				if 1/i + 2/j < n_num:
					break
				else:
					r = lcm(i, j)
					if 1/i+1/j+1/r == n_num:
						print("{} {} {}".format(int(i), int(j), int(r)))
						done = True
						break
if not done:
	print(-1)

'''