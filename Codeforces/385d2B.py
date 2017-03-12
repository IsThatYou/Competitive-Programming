cases = input().split()
n = int(cases[0])
m = int(cases[1])
h_max = 0
a = []
count = 0
finish = False
for i in range(n):
	inp = input()
	if count == 0:
		for j in inp:
			if j=='X':
				count+=1
	if count:
		this_count =0
		for j in inp:
			if j=='X':
				this_count+=1
		if this_count:
			if count != this_count:
				print('NO')
				finish=True
				break
	a.append(inp)
if not finish:
	print('YES')
