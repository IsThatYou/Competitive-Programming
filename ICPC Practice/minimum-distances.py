length = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

lowest = 2000
for i in range(length):
	for j in range(i + 1, length):
		if A[i] == A[j]:
			dis = abs(j - i)
			if dis < lowest:
				lowest = dis

if lowest != 2000:
	print(lowest)
else:
	print(-1)