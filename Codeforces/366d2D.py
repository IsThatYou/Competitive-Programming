n = int(input())
a = {}
for i in range(n):
	bid = input().split()
	bid = (bid[0], bid[1])
	if a[bid[0]]:
		a[bid[0]].append(i)
	else:
		a[bid[0]] = [i]

print(a)

q = int(input())
for i in range(q):
	s = [x for x in range(n)]
	print(s)