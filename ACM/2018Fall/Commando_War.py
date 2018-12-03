#https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=658&page=show_problem&problem=2829
case = 1
while True:
	n = int(input())
	if n== 0:
		break

	lis = []
	for i in range(n):
		b,j = [int(x) for x in input().split()]

		lis.append((b,j))

	lis = sorted(lis,key = lambda x: x[1],reverse=True)
	#print(lis)

	last = 0
	ans = 0
	koniji = []
	for i in range(0,len(lis)):
		b = lis[i][0]
		j = lis[i][1]
		last += b
		ans = max(ans,last + j)
		#koniji.append(last + j)
	last += j
	print("Case {}: {}".format(case,ans))
	case+=1
	# print(koniji)
	# for i in range(len(koniji)):
	# 	if koniji[i]> 


