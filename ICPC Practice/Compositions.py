import sys
counter = 0
casenum = 0
dynamic = []
for i in range(30):
	dynamic.append({})
def backinseq(back, seq):
	qu = []
	for i in seq:
		if i <= back:
			qu.append(i)
	return qu
def combine(qu):
	s = ''
	for i in range(len(qu)):
		if i + 1 == len(qu):
			s += str(qu[i]) 
		else:
			s += str(qu[i]) + ' '
	return s
def find_sub(n, seq):
	count = 0
	for i in range(1, n + 1):
		if i == n:
			if n in seq:
				count += 1
		else:
			front = n - i
			back = i
			qu = backinseq(back, seq)
			if front in seq:
				count += 2**(back-1)
			elif len(qu) > 0:
				ser = combine(qu)
				if ser in dynamic[back-1]:
					count += dynamic[back-1][ser]
				else:
					sub = find_sub(back, seq)
					dynamic[back-1][ser] = sub
					count += sub
	return count
for case in sys.stdin:
	if counter == 0:
		casenum = case
		counter += 1
	else:
		inp = case.split()
		n = int(inp[1])
		m = int(inp[2])
		k = int(inp[3])
		total = 2**(n-1)

		seq = []
		big = 0
		counte = 0
		while big <= n:
			big = m + k * counte
			counte += 1
			seq.append(big)
		a = n
		deduct = find_sub(a, seq)
		print(str(counter) + ' '  + str(total - deduct))


		counter += 1