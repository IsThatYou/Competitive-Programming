n = int(input())
arr = [int(x) for x in input().strip().split()]
maximum = 1
count = 1
last = arr[0]
consec = []
notconsec = set()
cur = [arr[0]]
for i in range(1,len(arr)):
	if arr[i] == (last+1):
		count += 1
		cur.append(arr[i])
	else:
		if count >= 2:
			consec.append(cur)
		notconsec.add(arr[i] - last+1)
		count = 1
		cur = [arr[i]]
	last = arr[i]

if count >= 2:
	consec.append(cur)
# print(consec,notconsec)
ans = 0
for i in consec:
	temp = len(i)-2
	if i[0] == 1:
		temp +=1
	if i[-1]==1000:
		temp += 1
	ans = max(ans,temp)
print(ans)
