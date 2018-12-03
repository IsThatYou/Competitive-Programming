M,S = [int(x) for x in input().split()]
int_arrays = []
for i in range(M):
	int_array = [int(x) for x in input().split()]
	int_arrays.append(int_array)
dic = {}
for i in range(S):
	for j in range(M):
		if int_arrays[j][i] in dic:
			rua = dic[int_arrays[j][i]]
			dic[int_arrays[j][i]] += 1
			if rua == M-1:
		else:
			dic[int_arrays[j][i]] = 1
	keys = list(dic.keys())
	results = []

	
	else:
		print(len(results))
		a = sorted(results)
		for i in range(len(a)-1):
			print(a[i], end=" ")
		print(a[-1])
		break

