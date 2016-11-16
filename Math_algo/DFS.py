adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]


def dfs_iterative(adjLists, s):
	track = []
	for a in range(len(adjLists)):
		track.append(False)
	S = []
	S.append(s)
	print(track)
	print("----")
	while len(S) != 0:
		u = S.pop()
		if not track[u]:
			track[u] = True
			print(adjLists[u])
			for w in adjLists[u]:
				S.append(w)
	print(track)
dfs_iterative(adjLists, 0)
