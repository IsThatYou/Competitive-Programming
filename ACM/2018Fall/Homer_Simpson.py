#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=655&problem=1406
from sys import stdin
for line in stdin:
	m,n,t = [int(x) for x in line.split()]
	if m >n:
		temp = n
		n =m
		m = temp
	if t%m == 0:
		print(int(t/m))
	else:
		residual = t%m
		ans = t//m
		ns = n
		sol = ns % m
		counter = 2

		maxn = t//n
		solved = False
		while sol!=residual:
			sol = (ns * counter) % m
			if counter >= maxn:
				print( ans,residual)
				solved = True
				break
			counter += 1
		if not solved:
			counter -= 1
			ans = ans - ((ns*counter)//m) + counter
			print(int(ans))
