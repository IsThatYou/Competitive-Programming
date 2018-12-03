#https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=6201
import sys 
MAX = 10**(101)
end = MAX*MAX*2
for line in sys.stdin:

	x,y = line.strip().split()
	a = x.split('/')
	b = 1
	c = y.split('/')
	d = 1
	if len(a) !=1:
		a,b = a
	else:
		a = a[0]
	if len(c) != 1:
		c,d = c
	else:
		c = c[0]
	#demonator:
	a =int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	de = b*b *d*d
	#print(de)
	l = 0
	r = end
	found1 = False
	#print("numerator")
	for i in range(1000):
		mid = int((l + r)//2)
		temp = mid * mid
		#print(temp)
		if temp==de:
			found1 = True
			break
		elif temp <de:
			l = mid
		else:
			r = mid
	if not found1:
		print("no")
	else:
		#print("demonator")
		de = a*a*d*d + c*c*b*b
		#print(de)
		l = 0
		r = end
		found2 = False
		for i in range(1500):
			mid = int((l + r)//2)
			temp = mid * mid
			if temp==de:
				found2 = True
				break
			elif temp <de:
				l = mid
			else:
				r = mid
		#print(l,r,mid)
		if not found2:
			print("no")
		else:
			#print("area")
			nu = a*c
			de = b*d
			l = 0
			r = end
			found3 = False
			#print(nu)
			for i in range(1000):
				mid = (l + r)//2
				temp = de*mid
				if temp==nu:
					found3 = True
					break
				elif temp <nu:
					l = mid
				else:
					r = mid
			#print(int(mid)-mid)
			if not found3 or (not (abs(int(mid)-mid)<1e-6)):
				print("no")
			else:
				print(int(mid/2))










