nn = input().split()
n = int(nn[0])
l = int(nn[1])
r = int(nn[2])
#s = [n]
'''
while True:
	la = True
	for i in range(len(s)):

		if s[i] > 1:
			s = s[:i]+[int(s[i]/2),s[i]%2, int(s[i]/2)]+s[i+1:]
			la = False
	if la:
		break

def f(w):
	if w == 1:
		return [1]
	if w == 0:
		return[0]
	a = f(int(w/2))
	return a + [w%2] + a
'''
lis = []
while n > 1:
	if n%2:
		lis.append(1)
	else:
		lis.append(0)
	n = int(n/2)
	print(n)
lis = lis[::-1]
llis = len(lis)
count = 0
print(lis)
print(llis)
for i in range(l,r+1):
	if i % 2:
		#print(i)
		count += 1
	else:
		for j in range(llis):
			if i - 2**(j +1) <0:
				#print(i - 2**(j +1))
				break
			if (i-2**(j +1))%(2**(j+2)) == 0:
				#print(2**(j +1))
				count += lis[j]


print(count)