n = int(input())
a = [int(x) for x in input().split()]
'''
sums = 0
for i in range(len(a)):
	sums += int(a[i])
ave = sums/len(a)
least = [1000000000, 1000000000,1000000000]
index = [0,1,2]
me1 = True
me2 = False
me3 = False
for i in range(len(a)):
	if abs(int(a[i]) - ave) < least[0]:
		index[0] = i
		least[0] = abs(int(a[i]) - ave)
	elif abs(int(a[i]) - ave) < least[1]:
		index[1] = i
		least[1] = abs(int(a[i]) - ave)
	elif abs(int(a[i]) - ave) < least[2]:
		index[2] = i
		least[2] = abs(int(a[i]) - ave)
if int(a[index[0]]) + int(a[index[1]]) > int(a[index[2]]) and int(a[index[2]]) + int(a[index[1]]) > int(a[index[0]]) and int(a[index[0]]) + int(a[index[2]]) > int(a[index[1]]):
	print ("YES")
	print(index)
else:
	print(index)
	print ("NO")
'''
a = sorted(a, reverse = True)
new = []
diff = 1000000000
for i in range(1,len(a)):
	newd = a[i-1] - a[i]
	new.append(newd)
index = 0
for i in range(1,len(new)):
	newd = new[i-1] + new[i]
	if newd < diff:
		diff = newd
		index = i
f = index-1
s = index
t = index+1
if a[f] + a[s] > a[t] and a[s] + a[t] > a[f] and a[f] + a[t] >a[s]:
	print("YES")
else:
	print("NO")
