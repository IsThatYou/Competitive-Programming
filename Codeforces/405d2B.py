n, m = [int(i) for i in input().split()]
head = []
rear = []
rears = {}
for i in range(m):
	a,b = [int(i) for i in input().split()]
	head.append(a)
	rear.append(b)
	if a not in rears:
		rears[a] = []
	rears[a].append(b)

suc = True
for i in range(len(rear)):
	if rear[i] in head:
		for j in rears[rear[i]]:
			new = False
			if head[i] in rears:
				if j in rears[head[i]]:
					new = True
			if j in rears:
				if head[i] in rears[j]:
					new = True

			#print(head[i] not in head[:i] + head[i+1:], rear[j] not in rear[:j] + rear[j+1:])
			'''
			new_head = head[:i] + head[i+1:]
			new_rear = rear[:j] + rear[j+1:]
			if (head[i] not in new_head) or (rear[j] not in new_rear):
				suc = False
				break
			else:
				for q in range(len(new_head)):
					if new_head[q] == head[i]:
						if 
			

			for q in range(len(head)):
				if head[q] == head[i]:
					if rear[q] == j:
						new = True
				elif head[q] == rear[j]:
					if rear[q] == head[i]:
						new = True
			'''
			if not new:
				suc = False
			
if suc:
	print("YES")
else:
	print("NO")


