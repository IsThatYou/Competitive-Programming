def newname():
	for i in range(25):
		yield chr(65+i) + 'a'
		yield chr(65+i) + 'b'
a = input().split()
n = int(a[0])
k = int(a[1])
s = input().split()
last = False
new = newname()
ab = next(new)
lis = [ab]
remember = ab
#  did not think it through, have to put all the operation at the first index
# and then replenish the rest at the end
for i in s:
	if i == "NO":
		if not last:
			lis.append(remember)
		else:
			last = False
			lis.append(remember)
	elif i == "YES":
		if not last:
			for j in range(k-1):
				ab = next(new)
				lis.append(ab)
				remember = ab
				last = True
		else:
			ab = next(new)
			lis.append(ab)
			remember = ab

for i in range(n - len(lis)):
	ab = next(new)
	lis.append(ab)
print(' '.join(lis))