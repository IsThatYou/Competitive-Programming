#https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=499
# shi li chin
# if there is 1 cycle that results in negative value
def recur_dfs(start,dic):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		if vertex in dic:
			for each in dic[vertex]:
				node = each[0]
				val = each[1]
				if node in path:
					ind = path.index(node)
					this_path = path[ind:]
					this_path.append(node)
					sums = 0
					for i in range(len(this_path)-1):
						this_node = this_path[i]
						next_node = this_path[i+1]
						val = 0
						for j in dic[this_node]:
							if j[0] == next_node:
								val = j[1]
						sums += val
					if sums <0:
						return True
				else:
					stack.append((node, path+[node]))
	return False


n = int(input())
for i in range(n):
	n,m = [int(x) for x in input().split()]
	dic = {}
	start = 0
	for j in range(m):
		fr,to,val = [int(x) for x in input().split()]

		if fr in dic:
			dic[fr].append((to,val))
		else:
			dic[fr] = [(to,val)]
	start = fr
	sol = recur_dfs(start,dic)
	if sol:
		print('possible')
	else:
		print('not possible')


