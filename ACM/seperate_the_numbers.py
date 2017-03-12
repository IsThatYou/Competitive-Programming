#https://www.hackerrank.com/contests/university-codesprint-2/challenges/separate-the-numbers
q = int(input())
for qwert in range(q):
	s = input().strip()
	faulty = True
	first = ''
	for i in range(1,int(len(s)/2)+1):
		num = int(s[:i])
		if str(num) != s[:i]:
			pass
		else:
			faulty = False
			first = str(num)
			while i < len(s):
				new = num + 1
				#print(i, new, s[i:(i+len(str(new)))])
				if s[i:(i+len(str(new)))] != str(new):
					faulty = True
				num = new
				i = i + len(str(new))

			if not faulty:
				break
			else:
				first = ''
	if faulty:
		print("NO")
	else:
		print("YES", first, sep = " ")