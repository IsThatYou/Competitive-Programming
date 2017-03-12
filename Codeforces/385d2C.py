cases = input().split()
n = int(cases[0])
m = int(cases[1])
k = int(cases[2])
ks = input().split()
indiv = [0]*(n+1)
non_index = []
a = []
d = []
result = 0
edges = []
for i in range(m):
	edge = input().split()
	fnode = edge[0]
	snode = edge[1]
	edges.append((fnode, snode))
	got_it = False
	for j in range(len(a)):
		if fnode in a[j] or snode in a[j]:
			a[j].add(fnode)
			a[j].add(snode)
			d[j].add(fnode)
			d[j].add(snode)
			indiv[int(fnode)] = 1
			indiv[int(snode)] = 1
			if snode in ks or fnode in ks:
				non_index[j] = 1
			got_it = True
	if not got_it:
		a.append(set())
		a[-1].add(snode)
		a[-1].add(fnode)
		d.append(set())
		d[-1].add(snode)
		d[-1].add(fnode)
		indiv[int(fnode)] = 1
		indiv[int(snode)] = 1
		if snode in ks or fnode in ks:
			non_index.append(1)
		else:
			non_index.append(0)
for i in range(len(d)):
	begain = 0
	for z in range(len(d[i])-1):
		new = d[i].pop()
		count = begain
		for j in range(len(edges)):
			if new in edges[j]:
				count+=1
		if (len(d[i]) - count)<=0:
			result += len(d[i]) - count+1
		else:
			result+= len(d[i]) - count
for i in range(1, len(indiv)):
	if not indiv[i]:
		max_set = 0
		max_index = -1
		if str(i) not in ks:
			for j in range(len(a)):
				if len(a[j]) >max_set:
					max_set = len(a[j])
					max_index = j
			result += len(a[max_index])
			a[max_index].add(str(i))
		else:
			a.append(set(str(i)))
			non_index.append(1)


b = []
c = []

for i in range(len(a)):
	if non_index[i] == 0:
		b.append(a[i])
	else:
		c.append(a[i])
if len(c) > 0 and len(b) >0:
	c_max = max(c)
	c_max_len = len(c_max)
	c_max_index = c.index(c_max)
	for i in range(len(b)):
		b_len = len(b[i])
		result = c_max_len * b_len
		c_max_len = len(c_max.union(b[i]))

		c[c_max_index] = c[c_max_index].union(b[i])
#for i  in range(c)
print(result)
