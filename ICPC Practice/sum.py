import sys
counter = 0
casenum = 0
dynamic_sum = {}
dynamic_oi = {}
def find_between(n, dic):
	start = 0
	for i in dic.keys():
		if n < i and n > start:
			return start
		start = i
	return start
def sum_pi(n):
	sums = 0
	if n in dynamic_sum:
		sums = dynamic_sum[n]
	else:
		if n%2 == 0:

			sums = (1 + n)* n//2
		else:

			sums = ((1 + n) * (n//2)) + (n+1)//2
		dynamic_sum[n] = sums
	return sums

def sum_oi(n):
	return n*n
	'''
	if n in dynamic_oi:
		sums = dynamic_oi[n]
	else:
		sums = 0
		counter = 1
		number = 1
		start_index = find_between(n, dynamic_oi)
		if start_index != 0:
			take = dynamic_oi[start_index]
			start = take[0]
			csums = take[1]
			counter = start_index + 1
			sums += csums
			number = start + 2 
		while counter <= n:
			sums += number
			number += 2
			counter += 1
		dynamic_oi[n] = (number, sums)
	return sums
	'''
for case in sys.stdin:
	if counter == 0:
		casenum = case
		counter += 1
	else:
		inp = case.split()
		n = int(inp[1])
		a = n
		pi = sum_pi(a)
		oi = sum_oi(a)
		ei = oi + n
		print(str(counter) + ' ' + str(pi) + ' ' + str(oi) + ' ' + str(ei))
		counter += 1