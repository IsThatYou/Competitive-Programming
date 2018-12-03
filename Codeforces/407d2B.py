b1,q,l,m = [int(i) for i in input().split()]
bad = [int(i) for i in input().split()]
if abs(q) > 1 and b1 != 0:
	b2 = b1
	count = 0
	while abs(b2) <= l:
		count += 1
		if b2 in bad:
			count-=1
		b2 *= q
		'''
	for u in bad:
		i = u

		while (i%q == 0):
			i = i / q
			a = i == b1
			if a:
				break
		a = i == b1

		if (a and abs(u)<=l) or u == b1:
			count-=1
	'''
	print(count)
else:
	'''
	if abs(b1)<=l:
		if q == 1:
			if b1 in bad:
				print("0")
			else:
				print("inf")
		elif q == 0:
			if 0 in bad:
				if b1 in bad:
					print("0")
				else:
					print("1")
			else:
				print("inf")
		elif q == -1:
			if (b1 in bad) and (b2 in bad):
				print("0")
			else:
				print("inf")

	else:
		print("0")
	'''
	a1 = b1 * q
	if abs(b1) <= l:
		if b1 == 0:
			if b1 in bad:
				print("0")
			else:
				print("inf")
		elif a1 in bad:
			if b1 in bad:
				print("0")
			else:
				if a1 == 0:
					print("1")
				else:
					print("inf")
		else:
			print("inf")
	else:
		print("0")