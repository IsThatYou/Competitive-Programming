#https://open.kattis.com/problems/rationalsequence3
n = int(input())
for i in range(n):
	_,k = [int(x) for x in input().split()]
	bin_k = bin(k)[2:]
	p=1
	q=1
	for i in range(1,len(bin_k)):
		if bin_k[i] == '0':
			q = p+q
		elif bin_k[i] == '1':
			p = p+q
	print("{} {}/{}".format(_,p,q))