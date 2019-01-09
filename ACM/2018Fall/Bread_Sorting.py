#https://open.kattis.com/problems/bread
n = int(input())
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
numofCycles = 0
r1 = [0] * len(s1)
for i in range(len(s1)):
	if r1[i] == 0:
		ori_index = i+ 1
		index = i+1
		while True:
			r1[index-1] = 1
			new_index = s1[index-1] 
			if new_index == ori_index:
				break
			index = new_index
		numofCycles += 1
numofCycles2 = 0
r2 = [0] * len(s2)
for i in range(len(s2)):
	if r2[i] == 0:
		index = i+1
		ori_index = index
		while True:
			r2[index-1] = 1
			new_index = s2[index-1] 
			if new_index == ori_index:
				break
			index = new_index
		numofCycles2 += 1
#print(numofCycles)
if (abs(numofCycles2- numofCycles)%2) == 0:
	print("Possible")
else: 
	print("Impossible")