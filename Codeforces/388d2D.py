n = int(input())
a = {}
for i in range(n):
	bid = input().split()
	bid = (bid[0], bid[1])
	if bid[0] in a:
		a[bid[0]].append(i)
	else:
		a[bid[0]] = [i]

print(a)

q = int(input())
for i in range(q):
	cases = input().split()
	k = int(cases[0])
	s = [x for x in range(n)]
	for j in range(k):
		interested = int(cases[j+1])
		for z in len(a[interested]):
			s[a[interested][z]] = -1
	
	