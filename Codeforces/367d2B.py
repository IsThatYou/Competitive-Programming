n = int(input())
s = input()
a = 0
c = 0
g = 0
t = 0
question = 0
for i in range(len(s)):
	cha = s[i]
	if cha == "A":
		a +=1
	elif cha == "C":
		c +=1
	elif cha == "G":
		g +=1
	elif cha == "T":
		t +=1
	elif chat == "?":
		question += 0
maximum = max(a,c,g,t)
needl = maximum*4 - (a+c+g+t)
if needl < question:
	print("===")
else:
	left = question - needl
	if left % 0:
		need = needl/4
		aneed = maximum-a + need
		cneed = maximum-c+need
		gneed = maximum-g + need
		tneed = maximum-t + need
		for i in range(len(s)):
			if s[i] == "?":
				if aneed:
					s[i] = 'A'
					anned-=1
				elif cneed:
					s[i] = 'C'
					cneed-=1
				elif gneed:
					s[i] = "G"
					gneed-=1
				elif tneed:
					s[i] = "T"
					tneed-=1
		print(s)
	else:
		print("===")