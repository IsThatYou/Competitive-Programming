cases = input().split()
n = int(cases[0])
m = int(cases[1])
w = int(cases[2])
weights = input().split()
weights = [int(x) for x in weights]
beauty = input().split()
beauty = [int(x) for x in beauty]

n_list = [0]*n
hackme = []
for i in range(m):
	pair = input().split()
	pair1 = int(pair[0])
	pair2 = int(pair[1])
	added = False
	for i in hackme:
		if pair1 in i or pair2 in i:
			i.add(pair1)
			i.add(pair2)
			n_list[pair1-1]=1
			n_list[pair2-1]=1
			added = True
	if not added:
		n_list[pair1-1]=1
		n_list[pair2-1]=1
		hackme.append(set([pair1,pair2]))
for i in range(n):
	if not n[i]:
		hackme.append(i+1)
best = [(0,0)]*1000
for i in range(1, n+1):
	maxium = -1
	for j in hackme:
		if len(j) == i:
			if j>maxium:
				maxium = j
	for num in range(i):
		onum = i-1
