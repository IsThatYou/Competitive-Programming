case =int(input())
for i in range(case):
	l1,a1,l2,a2,l,a = [int(x) for x in input().strip().split()]
	l = l-l1-l2
	a = a - a1 - a2
	if l <l1 and l<l2:
		print("?")
		continue
	if a <a1 and a<a2:
		print("?")
		continue
	coef = a1/l1
	templ1 = a1
	templ2 = l2 * coef
	templ = l * coef
	#print(templ1,templ2,templ,a1,a2,a)
	b1 =templ2 - a2
	b2 = templ - a
	if b1 == 0 and b2==0:
		if l/min(l1,l2) < max(l1,l2)/min(l1,l2):
			print(int(l/min(l1,l2))+1,1)
		else:
			print("?")
		continue
	else:
		y = b2/b1
	if (int(y) < y):
		print("?")
		continue
	x = (l - y * l2)/l1
	if (int(x) < x):
		print("?")
		continue
	print(int(x+1),int(y+1))
