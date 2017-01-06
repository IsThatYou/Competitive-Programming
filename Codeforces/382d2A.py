cases = input().split()
n = int(cases[0])
k = int(cases[1])
array = input()
t_index = 0
g_index = 0
for i in range(len(array)):
	if array[i] == 'T':
		t_index = i
	if array[i] == 'G':
		g_index = i
dis = abs(t_index - g_index)
rem = dis%k
counter = 0
if rem == 0:
	for j in range(min(t_index, g_index), max(t_index, g_index), k):
		if array[j] == '#':
			print('NO')
			counter +=1
			break
	if counter == 0:
		print('YES')
else:
	print('NO')
