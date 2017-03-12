
n = int(input())
s = input()
d = []
r = []
for i in range(len(s)):
	if s[i] == 'D':
		d.append(i)
	else:
		r.append(i)

t = n
while (len(d)) and (len(r)):

    if (d[0] < r[0]):
    	t +=1
    	d.append(t)
    	del d[0]
    	del r[0]
    else:
    	t += 1
    	r.append(t)
    	del r[0]
    	del d[0]


print("R" if len(r) else "D")

