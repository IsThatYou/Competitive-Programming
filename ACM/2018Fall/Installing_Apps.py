n,c = [int(x) for x in input().split()]
dic = {}
num =1
for i in range(n):
	d,s = [int(x) for x in input().split()]
	a = max(d,s)
	if a in dic:
		dic[a].append((num,d,s))
	else:
		dic[a] = [(num,d,s)]
	num += 1
dp = [[] for x in range(c+1)]
cur = []
cur_left = 1
#print(dic)
for i in range(1,c+1):
	best = []
	# print(i)
	# print(dp[i])
	for j in range(len(dp[i-1])):
		if dp[i-1][j][1]+1 >0:
			for z in dp[dp[i-1][j][1]+1]:
				if len(set(z[0]).intersection(set(dp[i-1][j][0])))>0:
					pass
				else:
					#could optimize here
					#print(z[0])
					#print(dp[i-1][j][0])
					dp[i].append((dp[i-1][j][0]+z[0],z[1]))
					break
			else:
				dp[i].append((dp[i-1][j][0], dp[i-1][j][1]+1))
		else:
			dp[i].append((dp[i-1][j][0], dp[i-1][j][1]+1))
	# print(dp)
	if i in dic:
		for j in dic[i]:
			seq = [j[0]]
			val = i - j[2]
			if val >0:
				for z in dp[val]:
					if len(set(z[0]).intersection(set(seq)))>0:
						pass
					else:
						#could optimize here
						dp[i].append((seq+z[0],z[1]))
						break
				else:
					#print(seq,val)
					dp[i].append((seq, val))
			else:
				dp[i].append((seq,val))
	#print(dp)
	#print(dp[i])
# for c in range(0,c+1):
	# print(dp[c])
#print(dp)
if len(dp[-1]) == 0:
	print(0)
else:
	longest = 0
	rua = []
	for i in dp[-1]:
		if len(i[0]) >longest:
			longest = len(i[0])
			rua = i[0]
	print(longest)
	print(' '.join(str(x) for x in rua))