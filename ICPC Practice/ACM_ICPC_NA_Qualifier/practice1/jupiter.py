n,q,s = [int(x) for x in input().split()]
qarray = [int(x) for x in input().split()]
qstorage = [int(x) for x in input().split()]
for i in range(n):
	cur = [int(x) for x in input().split()]
	window = cur[0]
	if sum(cur[1:])< window:
		for j in range(1,s+1):
			qarray[j-1]cur[j]
	else:
		print("impossible")
