s = input()
a = set()
new=s
for i in range(len(s)):
	a.add(new)
	new = new[-1]+new[0:-1]

print(len(a))