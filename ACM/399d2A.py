n = int(input())
s = [int(x) for x in inpu().split()]
s = sorted(s)
count = len(s)
for i in range(0,len(s)):
	if s[i] == s[0]:
		count -= 1
	elif s[i] == s[-1]:
		count-=1
print(count)dir
